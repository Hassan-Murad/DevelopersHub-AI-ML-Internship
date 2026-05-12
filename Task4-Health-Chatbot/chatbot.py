"""
Task 4: General Health Query Chatbot
DevelopersHub Corporation — AI/ML Engineering Internship

A multi-turn health information chatbot powered by an LLM.
Uses prompt engineering and two-layer safety filtering.

Usage:
    python chatbot.py

Requirements:
    pip install anthropic
    export ANTHROPIC_API_KEY="your-key-here"
"""

import os
import re
import anthropic


# =============================================================================
# PROMPT ENGINEERING — System Prompt
# =============================================================================

SYSTEM_PROMPT = """
You are HealthBot, a friendly and knowledgeable general health information assistant.

## Your Role
- Answer general health questions clearly, warmly, and in plain language.
- Provide educational health information based on established medical knowledge.
- Help users understand common symptoms, conditions, medications, and wellness tips.

## Your Tone
- Be warm, empathetic, and reassuring — like a knowledgeable friend.
- Use simple language. Avoid excessive medical jargon.
- Structure answers with short paragraphs or bullet points for clarity.

## STRICT Safety Rules — You MUST follow these at all times
1. NEVER diagnose a user with a specific medical condition.
2. NEVER prescribe or recommend specific medications, dosages, or treatments.
3. NEVER advise users to stop taking prescribed medications.
4. If a user describes a SERIOUS or EMERGENCY symptom (chest pain, difficulty breathing,
   severe bleeding, stroke symptoms, suicidal thoughts), IMMEDIATELY direct them to
   call emergency services (911 or local equivalent) and do NOT provide other advice.
5. Always end responses about symptoms or conditions with a recommendation to consult
   a qualified healthcare professional.
6. If unsure about any health information, say so clearly and recommend a doctor.

## What You Can Help With
- Explaining what common conditions or terms mean
- General wellness advice (sleep, nutrition, hydration, exercise)
- How common over-the-counter medications generally work (not specific dosing)
- Answering "what causes X?" or "what is X?" questions
- First-aid basics for minor injuries

## Disclaimer
Always remind users that your information is educational only and does not replace
professional medical advice, diagnosis, or treatment.
""".strip()


# =============================================================================
# SAFETY FILTER — Layer 1: Pre-LLM rule-based screening
# =============================================================================

EMERGENCY_KEYWORDS = [
    r"\bchest pain\b", r"\bcan'?t breathe\b", r"\bcan not breathe\b",
    r"\bdifficulty breathing\b", r"\bshortness of breath\b",
    r"\bheart attack\b", r"\bstroke\b", r"\blosing consciousness\b",
    r"\bpassing out\b", r"\bsevere bleeding\b", r"\bsuicid\b",
    r"\bkill myself\b", r"\bend my life\b", r"\boverdos\b",
    r"\bseizure\b", r"\bunconscious\b",
]

HARMFUL_KEYWORDS = [
    r"\bhow to make\b.{0,30}\b(poison|drug|toxin)\b",
    r"\blethal dose\b", r"\bhow much .{0,20} to die\b",
    r"\bhow to harm\b", r"\bhow to hurt\b",
]

EMERGENCY_RESPONSE = (
    "🚨 This sounds like a medical emergency.\n\n"
    "Please call emergency services immediately:\n"
    "  • Pakistan: 115 (Rescue) or 1122\n"
    "  • US/Canada: 911\n"
    "  • UK: 999\n\n"
    "Do not wait — please get professional help right away."
)

HARMFUL_RESPONSE = (
    "⚠️ I'm not able to help with that request. "
    "If you're going through a difficult time, please reach out to a trusted person "
    "or a mental health professional. You're not alone."
)


def check_safety(user_input: str) -> tuple[bool, str]:
    """
    Pre-screens user input before sending to the LLM.
    Returns (is_blocked, response_message).
    """
    lowered = user_input.lower()

    for pattern in EMERGENCY_KEYWORDS:
        if re.search(pattern, lowered):
            return True, EMERGENCY_RESPONSE

    for pattern in HARMFUL_KEYWORDS:
        if re.search(pattern, lowered):
            return True, HARMFUL_RESPONSE

    return False, ""


# =============================================================================
# CHATBOT ENGINE
# =============================================================================

class HealthChatbot:
    """
    Multi-turn health information chatbot with two-layer safety filtering.
    
    Layer 1: Rule-based keyword pre-filter (no LLM cost, instant)
    Layer 2: LLM-level system prompt constraints (handles nuanced cases)
    """

    def __init__(self, client: anthropic.Anthropic, system_prompt: str,
                 model: str = "claude-sonnet-4-20250514"):
        self.client = client
        self.system_prompt = system_prompt
        self.model = model
        self.conversation_history = []

    def chat(self, user_input: str) -> str:
        """Send a message and get a response."""
        # Layer 1: Safety check
        is_blocked, safety_response = check_safety(user_input)
        if is_blocked:
            return safety_response

        # Add to history
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            # Call LLM with full conversation context
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=self.system_prompt,
                messages=self.conversation_history,
            )

            assistant_message = response.content[0].text

            # Store response in history for next turn
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            return assistant_message

        except Exception as e:
            self.conversation_history.pop()  # Roll back on failure
            return f"⚠️ Error: {str(e)}"

    def reset(self):
        """Clear conversation history."""
        self.conversation_history = []
        print("🔄 Conversation reset.\n")


# =============================================================================
# MAIN — Interactive CLI Session
# =============================================================================

def main():
    # Load API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set.")
        print("   Run: export ANTHROPIC_API_KEY='your-key-here'")
        return

    client = anthropic.Anthropic(api_key=api_key)
    bot = HealthChatbot(client=client, system_prompt=SYSTEM_PROMPT)

    print("=" * 60)
    print("🏥  HealthBot — General Health Information Assistant")
    print("=" * 60)
    print("Ask any general health question. I'll do my best to help!")
    print("⚠️  Disclaimer: For educational purposes only. Not medical advice.")
    print("\nCommands: 'reset' | 'quit'")
    print("-" * 60 + "\n")

    while True:
        try:
            user_input = input("👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n🤖 HealthBot: Take care and stay healthy! 👋")
            break

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "bye", "q"]:
            print("🤖 HealthBot: Take care and stay healthy! 👋")
            break
        elif user_input.lower() == "reset":
            bot.reset()
        else:
            response = bot.chat(user_input)
            print(f"\n🤖 HealthBot: {response}\n")
            print("-" * 60)


if __name__ == "__main__":
    main()

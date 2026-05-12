# Task 4: General Health Query Chatbot

**Name:** Muhammad Hassan Murad
**DHC ID:** DHC-2360
**Internship:** DevelopersHub Corporation — AI/ML Engineering Internship

---

## Task Objective

Build a conversational chatbot that answers general health-related questions using a Large Language Model (LLM), with a focus on **prompt engineering** and **safety handling**.

---

## Dataset / Model Used

| Component | Details |
|---|---|
| **Model** | `claude-sonnet-4-20250514` (Anthropic) |
| **API** | Anthropic Messages API |
| **Data** | No dataset required — LLM draws on trained knowledge |

---

## Features

### Prompt Engineering
- Custom system prompt defines the chatbot's **persona**, **tone**, **scope**, and **hard safety rules**
- Techniques used: role assignment, tone definition, hard constraints, output format guidance, scope definition

### Two-Layer Safety System
| Layer | Method | Purpose |
|---|---|---|
| **Layer 1** | Rule-based regex pre-filter | Instantly catches emergency keywords — zero LLM cost |
| **Layer 2** | LLM system prompt rules | Prevents diagnoses, prescriptions, and harmful advice |

### Multi-Turn Conversation
- Full conversation history passed to the LLM on every turn
- Allows coherent follow-up questions across multiple messages

---

## Key Results & Findings

- Prompt engineering significantly shapes LLM behaviour
- Two-layer safety is more robust than either method alone
- Emergency detection works before any LLM call — instant and reliable
- Multi-turn context allows natural follow-up questions

---

## Project Structure

```
Task4-Health-Chatbot/
├── health_chatbot.ipynb    # Full Jupyter Notebook
├── chatbot.py              # Standalone Python CLI script
└── README.md
```

---

## How to Run

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"

# Jupyter
jupyter notebook health_chatbot.ipynb

# CLI
python chatbot.py
```

---

## Skills Demonstrated

- ✅ Prompt design and testing
- ✅ LLM API integration (Anthropic)
- ✅ Safety handling in chatbot responses
- ✅ Multi-turn conversational agent
- ✅ Clean, modular, well-commented Python code

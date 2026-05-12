# Task 5: Mental Health Support Chatbot

**Name:** Muhammad Hassan Murad  
**DHC ID:** DHC-2360  
**Internship:** DevelopersHub Corporation — AI/ML Engineering Internship

---

## Objective

Build a chatbot that provides **supportive and empathetic responses** for stress, anxiety, and emotional wellness.

---

## Two-Method Approach

| Method | Description |
|---|---|
| **Method A** | Fine-tuning `DistilGPT2` on the EmpatheticDialogues dataset (Hugging Face Trainer API) |
| **Method B** | LLM prompt engineering with a carefully designed empathy-focused system prompt |

---

## Dataset

| Detail | Value |
|---|---|
| **Name** | EmpatheticDialogues (Facebook AI) |
| **Source** | Hugging Face Datasets |
| **Conversations** | ~25,000 across 32 emotion categories |
| **Format** | Emotion label + prompt + empathetic response |

---

## Model

- **Fine-tuning base:** `DistilGPT2` (82M parameters) — lightweight, fast to fine-tune
- **Training:** 3 epochs, 3,000 samples, learning rate 5e-5
- **Format:** `<emotion>: X | Person: Y | Support: Z`

---

## Key Features

- Empathy-first response structure (validate before advising)
- Crisis detection pre-filter with helpline resources (Pakistan + international)
- Multi-turn conversation memory
- Carefully engineered system prompt with tone examples
- Safe, non-diagnostic, non-prescriptive responses

---

## Project Structure

```
Task5-Mental-Health-Chatbot/
├── mental_health_chatbot.ipynb   # Full Jupyter Notebook
└── README.md
```

---

## How to Run

```bash
pip install transformers datasets torch accelerate anthropic

# For Method B (LLM), set your API key:
export ANTHROPIC_API_KEY="your-key-here"

jupyter notebook mental_health_chatbot.ipynb
```

> **Tip:** Run Method A on Google Colab with a free GPU for faster fine-tuning.

---

## Skills Demonstrated

- ✅ Model fine-tuning with Hugging Face Transformers & Trainer API
- ✅ Emotional tone design for safe chatbots
- ✅ Dataset loading and preprocessing (EmpatheticDialogues)
- ✅ Conversation modeling with multi-turn memory
- ✅ Prompt engineering for empathy and safety
- ✅ Crisis detection and responsible AI design

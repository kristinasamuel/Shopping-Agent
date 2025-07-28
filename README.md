# 🛍️ Shopping Assistant Agent

A smart shopping assistant built using **OpenAI Agents SDK**, **Chainlit**, and **UV**, integrated with external APIs  to help users with their shopping queries.

---

## 🚀 Features

- Built using **OpenAI Agents SDK**
- Virtual environment managed with **UV**
- Interactive UI using **Chainlit**
- API integration (e.g., Gemini API)
- Smart responses via LLM and clear agent labeling
---

## 🧪 Tasks

1. **Agent Development**  
   Build a Shopping Agent using the OpenAI Agents Framework, ensuring seamless integration with selected APIs.

2. **Query Testing**  
   After integration, test the agent by posing relevant shopping-related questions to verify accurate responses.

---

## 🔑 Environment Variables

Create a `.env` file in the root folder to securely store your API keys:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

## 📦 Installation

### Step 1: Create a Virtual Environment
```bash
uv venv .venv
```

### Step 2: Activate Environment
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

### Step 3: Install Dependencies
```
Or add packages individually:
```bash
uv add openai-agents
uv add chainlit
```
## 🧪 Run the App

```bash
chainlit run main.py
```

---
# 📸 Snap & Study — AI-Powered Study Buddy

> **Snap a photo of your study material and get instant explanations, summaries, and step-by-step solutions — powered by Google Gemini.**

Snap & Study is an intelligent, conversational AI tutor built with **Streamlit** and **Google Gemini**. Upload images of textbook pages, handwritten notes, diagrams, code snippets, or math problems and get personalized explanations, interactive quizzes, and study recaps — all in one place. At the end of a session, send yourself a clean study summary straight to **Telegram**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📷 **Image Upload** | Upload PNG/JPEG photos of notes, textbooks, whiteboards, code, diagrams, and more |
| 🤖 **AI Tutor (Gemini)** | Powered by Google Gemini for accurate, context-aware educational responses |
| 💬 **Multi-turn Chat** | Remembers context across the entire session for a natural tutoring experience |
| 📚 **Multiple Learning Modes** | EXPLAIN, SOLVE, HINT, SUMMARIZE, MAKE NOTES, QUIZ ME, EXAM PREP, SIMPLIFY, CHECK MY ANSWER |
| 📤 **Telegram Integration** | Send a formatted study recap to your Telegram at the end of a session |
| 🧑‍🎓 **Onboarding** | Personalized welcome with your name and study goal |
| 🌐 **Multilingual** | Supports English, Hindi, and Hinglish explanations |

---

## 🧠 Learning Modes

Ask the tutor using any of these commands in chat:

- **EXPLAIN** — Get a clear, beginner-friendly explanation of a concept
- **SOLVE** — Get a step-by-step solution to a problem
- **HINT** — Get guided hints without giving away the full answer
- **SUMMARIZE** — Extract key ideas and conclusions from uploaded material
- **MAKE NOTES** — Generate structured study notes with headings and key terms
- **QUIZ ME** — Get interactive questions on the topic, one at a time
- **EXAM PREP** — Create revision material, important topics, and mock questions
- **SIMPLIFY** — Get a simpler re-explanation with easier language and examples
- **CHECK MY ANSWER** — Submit your own answer and get detailed feedback

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)
- A [Telegram Bot Token](https://core.telegram.org/bots#botfather) and your Chat ID

### 1. Clone the Repository

```bash
git clone https://github.com/Madhu1539/ai-vision-studyBuddy.git
cd ai-vision-studyBuddy
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Secrets

Create the file `.streamlit/secrets.toml` and add your credentials:

```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token-here"
TELEGRAM_CHAT_ID = "your-telegram-chat-id-here"
```

> **Note:** Never commit `secrets.toml` to version control. It is already listed in `.gitignore`.

### 5. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
Snap&Study/
├── app.py                  # Main Streamlit application
├── prompts.py              # System prompt, welcome message, and Telegram summary prompt
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── secrets.toml        # API keys and secrets (not committed to git)
└── README.md
```

---

## 📦 Dependencies

```
google-genai     # Google Gemini SDK
streamlit        # Web app framework
requests         # HTTP requests (for Telegram API)
```

---

## 📤 Telegram Study Recap

After studying, click the **📤 Send to Telegram** button. The app will:

1. Ask Gemini to summarize everything discussed in the session
2. Format it into a clean, phone-friendly recap with:
   - 📌 Topics Covered
   - 💡 Key Takeaways
   - 📝 What I Learned
   - 🎯 Quick Revision Points
3. Send it directly to your configured Telegram chat

> The **Send to Telegram** button is enabled only after at least 2 messages have been exchanged.

---

## 🔒 Privacy & Safety

- All text and content within uploaded images is treated as **educational material only**
- The AI will **not** follow any instructions embedded inside images that attempt to override its behavior
- Sensitive information (passwords, tokens) visible in images will not be reproduced
- Secrets are stored locally in `.streamlit/secrets.toml` and are never sent to any third party beyond the Gemini and Telegram APIs

---

## 🛠️ Tech Stack

- **Frontend & Server**: [Streamlit](https://streamlit.io/)
- **AI Model**: [Google Gemini](https://deepmind.google/technologies/gemini/) via `google-genai` SDK
- **Notifications**: [Telegram Bot API](https://core.telegram.org/bots/api)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

<div align="center">
  Made with ❤️ for students, by a student.
</div>

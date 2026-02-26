<div align="center">

# 🏥 AI Healthcare Assistant

### An AI-powered Healthcare Chatbot built with Python & Web Technologies  
> College Project by **Saurav Danej** ([@SauravDnj](https://github.com/SauravDnj))

<br/>

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-GitHub_Pages-00c6a7?style=for-the-badge)](https://sauravdnj.github.io/AI-Healthcare-Assistant)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq AI](https://img.shields.io/badge/Groq-LLaMA_3.3-F55036?style=for-the-badge)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 About The Project

**AI Healthcare Assistant (HealthAI)** is an intelligent chatbot application designed to provide general health information, explain medical terms, and offer wellness tips — all powered by **Groq's LLaMA 3.3** large language model.

This project was built as a **college assignment** to demonstrate the practical application of AI in the healthcare domain. It comes in **two versions**:

- 🖥️ **Desktop App** — Python GUI using CustomTkinter
- 🌐 **Web App** — Pure HTML/CSS/JS, deployable on GitHub Pages

> ⚠️ **Disclaimer:** This application is for **educational purposes only** and does NOT provide real medical advice. Always consult a licensed healthcare professional.

---

## 🌐 Live Demo

👉 **[https://sauravdnj.github.io/AI-Healthcare-Assistant](https://sauravdnj.github.io/AI-Healthcare-Assistant)**

---

## ✨ Features

- 💬 **Real-time AI Chat** — Ask any health-related question and get instant responses
- 🩺 **Quick Questions Sidebar** — 6 pre-loaded healthcare topic shortcuts
- 🌙 **Modern Dark UI** — Clean, professional interface with smooth animations
- 📱 **Fully Responsive** — Works on desktop, tablet, and mobile
- 🔑 **Secure API Key Handling** — Key stored locally in browser, never on a server
- 🗑️ **Clear Chat** — Reset conversation anytime
- ⚡ **Typing Indicator** — Visual feedback while AI is generating a response
- 🧠 **Multi-turn Memory** — AI remembers context throughout the conversation

---

## 🗂️ Project Structure

```
AI-Healthcare-Assistant/
│
├── index.html          # 🌐 Web version (GitHub Pages)
├── app.py              # 🖥️  Desktop GUI (CustomTkinter)
├── openai_client.py    # 🔗 Groq API integration
└── README.md           # 📄 This file
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| ![Python](https://img.shields.io/badge/Python-blue?logo=python&logoColor=white) | Desktop application logic |
| ![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-1a73e8) | Modern Python desktop UI |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) | Web app structure |
| ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white) | Web app styling |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) | Web app interactivity |
| ![Groq](https://img.shields.io/badge/Groq_API-LLaMA_3.3-F55036) | AI model provider |

---

## 🚀 Getting Started

### 🌐 Web Version (No Installation Needed)

1. Visit the **[Live Demo](https://sauravdnj.github.io/AI-Healthcare-Assistant)**
2. Get a **free** Groq API key from [console.groq.com/keys](https://console.groq.com/keys)
3. Enter your key in the popup modal
4. Start chatting! 🎉

---

### 🖥️ Desktop Version (Local Setup)

**Step 1 — Clone the repository**
```bash
git clone https://github.com/SauravDnj/AI-Healthcare-Assistant.git
cd AI-Healthcare-Assistant
```

**Step 2 — Install dependencies**
```bash
pip install customtkinter
```

**Step 3 — Add your Groq API key**

Open `openai_client.py` and replace the key:
```python
API_KEY = "gsk_your_groq_api_key_here"
```
Get your free key at 👉 [console.groq.com/keys](https://console.groq.com/keys)

**Step 4 — Run the app**
```bash
python app.py
```

---

## 🔑 Getting a Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for a **free account**
3. Navigate to **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_...`)
5. Paste it into the app

> Groq is completely **free** and significantly faster than OpenAI!

---

## 🧠 How It Works

```
User Types Question
        ↓
JavaScript / Python captures input
        ↓
Sends to Groq API (LLaMA 3.3-70b model)
        ↓
AI generates healthcare response
        ↓
Response displayed in chat UI
```

---

## 📋 Quick Question Topics

The app includes these built-in health topic shortcuts:

- 🩸 What are symptoms of diabetes?
- 💓 How to lower blood pressure naturally?
- 🍎 What foods boost immunity?
- 😰 Signs of anxiety & how to manage it?
- 😴 How much sleep does an adult need?
- ⚖️ What is BMI & how to calculate it?

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Saurav Danej**

[![GitHub](https://img.shields.io/badge/GitHub-SauravDnj-181717?style=flat-square&logo=github)](https://github.com/SauravDnj)

---

<div align="center">

Made with ❤️ for a College Assignment

⭐ **Star this repo if you found it helpful!** ⭐

</div>

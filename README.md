# 🤖 AI Q&A Bot

A lightweight conversational AI chatbot built with **Python, Streamlit, and the Google Gemini API**.  
This project was developed as part of an internship assignment to showcase **problem-solving, rapid prototyping, and deployment skills**.  

🌐 **[Live Demo – Try the Bot](https://e5coog8qc5rzu8a4cbv2kg.streamlit.app/)**  

---

## ✨ Features  

- **Conversational AI** – Powered by Google’s **Gemini Pro** model to answer a wide range of questions.  
- **Chat History** – Maintains full conversation context within a session.  
- **Factual Safeguards** – Provides accurate current date using Python’s `datetime`, avoiding AI hallucinations.  
- **Secure API Handling** – API keys are managed with `.env` and excluded from Git using `.gitignore`.  
- **Clean UI** – Simple and intuitive interface with Streamlit.  
- **Easy Setup** – Includes `requirements.txt` for quick installation.  

📸 **Screenshot**  
*(Insert a screenshot of your running app here for better presentation!)*  

---

## 🛠 Tech Stack  

- **Backend:** Python  
- **AI Model:** Google Gemini Pro API (`google-generativeai`)  
- **UI Framework:** Streamlit  
- **Environment Management:** `python-dotenv` for secrets handling  

---

## ⚙️ Installation & Setup  

### Prerequisites  
- Python 3.9+  
- Git  

### Steps  

1. **Clone the repository**  
```bash
git clone https://github.com/aaditya-01-28/QAbot
cd QAbot
```
2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
* Copy the example file into the src directory:
```bash
cd src
cp ../.env.example .env   
```
* Add your Google Gemini API Key inside src/.env:
```bash
GOOGLE_API_KEY="YOUR_SECRET_API_KEY"
```

5. **Run the app**
From the project root:
```bash
streamlit run src/app.py
```

The app will open in your browser at http://localhost:8501


## 📝 Project Journey & Learnings

* Phase 1: Foundation – Built a CLI-based script to test Gemini API integration.

* Phase 2: Web UI – Migrated to Streamlit for a polished, interactive interface with minimal backend changes.

* Phase 3: Problem Solving – Fixed incorrect date responses by integrating Python’s datetime module for factual output.

* Phase 4: Deployment – Deployed to Streamlit Community Cloud for easy access and sharing.

This project highlighted the importance of:

* Rapid prototyping with minimal tools.

* Secure API key management.

* Understanding and handling the limitations of LLMs.

* Deploying and sharing working applications quickly.

This bot is a demonstration of adaptability, problem-solving, and hands-on AI development skills.
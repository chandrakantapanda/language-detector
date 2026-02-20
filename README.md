# 🌍 Language Detector App using Python + FastAPI

This is a simple **Language Detection Web App** built using **Python**, **FastAPI**, and **langdetect**.  
It can automatically identify the language of any text you enter — in seconds! ⚡

---

## 🚀 Features
- Detects languages like Hindi, English, French, German, Chinese, Japanese, and more.
- Built with **FastAPI** for backend and **HTML + JavaScript** for frontend.
- Real-time language detection response.
- Simple, lightweight, and beginner-friendly.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- **FastAPI**
- **Uvicorn**
- **langdetect**
- **Jinja2** (for HTML templates)

---

## 📂 Project Structure
├── main.py # FastAPI backend
├── templates/
│ └── index.html # Frontend HTML template
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/your-username/language-detector-fastapi.git
cd language-detector-fastapi

---

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # for Linux/Mac
venv\Scripts\activate       # for Windows

---

3. Install dependencies
pip install -r requirements.txt

---

4. Run the FastAPI app
uvicorn main:app --reload


---

5. Open your browser
Visit 👉 http://127.0.0.1:8000

---

🧠 How It Works

The user types any text in the input box.

The frontend sends it to the /detect API route.

The FastAPI backend uses langdetect to identify the language.

The detected language name and code are displayed instantly on screen.

---

📦 Example Output
{
  "success": true,
  "language": "Hindi",
  "code": "hi"
}

---

👨‍💻 Author

Chandrakanta Panda
🔗 YouTube: @programmerchandra

📧 Feel free to connect and share ideas!
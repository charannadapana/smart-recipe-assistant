# 🍽 Smart Recipe & Nutrition Assistant

An ingredient-based Smart Recipe Recommendation System built using **Python** and the **Spoonacular API**, optimized for free-tier API usage.

This CLI-based application allows users to search recipes using available ingredients, apply diet filters, and view nutrition details.

---

## 🚀 Features

- 🔍 Ingredient-based recipe search
- 🥗 Diet filtering (None, Vegetarian, Vegan)
- 📊 Nutrition information (Calories, Carbs, Protein, Fat)
- 🧠 Smart ranking (least missing ingredients first)
- 🎤 Voice-based ingredient input
- ⚡ Free-tier API optimized (minimal API usage)
- 🔗 Direct recipe links

---

## 🛠 Tech Stack

- Python 3.11
- Requests
- SpeechRecognition
- python-dotenv
- Spoonacular REST API
- Git & GitHub

---

## 📂 Project Structure


SmartRecipeAssistant/
│
├── main.py
├── .env (not included in repo)
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/charannadapana/smart-recipe-assistant.git
cd smart-recipe-assistant
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install requests python-dotenv SpeechRecognition pyaudio
4️⃣ Add Environment Variables

Create a .env file:

SPOONACULAR_API_KEY=your_api_key_here

⚠️ Do not share your API key publicly.

5️⃣ Run Application
python main.py
📊 How It Works

User enters ingredients (manual or voice input)

Application queries Spoonacular API

Recipes are ranked by missing ingredients

Diet filtering is applied

Nutrition details are displayed

Direct recipe link is provided

🧠 Key Learnings

REST API integration

Handling API rate limits

Free-tier optimization strategies

CLI application development

Git version control workflow

📌 Future Improvements

Convert to Flask REST API

Add web-based frontend UI

Add local caching to reduce API usage

Add database for search history

Deploy online

👨‍💻 Author

Charan Aditya Nadapana
B.Tech CSE | Backend Development Enthusiast


---

# 🚀 After Adding README

Run:

```bash
git add README.md
git commit -m "Added professional README"
git push

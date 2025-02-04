####### 🌌 AI-Powered Dream Interpreter

Welcome to AI-Powered Dream Interpreter, a Streamlit app that analyzes your dreams using AI. This tool combines psychology, mythology, and symbolic analysis to provide meaningful interpretations of your dreams.

👉 **Click this link to view the live page:** [AI Dream Interpreter]([https://ai-dream-interpreter.streamlit.app/](https://ai-dream-interpreter.streamlit.app/)


🚀 Features

✅ AI-powered dream analysis using Groq’s LLM
✅ Identifies symbols, emotions, and psychological insights
✅ Dream journal to track patterns over time
✅ Theme tracking: Find recurring symbols and emotions in your dreams
✅ Supports Streamlit Cloud Secrets for API security

📌 Setup & Installation

1️⃣ Install Dependencies

First, clone this repository and install required dependencies:

git clone https://github.com/your-repo/dream-interpreter.git
cd dream-interpreter
pip install -r requirements.txt

2️⃣ Set Up API Key

👉 Running on Streamlit Cloud?
	1.	Go to Streamlit Cloud
	2.	Navigate to Settings > Secrets
	3.	Add your Groq API Key like this:

GROQ_API_KEY = "your_groq_api_key"


	4.	Click Save, and your app will use this key automatically!

👉 Running Locally?
	1.	Create a .streamlit/secrets.toml file in your project folder:

[secrets]
GROQ_API_KEY = "your_groq_api_key"


	2.	Your local instance will now access the API key securely.

▶️ Running the App

📡 On Streamlit Cloud (Deployed Version)
	•	Open the live page: AI Dream Interpreter

💻 Locally on Your Machine

Run the following command:

streamlit run app.py

(Replace app.py with your actual script name if different.)

📜 How to Use

1️⃣ Enter your dream in the text box.
2️⃣ Click “Interpret Dream” to analyze.
3️⃣ View AI insights, including symbols, emotions, and connections.
4️⃣ Save your analysis to Dream Journal.
5️⃣ Track patterns over time in the sidebar.

🛠️ Requirements.txt

Here’s the list of required Python packages:

streamlit
groq

(Note: If using Streamlit Cloud, python-dotenv is not required.)

📝 Example Dream Analysis

💭 User Input:
“I was flying over a city, but suddenly, I lost control and started falling.”

🔮 AI Interpretation:
	•	Symbols: Flying (freedom, ambition), Falling (loss of control, anxiety)
	•	Emotional Tone: Excitement → Fear
	•	Psychological Meaning: Fear of failure in real life
	•	Mythological Connection: Similar to Icarus’ story

📌 Contributing
	1.	Fork the repository
	2.	Create a feature branch (git checkout -b feature-name)
	3.	Commit your changes (git commit -m "Add new feature")
	4.	Push to the branch (git push origin feature-name)
	5.	Open a pull request 🚀

📩 Contact


📧 Email: avi.hm24@gmail.com

Happy Dreaming! 🌙✨

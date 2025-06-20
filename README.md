🍛 Helping My Mom Decide What To Cook

An AI-powered multi-agent system that suggests personalized Indian recipes based on time, mood, weather, and available ingredients. This project simulates the way a thoughtful family member would assist in everyday cooking decisions, using contextual intelligence.

🔍 Features

🕒 Time Agent — Suggests suitable recipes based on the time of day.

🥦 Ingredients Agent — Filters recipes based on ingredients available.

🥽 Mood Agent — Recommends food depending on the user’s mood (e.g., lazy, happy, unwell).

☀️ Weather Agent — Selects dishes appropriate for current weather (hot, cold, rainy).

❤️ Fallback Comfort Food — If no strong matches are found, top comfort foods are suggested.

🧠 Multi-Agent Intelligence — Agents collaborate to filter, sort, and recommend the best meal options.

🌐 Streamlit UI — Easy-to-use web app for quick selections and results.

📅 Sample Use Case

Mom: "It’s hot, I feel lazy, and we have rice, coconut milk, and garlic."

App: "Try making Pongal, Rasam, or Prawn Malai Curry."

📁 Project Structure

HelpingMyMomDecideWhatToCook/
├── agents/                # Individual AI agents (time, mood, etc.)
├── recipes/               # Recipe JSON files
├── main.py                # CLI interface
├── AI.py                  # Streamlit frontend
├── convertCSVToJSON.py    # Tool to convert CSV recipe data
├── requirements.txt       # Python dependencies
└── README.md              # This file

🚀 Getting Started

Requirements

Python 3.10+

pip install -r requirements.txt

Run the Web App

streamlit run AI.py

Run via Command Line

python main.py

🍴 Sample Inputs

Time: morning, afternoon, evening

Mood: lazy, happy, unwell

Weather: hot, cold, rainy, any

Ingredients: e.g., rice, garlic, paneer

🚀 What's Special?

Uses cooperative AI agents, not just filters

Prioritizes human-like decisions

Comfort fallback system ensures always-relevant output

Real Indian recipe data sourced and structured with added tags

🤝 Contributing

Have ideas like a Festival Agent, Nutritional Agent, or regional cuisine expert agent? Pull requests welcome!

📄 License

MIT License — Free to use, remix, and share. Make daily cooking smarter and easier.

Built with ❤️ to help moms (and everyone else) reduce food waste and decision fatigue.


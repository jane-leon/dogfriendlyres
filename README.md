# 🐾 Barkometer

**Barkometer** is an AI-powered tool that analyzes Google Maps reviews to determine how dog-friendly a place is. It extracts relevant keywords, visualizes review patterns, and uses GPT-4 to give each location a dog-friendliness score from 0 to 10.

---

## How it Works?

- Scrapes Google Maps reviews using Apify
- 🐶 Detects direct & indirect dog-friendly keywords (e.g. "dog", "patio")
- 📊 Generate visualizations:
  - Bar chart of keyword frequency
  - Pie chart showing keyword coverage 
- 🤖 Use GPT-4 to:
  - Score dog-friendliness (0–10)
  - Explain reasoning
  - Highlight specific influential reviews
- Lists out the reviews with direct/indirect keywords

---

## Project Structure
├── data/ # Stores scraped reviews
│ └── place_reviews.csv
├── utils/ # Helper functions
│ ├── keyword_analyzer.py
│ ├── save_to_csv.py
│ └── visualizer.py #visualizations of bar/pie charts
├── venv/ # not included
├── .env # not included, must create with api keys
├── .gitignore
├── analyze_with_openai.py # GPT-4 analysis code
├── barkometer_score.py # Calls analyzer and prints results
├── main.py # Main script to run the full pipeline
├── requirements.txt # All required Python packages
└── README.md

## Getting Started
 1. Clone the repository
 2. Create and activate a virtual environment
    - Do this in terminal:
        - python3 -m venv venv
        - source venv/bin/activate #On Windows use this: venv\Scripts\activate
 3. Install Dependencies
    - pip install -r requirements.txt
 4. .env file
    - Create a .env file in the root directory with this content:
    - OPENAI_API_KEY=your_openai_api_key_here
    - APIFY_API_TOKEN=your_apify_api_key_here

## How to Use
- Run the app: python main.py and follow the terminal instructions

## Current Work In progress
- Creating the UI interface







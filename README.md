MovieLens EDA & Visualization App
This project performs exploratory data analysis (EDA) on the MovieLens 1M dataset and presents the results via an interactive Streamlit web app using Plotly.

📁 Dataset
Users: Contains demographic info like age, gender, occupation, and zipcode.

Movies: Includes movie ID, title, genres (multi-genre), and extracted release year.

Ratings: Includes user ratings (1–5) with timestamps.

🔍 EDA Insights
🎭 Demographics
Gender Distribution

Age Distribution (Binned: Under 18, 18–24, ..., 56+)

Top 10 Occupations

Top 10 Zipcodes

🎬 Genre Preferences
Top 5 genres per gender, age group, occupation, and zipcode

Genre distribution and popularity comparisons across demographic groups

⭐ Ratings Analysis
Average ratings by:

Gender per genre

Age group per genre

Occupation per genre

Zipcode

Time-based rating changes (by year)

Identification of movies with decreasing rating trends

🚀 Streamlit App Features
Built using:

Streamlit for the web interface

Plotly for interactive charts

Pandas + SQLite for querying and processing

Features:

Interactive visualizations with filters

Demographic breakdowns

Genre and rating comparisons

Clean layout for storytelling with data

🛠️ How to Run Locally
Clone this repo:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies
Launch the app:
streamlit run app.py

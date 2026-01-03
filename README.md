# Guvi_Projects
🏏 Cricbuzz LiveStats: Real-Time Cricket Insights &amp; SQL-Based Analytics

\# 🏏 Cricbuzz LiveStats



\## 📌 Problem Statement

Cricket fans and analysts often struggle to access live match data, player statistics, and historical insights in a unified, interactive dashboard. Existing platforms scatter information across multiple pages, making real-time analysis cumbersome.



\## 🎯 Project Goal

Build a Streamlit-based dashboard that integrates:

\- Live match feeds

\- Player statistics (via RapidAPI + local DB)

\- SQL-driven insights

\- Rankings (team \& player)

\- CRUD operations on a local database



The system is modular, reusable, and easy to extend.



---



\## ⚙️ Tech Stack

\- \*\*Frontend:\*\* Streamlit

\- \*\*Backend:\*\* Python, Pandas, MySQL

\- \*\*API:\*\* RapidAPI (Cricbuzz)

\- \*\*Database:\*\* MySQL with normalized schema

\- \*\*Other:\*\* Modular programming, reusable `render()` functions



---



\## 🛠 Features

\- \*\*Home Dashboard:\*\* Quick navigation to all modules

\- \*\*Live Matches:\*\* Real-time scorecards with batting/bowling stats

\- \*\*Player Stats:\*\* Search players via API and load DB stats

\- \*\*Rankings:\*\* Team \& player rankings

\- \*\*SQL Analysis:\*\* Predefined queries for cricket insights

\- \*\*CRUD Operations:\*\* Add, update, delete players in DB

\- \*\*Navigation:\*\* Quick Access + Back to Home buttons



---



\## 📊 Code Quality \& Data Transformations

\- Clear separation of concerns: each view (`home.py`, `player\_stats.py`, `sql\_analysis.py`, `rankings.py`, `crud\_operations.py`) handles its own rendering.

\- Shared DB connection logic in `utils/db\_connection.py`.

\- Pandas used for reshaping, transposing, and presenting dataframes.

\- Safe type conversions (NumPy → Python native types) in CRUD operations.



---



\## 📈 Insights

\- Top ODI run scorers

\- Venues with capacity > 25,000

\- All-rounders with 1000+ runs \& 50+ wickets

\- Close match performers

\- Year-wise batting trends (planned)



---



\## 🚀 Installation

```bash


cd Cricbuzz\_Livestats

pip install -r requirements.txt

streamlit run app.py


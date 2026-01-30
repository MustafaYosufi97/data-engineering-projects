import requests
import sqlite3
from datetime import datetime

DB_PATH = "/opt/airflow/data/league_one.db" 

def fetch_future_matches():
    
    url = f"https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4330"
    response = requests.get(url)
    data = response.json()
    
    matches = []
    if data.get("events"):
        for event in data["events"]:
            matches.append((
                event["idEvent"],
                event["strHomeTeam"],
                event["strAwayTeam"],
                event["dateEvent"],
                event.get("strTime"),
                event.get("strVenue"),
                datetime.now().isoformat()
            ))
    return matches

def load_to_sqlite(matches):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        event_id TEXT PRIMARY KEY,
        home_team TEXT,
        away_team TEXT,
        date TEXT,
        time TEXT,
        venue TEXT,
        last_updated TEXT
    )
    """)
    
    for match in matches:
        c.execute("""
        INSERT OR REPLACE INTO matches (event_id, home_team, away_team, date, time, venue, last_updated)
        VALUES (?,?, ?, ?, ?, ?, ?)
        """, match)
    
    conn.commit()
    conn.close()
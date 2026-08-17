Perfetto. ✅
Adesso creiamo il secondo file: api_client.py.
STEP 2 — Crea api_client.py
Nel repository GitHub:
Clicca Add file
Create new file
Come nome inserisci: api_client.py
Incolla questo codice:
import os
import requests


BASE_URL = "https://v3.football.api-sports.io"


def get_headers():
    api_key = os.getenv("API_FOOTBALL_KEY")

    if not api_key:
        raise ValueError("API_FOOTBALL_KEY non configurata")

    return {
        "x-apisports-key": api_key
    }


def api_get(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"

    response = requests.get(
        url,
        headers=get_headers(),
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data and data["errors"]:
        raise RuntimeError(data["errors"])

    return data


def get_leagues():
    return api_get("leagues")


def get_teams(league_id, season):
    return api_get(
        "teams",
        {
            "league": league_id,
            "season": season
        }
    )


def get_fixtures(league_id, season):
    return api_get(
        "fixtures",
        {
            "league": league_id,
            "season": season
        }
    )


def get_standings(league_id, season):
    return api_get(
        "standings",
        {
            "league": league_id,
            "season": season
        }
    )
Poi clicca Commit changes.
⚠️ Importante: non inserire qui la tua API key. La collegheremo in modo sicuro più avanti.
Quando hai fatto, scrivimi “fatto” e passiamo a app.py.

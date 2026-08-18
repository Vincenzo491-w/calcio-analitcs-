
import os
import requests
import streamlit as st


# ============================================================
# CONFIGURAZIONE PAGINA
# ============================================================

st.set_page_config(
    page_title="Calcio Analytics",
    page_icon="⚽",
    layout="wide"
)


# ============================================================
# TITOLO
# ============================================================

st.title("⚽ Calcio Analytics")
st.subheader("Sistema di analisi e pronostici calcistici")

st.write(
    "Piattaforma per analizzare campionati, squadre, "
    "classifiche e partite tramite API-Football."
)

st.divider()


# ============================================================
# API KEY
# ============================================================

def get_api_key():
    """
    Recupera la API key dalle Streamlit Secrets.
    In alternativa prova la variabile d'ambiente.
    """

    try:
        api_key = st.secrets.get("API_FOOTBALL_KEY")
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("API_FOOTBALL_KEY")

    return api_key


API_KEY = get_api_key()


if not API_KEY:
    st.error(
        "❌ API key non trovata. "
        "Inserisci API_FOOTBALL_KEY nei Secrets di Streamlit."
    )
    st.stop()


# ============================================================
# CONFIGURAZIONE API-FOOTBALL
# ============================================================

BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}


# ============================================================
# FUNZIONE: CARICA CAMPIONATI
# ============================================================
def get_leagues():
    """
    Recupera i campionati disponibili da API-Football.
    """

    url = f"{BASE_URL}/leagues"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data.get("errors"):
        st.error(f"Errore API-Football: {data['errors']}")

    if data.get("results", 0) == 0:
        st.warning("API-Football ha restituito 0 risultati.")
        st.write("Risposta API:", data)

    return data.get("response", [])
def get_leagues():
    """
    Recupera i campionati disponibili da API-Football.
    """

    url = f"{BASE_URL}/leagues"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    
data = response.json()

if data.get("errors"):
    st.error(f"Errore API-Football: {data['errors']}")

if data.get("results", 0) == 0:
    st.warning("API-Football ha restituito 0 risultati.")
    st.write("Risposta API:", data)

return data.get("response", [])

# ============================================================
# SEZIONE CAMPIONATI
# ============================================================

st.header("🌍 Campionati")

st.write(
    "Carica l'elenco dei campionati disponibili "
    "tramite API-Football."
)


if st.button("📥 Carica campionati", type="primary"):

    try:
        with st.spinner("Caricamento campionati..."):

            response = get_leagues()

        rows = []

        for item in response:

            league = item.get("league", {})
            country = item.get("country", {})

            rows.append(
                {
                    "ID": league.get("id"),
                    "Campionato": league.get("name"),
                    "Paese": country.get("name"),
                    "Tipo": league.get("type")
                }
            )

        if rows:

            st.success(
                f"✅ Caricati {len(rows)} campionati."
            )

            st.dataframe(
                rows,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "⚠️ L'API non ha restituito campionati."
            )

    except requests.exceptions.RequestException as e:

        st.error(
            f"❌ Errore nella connessione all'API: {e}"
        )

    except Exception as e:

        st.error(
            f"❌ Errore: {e}"
        )


# ============================================================
# INFORMAZIONI
# ============================================================

st.divider()

st.caption(
    "Calcio Analytics • Powered by API-Football"
)

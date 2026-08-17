

import os
import streamlit as st

from api_client import get_leagues


st.set_page_config(
    page_title="Calcio Analytics",
    page_icon="⚽",
    layout="wide"
)


st.title("⚽ Calcio Analytics")
st.subheader("Sistema di analisi e pronostici calcistici")


st.write(
    "Piattaforma per analizzare campionati, squadre, "
    "classifiche e partite tramite API-Football."
)


st.divider()


if "API_FOOTBALL_KEY" not in st.secrets:
    st.error(
        "API-Football non configurata. "
        "Inserisci API_FOOTBALL_KEY nei Secrets di Streamlit."
    )
    st.stop()


os.environ["API_FOOTBALL_KEY"] = st.secrets["API_FOOTBALL_KEY"]


st.success("✅ API-Football configurata correttamente")


st.header("🌍 Campionati disponibili")


if st.button("Carica campionati"):

    try:
        data = get_leagues()

        leagues = data.get("response", [])

        st.success(f"Campionati trovati: {len(leagues)}")

        if leagues:

            rows = []

            for item in leagues:

                league = item.get("league", {})
                country = item.get("country", {})

                rows.append(
                    {
                        "ID": league.get("id"),
                        "Campionato": league.get("name"),
                        "Paese": country.get("name"),
                        "Tipo": league.get("type"),
                    }
                )

            st.dataframe(
                rows,
                use_container_width=True
            )

    except Exception as e:

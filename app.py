import streamlit as st
 st.button("Carica campionati "): try:
        response = get_leagues()

        rows = []

        for item in response:
            league = item.get("league", {})
            country = item.get("country", {})

            rows.append({
                "ID": league.get("id"),
                "Campionato": league.get("name"),
                "Paese": country.get("name"),
                "Tipo": league.get("type")
            })

        st.dataframe(rows, use_container_width=True)

    except Exception as e:
        st.error(f"Errore API: {e}")

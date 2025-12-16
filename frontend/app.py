import streamlit as st
import requests
from loguru import logger

st.set_page_config(page_title="FastIA Template Frontend", page_icon="🧮")

st.title("🧮 Carré d'un entier")
st.write("Entrez un entier, il est envoyé au backend qui retourne son carré.")

API_URL = "http://backend:8000/calcul"

n = st.number_input("Entier", value=2, step=1)

if st.button("Calculer"):
    logger.info(f"Envoi vers API: n={n}")
    try:
        resp = requests.post(API_URL, json={"n": int(n)}, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        st.success(f"{data['n']}² = {data['carre']}")
        logger.info(f"Réponse API: {data}")
    except Exception as e:
        logger.exception("Erreur appel API")
        st.error(f"Erreur: {e}")

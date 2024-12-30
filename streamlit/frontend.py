import streamlit as st
import requests

# Titre de l'application
st.title("Prédictions Avocado - Frontend avec Streamlit")
st.write("Remplissez les informations ci-dessous pour obtenir une prédiction du prix moyen d'un avocat.")

# Configuration du slider et de l'input pour Quality1
Quality1 = st.slider(
    "Quality1 (Quantité de petites avocats vendus)",
    min_value=0.0, max_value=1000.0, step=0.1, value=0.0
)

Quality1_input = st.number_input(
    "Quality1 (Quantité de petites avocats vendus) - Input",
    min_value=0.0, max_value=1000.0, step=0.1, value=Quality1
)

# Synchronisation entre le slider et l'input
if Quality1_input != Quality1:
    Quality1_slider = Quality1_input

# Configuration du slider et de l'input pour Quality2
Quality2 = st.slider(
    "Quality2 (Quantité de moyennes avocats vendus)",
    min_value=0.0, max_value=1000.0, step=0.1, value=0.0
)

Quality2_input = st.number_input(
    "Quality2 (Quantité de moyennes avocats vendus) - Input",
    min_value=0.0, max_value=1000.0, step=0.1, value=Quality2
)
# Synchronisation entre le slider et l'input
if Quality2_input != Quality2:
    Quality2_slider = Quality2_input

# Configuration du slider et de l'input pour Quality3
Quality3 = st.slider(
    "Quality3 (Quantité de grandes avocats vendus)",
    min_value=0.0, max_value=1000.0, step=0.1, value=0.0
)

Quality3_input = st.number_input(
    "Quality3 (Quantité de grandes avocats vendus) - Input",
    min_value=0.0, max_value=1000.0, step=0.1, value=Quality3
)

# Synchronisation entre le slider et l'input
if Quality3_input != Quality3:
    Quality3_slider = Quality3_input


Small_Bags = st.slider(
    "Small Bags (Nombre de petits sacs)", 
    min_value=0, max_value=500, step=1, value=0
)

Large_Bags = st.slider(
    "Large Bags (Nombre de grands sacs)", 
    min_value=0, max_value=500, step=1, value=0
)

XLarge_Bags = st.slider(
    "XLarge Bags (Nombre de très grands sacs)", 
    min_value=0, max_value=500, step=1, value=0
)

year = st.slider(
    "Année", 
    min_value=2000, max_value=2030, step=1, value=2023
)
type_ = st.selectbox("Type", ["organic", "conventional"])
region = st.text_input("Région", "California")

# Bouton pour envoyer les données
if st.button("Prédire le prix moyen"):
    # Données à envoyer à l'API
    data = {
        "Quality1": Quality1,
        "Quality2": Quality2,
        "Quality3": Quality3,
        "Small Bags": Small_Bags,
        "Large Bags": Large_Bags,
        "XLarge Bags": XLarge_Bags,
        "year": year,
        "type": type_,
        "region": region
    }
    
    # URL de l'API Flask
    api_url = "http://localhost:8000/predict"
    
    try:
        # Requête POST à l'API
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            # Affiche le résultat de la prédiction
            prediction = response.json().get("prediction", "Erreur dans la réponse")
            st.success(f"Prix moyen prédit : {prediction}")
        else:
            st.error(f"Erreur : {response.status_code}, {response.text}")
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")

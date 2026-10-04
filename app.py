import streamlit as st

st.title("Formulaire d'accès au groupe WhatsApp")

# Champs pour les notes
Ar = st.number_input("Entrer la note de Ar:", min_value=0.0, max_value=20.0, step=0.25)
Fr = st.number_input("Entrer la note de Fr:", min_value=0.0, max_value=20.0, step=0.25)
Hg = st.number_input("Entrer la note de Hg:", min_value=0.0, max_value=20.0, step=0.25)
Ei = st.number_input("Entrer la note de Ei:", min_value=0.0, max_value=20.0, step=0.25)

if st.button("Calculer et obtenir le lien"):
    Ab = Ar + Hg + Ei
    bc = Ab * 2
    Ac = Fr * 4
    Regio = bc + Ac
    régional = Regio / 10
    
    st.success(f"Votre résultat final est : {régional:.2f}")
    
    # Lien de votre groupe WhatsApp
    st.markdown("[Cliquez ici pour rejoindre le groupe WhatsApp](https://chat.whatsapp.com/VOTRE_LIEN_ICI)")
 

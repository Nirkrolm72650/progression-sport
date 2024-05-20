import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Nom du fichier pour stocker les données
DATA_FILE = 'progression_data.csv'

# Charger les données depuis le fichier CSV
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame({
        'Séance': [],
        'Développé couché': [],
        'Ecarté incliné': [],
        'Triceps Kickback': [],
        'Barre au front Haltère': [],
        'Traction poulie haute': [],
        'Rowing Haltère': [],
        'Curl biceps haltère': [],
        'Curl marteau': [],
        'Crunch à la poulie haute': [],
        'Squat': [],
        'Presse à cuisse': [],
        'Soulevé de terre jambe tendu haltère': [],
        'Leg extension': [],
        'Développé militaire': [],
        'Elevation latérales': [],
        'Oiseau': [],
        'Face-Pull à la poulie haute': [],
        'Shrug': []
    })

# Sélection des exercices à suivre
exercises = [
    'Développé couché', 'Ecarté incliné', 'Triceps Kickback', 'Barre au front Haltère',
    'Traction poulie haute', 'Rowing Haltère', 'Curl biceps haltère', 'Curl marteau',
    'Crunch à la poulie haute', 'Squat', 'Presse à cuisse', 'Soulevé de terre jambe tendu haltère',
    'Leg extension', 'Développé militaire', 'Elevation latérales', 'Oiseau',
    'Face-Pull à la poulie haute', 'Shrug'
]
selected_exercises = st.multiselect('Sélectionnez les exercices', exercises, exercises)

# Entrée des données pour chaque séance
st.header('Entrer les données pour chaque séance')
session_number = st.number_input('Numéro de séance', min_value=1, step=1)
weights = {exercise: None for exercise in exercises}

for exercise in selected_exercises:
    weights[exercise] = st.number_input(f'Poids pour {exercise} (kg)', min_value=0.0, step=0.5)

# Bouton pour ajouter les données de la séance
if st.button('Ajouter les données'):
    if session_number not in df['Séance'].values:
        new_data = {'Séance': session_number}
        for exercise in exercises:
            new_data[exercise] = weights[exercise] if exercise in selected_exercises else None
        df = df.append(new_data, ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success(f'Données de la séance {session_number} ajoutées !')
    else:
        st.error(f'Les données pour la séance {session_number} existent déjà.')

# Affichage du graphique
st.header('Progression en termes de poids (kg) pour chaque exercice au fil des séances')
plt.figure(figsize=(12, 6))
for column in selected_exercises:
    if df[column].notna().any():
        plt.plot(df['Séance'], df[column], marker='o', label=column)

plt.title('Progression en termes de poids (kg) pour chaque exercice au fil des séances')
plt.xlabel('Séance')
plt.ylabel('Poids (kg)')
plt.legend()
plt.grid(True)

st.pyplot(plt)

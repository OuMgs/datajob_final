# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:52:04 2024

@author: AncaE - Olivia - Oumou
"""

import streamlit as st
import pandas as pd
import plotly.express as px

sidebar_name = "Données"

def run():
    st.title(":orange[Données]")
    st.subheader (":orange[Jeu de données]")
    url = "https://www.kaggle.com/c/kaggle-survey-2020/overview"
    st.write("Nous avons utilisé le jeu de données disponible sur [kaggle](%s), constitué des réponses des 20 036 participants aux 39 questions de l'enquête. Ces réponses sont réparties sur 355 colonnes. La variable cible sont les métiers situés dans la colonne « Q5 ». " % url)
    df = pd.read_csv("kaggle_survey_2020_responses.csv", sep =",", low_memory = False)
    st.dataframe(df.head())
    st.write("")
    if st.checkbox ("Afficher la description du JDD"):
        st.dataframe(df.describe())
    st.write("")
    st.subheader(":orange[Particularités]")
    st.markdown("""
Notre projet est à 100% un questionnaire, avec des questions à choix multiples ou unique. Nous avons donc dû évaluer la pertinence des réponses et traiter les valeurs manquantes de manière appropriée : 
- Si au moins une réponse avait été saisie dans une question à choix multiple, les autres réponses manquantes pour cette question étaient remplacées par « No »
- Si aucune réponse n'avait pas du tout été saisie pour une question, cette question était considérée comme déclinée et les réponses manquantes étaient remplacées par « Declined Question ».
"""
)

    st.title(":orange[Préparation des données]")
    df0 = pd.read_csv("data_job_donnees_pretraitees_NoNaN0.csv", sep =",", low_memory = False)
    st.subheader(":orange[Nettoyage du JDD]")
    st.markdown("""
Afin d'avoir un jeu de données exploitables, nous avons procédé à quelques suppressions :
- les lignes à valeurs nulles dans la colonne cible (« Q5 »)
- les colonnes vides ou incluant que des « NaN »
- la première ligne qui contenait les questions du questionnaire
"""
)
            
    st.write("")
    
    st.subheader(":orange[Réduction des dimensions]")
    
    st.write("Nous avons exclu des classes non pertinentes pour notre objectif : « Student », « Currently not employed » et « Other ». Cela a conduit à une réduction du nombre de répondants à 10 717, soit une perte d'environ 46 % par rapport au jeu de données initial. ")
    value_counts_q5 = df0['Q5'].value_counts()
    fig1 = px.pie(labels=value_counts_q5.index, values=value_counts_q5.values, names=value_counts_q5.index, color_discrete_sequence=px.colors.qualitative.Pastel)
    fig1.update_layout(title='Répartition des variables cibles avant suppression 3 classes', showlegend=True)
    st.plotly_chart(fig1)
    
    df3 = pd.read_csv("data_job_donnees_pretraitees_NoNaN.csv", sep =",", low_memory = False)
    value_counts_q5 = df3['Q5'].value_counts()
    fig2 = px.pie(labels=value_counts_q5.index, values=value_counts_q5.values, names=value_counts_q5.index, color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_layout(title='Répartition des variables cibles après suppression 3 classes', showlegend=True)
    st.plotly_chart(fig2)
    
    st.write("")
    
    st.markdown("""
Pour assurer une efficacité optimisée du modèle nous avions besoin d'un taux de réponses global maximisé. Nous avons donc enlevé les questions les moins pertinentes par rapport à l'objectif final:
- questions « alternative » (B) à destination des publics non professionnels
- questions additionnelles conditionnées à la réponse d’une question précédente.
"""
)
    df1 = pd.read_csv("data_job_donnees_pretraitees_NoNaN1.csv", sep =",", low_memory = False)
    def calculate_response_percentage(row):
        total_questions = len(row)
        declined_count = row.tolist().count("Declined Question")
        answered_count = total_questions - declined_count
        return (answered_count / total_questions) * 100

    response_percentages = df1.apply(calculate_response_percentage, axis=1)
    
    # boîte à moustaches avec Plotly
    fig3 = px.box(df1, y=response_percentages)
    fig3.update_layout(title="Taux de réponses par répondant après suppression questions alternatives et conditionnées",
                  yaxis_title="Taux de réponses (%)")
    st.plotly_chart(fig3)
    
    st.write("")
    
    st.write("Afin d'optimiser le modèle final, nous avons supprimé les questions dont le taux de réponse était inférieur à 80%.")
    st.info("Suite étape de nettoyage des données : 153 colonnes vs 355 initialement, 28 questions vs 39.")
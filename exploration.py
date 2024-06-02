# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:58:33 2024

@author: AncaE - Olivia - Oumou
"""

import streamlit as st
import pandas as pd
import plotly.express as px

sidebar_name = "Analyse exploratoire et statistique"

def run():
    st.title(":orange[Analyse exploratoire et statistique]")
    st.subheader(":orange[Exploration des données]")
    st.write("Après le nettoyage des données, nous avons une nouvelle répartition des classes :")
    df2 = pd.read_csv("data_job_donnees_pretraitees_NoNaN.csv", sep =",", low_memory = False)
    value_counts_q5 = df2['Q5'].value_counts()
    fig4 = px.pie(labels=value_counts_q5.index, values=value_counts_q5.values, names=value_counts_q5.index, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig4)
    st.write("Plus généralement, ce jeu de données nous fournit des tendances sur les profils des répondants :")
    st.markdown("""
- La majorité des répondants possèdent un diplôme niveau Master ou Licence (74%)
"""
)
    value_counts_q4 = df2['Q4'].value_counts()
    fig5 = px.bar(x = value_counts_q4.index, y = value_counts_q4.values, 
                  labels = {'x':'Niveau études', 'y' : 'Nombre de répondants'},
                  text_auto=True,
                  color = value_counts_q4.values)
    fig5.update_yaxes (range = [0,4000])
    st.plotly_chart(fig5)
    
    st.write("")
    st.markdown("""
- La majorité des répondants ont une expérience d'écriture de code comprise entre 1 et 10 ans (64%)
"""
)
    value_counts_q6 = df2['Q6'].value_counts()
    fig6 = px.bar(x = value_counts_q6.index, y = value_counts_q6.values, 
                  labels = {'x':'Nombre années écriture code', 'y' : 'Nombre de répondants'},
                  text_auto=True,
                  color = value_counts_q6.values)
    fig6.update_yaxes (range = [0,2500])
    st.plotly_chart(fig6)
    
    st.write("")
    st.markdown("""
- La tranche d'âge la plus représentée est de 22 à 34 ans (55%) 
"""
)    
    value_counts_q1 = df2['Q1'].value_counts()
    fig7 = px.bar(x = value_counts_q1.index, y = value_counts_q1.values, 
                  labels = {'x':'Age', 'y' : 'Nombre de répondants'},
                  text_auto=True,
                  color = value_counts_q1.values)
    fig7.update_yaxes (range = [0,2000])
    st.plotly_chart(fig7)
    
    st.write("")
    st.markdown("""
- La plupart des répondants ont moins de 2 ans d'expérience en apprentissage automatique (58%) 
"""
)    
    value_counts_q15 = df2['Q15'].value_counts()
    fig8 = px.bar(x = value_counts_q15.index, y = value_counts_q15.values, 
                  labels = {"x":"Nombre d'années", "y" : "Nombre de répondants"},
                  text_auto=True,
                  color = value_counts_q15.values)
    fig8.update_yaxes (range = [0,2500])
    st.plotly_chart(fig8)

    st.write("Après avoir examiné le profil global des participants, nous avons cherché à réduire le questionnaire aux dix questions les plus pertinentes.")
    st.write("Pour évaluer la relation entre la variable cible et les variables explicatives, nous avons utilisé le test du Chi2, avec deux méthodes distinctes en fonction du type de question (multiple ou unique):")
    st.image("chi2.png", width=600)
    st.write("")
    if st.checkbox ("<< Cocher cette case pour voir le Top 10 des questions"):
        st.markdown("""
1.	Quel est le niveau le plus élevé d'éducation que vous avez atteint ? 
2.	Sélectionnez les activités qui constituent une partie importante de votre rôle au travail.
3.	Quels langages de programmation utilisez-vous régulièrement ?
4.	Quels environnements de développement intégrés (IDE) utilisez-vous régulièrement ?
5.	Depuis combien d'années utilisez-vous des méthodes d'apprentissage automatique ?
6.	Quel est l'outil principal que vous utilisez pour analyser les données ?
7.	Quels frameworks d'apprentissage automatique utilisez-vous régulièrement ?
8.	Quels algorithmes d'apprentissage automatique utilisez-vous régulièrement ?
9.	Votre employeur intègre-t-il des méthodes d'apprentissage automatique ?
10.	Depuis combien d'années écrivez-vous du code et/ou programmez-vous ?
"""
)
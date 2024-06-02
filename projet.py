# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:20:08 2024

@author: AncaE - Olivia - Oumou
"""

import streamlit as st

sidebar_name = "Présentation du projet"

def run():
    st.title(":orange[DataJob]")
    st.subheader(":orange[Contexte]")
    st.write("En 2020, Kaggle a lancé une enquête majeure sur le Machine Learning et la data science, dans le but de dresser un état des lieux complet du marché de la science des données et de l'apprentissage automatique. Après un processus de nettoyage des données, dont les détails ne sont pas explicités par Kaggle, le jeu de données mis à disposition comprend les réponses de 20 036 participants. Ces participants ont des profils divers : experts ou débutants, en activité professionnelle ou non.")
    st.subheader(":orange[Objectifs du projet]")
    st.write("Ce projet vise principalement à explorer les divers profils techniques présents dans l'industrie de la data en 2020. Nous avons entrepris une analyse approfondie des compétences, des applications pratiques et des outils maîtrisés par chaque poste, dans le but de saisir pleinement la nature de chaque métier du domaine.")
    st.write("Notre objectif était la création d'un outil de recommandation ou de profilage des apprenants en fonction de leurs compétences et de leurs intérêts, tout en nous positionnant nous-mêmes dans l'industrie de la data.")


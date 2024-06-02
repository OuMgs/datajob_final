# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:04:55 2024

@author: AncaE - Olivia - Oumou
"""

import streamlit as st

sidebar_name = "Transformation des données"

def run():
    st.title (":orange[Stratégie d'encoding]")
    st.write("")
    st.image("encodage.png", use_column_width=True)
    st.write("")
    st.title (":orange[PCA]")
    st.write("")
    
    st.write ("Nous avons testé le Top10 des questions au travers de PCA :")
    if st.checkbox ("<< Cocher cette case pour revoir le Top 10 des questions"):
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
    st.image("PCA_8questions.png", use_column_width=True)
    st.image("PCA_9questions.png", use_column_width=True)
    st.image("PCA_10questions.png", use_column_width=True)
    st.write("Les questions 22 et 6 ne contribuent pas significativement à la différenciation des métiers, puisque les PCAs #10, #9 et #8 questions présentent des similarités marquées.")
    st.image("PCA_5questions.png", use_column_width=True)
    st.image("PCA_6questions.png", use_column_width=True)
    st.image("PCA_7questions.png", use_column_width=True)
    st.write("PCA 7 questions a une orientation différente mais possède une répartition similaire à #8, souffre donc des mêmes limites. En revanche, #6 montre une belle distinction vis-à-vis des axes 0. Nous nous portons donc sur cette sélection.")
    st.write("")
    
    st.warning("Les 6 questions ci-dessous permettent une distinction métier réaliste et cohérente vis-à-vis de l’industrie de la data. Pour autant nous notons une proximité réelle entre certains métiers qui risquent de troubler l’interprétation du modèle.")
    if st.checkbox ("<< Cocher cette case pour voir les 6 questions sélectionnées"):
        st.markdown("""
1.	Quel est le niveau le plus élevé d'éducation que vous avez atteint ? 
2.	Sélectionnez les activités qui constituent une partie importante de votre rôle au travail.
3.	Quels langages de programmation utilisez-vous régulièrement ?
4.	Quels environnements de développement intégrés (IDE) utilisez-vous régulièrement ?
5.	Depuis combien d'années utilisez-vous des méthodes d'apprentissage automatique ?
6.	Quel est l'outil principal que vous utilisez pour analyser les données ?

"""
)
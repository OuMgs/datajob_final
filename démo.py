# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:16:09 2024

@author: AncaE - Olivia - Oumou
"""

import streamlit as st
import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier, BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV, cross_val_score

sidebar_name = "Démo"

def run():
     ANN = joblib.load('ANN_model.joblib')
     arbre_decision = joblib.load("Arbre de Décision_model.joblib")
     extra_tree = joblib.load("Extra Trees_model.joblib")
     foret_aleatoire = joblib.load("Forêt Aléatoire_model.joblib")
     gradient_boosting = joblib.load("Gradient Boosting Classifier_model.joblib")
     KNN = joblib.load("K Plus Proches Voisins (KNN)_model.joblib")
     naive_bayes = joblib.load("Naive Bayes_model.joblib")
     regression_logistique = joblib.load("Régression Logistique_model.joblib")
     SVM = joblib.load("SVM_model.joblib")
    
     st.subheader("Veuillez sélectionner un modèle et répondre aux questions pour effectuer une prédiction.") 

     modele_choisi = st.selectbox(label='Modèle', options=["ANN", "Arbre de décision", "Extra trees", "Forêt Aléatoire", "Gradient Boosting", "K Plus Proches Voisins (KNN)", "Naives Bayes", "Régression Logistique", "SVM"])


     if modele_choisi == "ANN":
          modele_selectionne = ANN
     elif modele_choisi == "Arbre de décision":
          modele_selectionne = arbre_decision
     elif modele_choisi == "Extra trees":
          modele_selectionne =  extra_tree
     elif modele_choisi == "Forêt Aléatoire":
          modele_selectionne = foret_aleatoire
     elif modele_choisi == "Gradient Boosting":
          modele_selectionne = gradient_boosting
     elif modele_choisi == "K Plus Proches Voisins (KNN)":
          modele_selectionne =  KNN
     elif modele_choisi == "Naives Bayes":
          modele_selectionne =  naive_bayes
     elif modele_choisi == "Régression Logistique":
          modele_selectionne =  regression_logistique
     elif modele_choisi == "SVM":
          modele_selectionne =  SVM
 
     #mapping_multiple = {0: 'Declined', 1: 'No', 2: 'Yes'}
     mapping_multiple = {2: 'Yes', 1: 'No'}
     mapping_unique = {1: 'Yes', 0: 'No', }

# Mapping inverse pour convertir les réponses en valeurs numériques pour les modèles
     inverse_mapping_multiple = {v: k for k, v in mapping_multiple.items()}
     inverse_mapping_unique = {v: k for k, v in mapping_unique.items()}

# Pour rappel : encoding
# question choix multiple Q23, Q4, Q7 & Q9 --> valeur 0 = Declined / 1 = No / 2 = Yes
# question choix unique Q4, Q15 & Q38 --> valeur 0 = No / 1 = Yes

# Q5','Q23', 'Q4_', 'Q7_','Q9_', 'Q15', 'Q38']

# Définir les questions du questionnaire et leurs options
     mapping_questions = {
         '1 - Select any activities that make up an important part of your role at work: (Select all that apply)': {
             'Analyze and understand data to influence product or business decisions': 'Q23_Analyze and understand data to influence product or business decisions',
             'Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data': 'Q23_Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data',
             'Build prototypes to explore applying machine learning to new areas': 'Q23_Build prototypes to explore applying machine learning to new areas',
             'Build and/or run a machine learning service that operationally improves my product or workflows': 'Q23_Build and/or run a machine learning service that operationally improves my product or workflows',
             'Experimentation and iteration to improve existing ML models': 'Q23_Experimentation and iteration to improve existing ML models',
             'Do research that advances the state of the art of machine learning': 'Q23_Do research that advances the state of the art of machine learning',
             'None of these activities are an important part of my role at work': 'Q23_None of these activities are an important part of my role at work',
             'Other': 'Q23_Other'},
         
         '2 - What is the highest level of formal education that you have attained or plan to attain within the next 2 years?': {
             'Bachelor’s degree': 'Q4_Bachelor’s degree',
             'Doctoral degree': 'Q4_Doctoral degree',
             'I prefer not to answer': 'Q4_I prefer not to answer',
             'Master’s degree': 'Q4_Master’s degree',
             'No formal education past high school': 'Q4_No formal education past high school',
             'Professional degree': 'Q4_Professional degree',
             'Some college/university study without earning a bachelor’s degree': 'Q4_Some college/university study without earning a bachelor’s degree',},
         
         '3 - What programming languages do you use on a regular basis? (Select all that apply)': {
             'Python': 'Q7_Python',
             'R': 'Q7_R',
             'SQL': 'Q7_SQL',
             'C': 'Q7_C',
             'C++': 'Q7_C++',
             'Java': 'Q7_Java',
             'Javascript': 'Q7_Javascript',
             'Julia': 'Q7_Julia',
             'Swift': 'Q7_Swift',
             'Bash': 'Q7_Bash',
             'MATLAB': 'Q7_MATLAB',
             'Other': 'Q7_Other',},
         
         "4 - Which of the following integrated development environments (IDE's) do you use on a regular basis? (Select all that apply)": {
             'Jupyter (JupyterLab, Jupyter Notebooks, etc)': 'Q9_Jupyter (JupyterLab, Jupyter Notebooks, etc) ',
             'RStudio': 'Q9_RStudio ',
             'Visual Studio': 'Q9_Visual Studio',
             'Visual Studio Code (VSCode)': 'Q9_Visual Studio Code (VSCode)',
             'PyCharm': 'Q9_PyCharm ',
             'Spyder':  'Q9_Spyder  ',
             'Notepad++': 'Q9_Notepad++  ',
             'Sublime Text': 'Q9_Sublime Text  ',
             'Vim / Emacs': 'Q9_Vim / Emacs  ',
             'MATLAB': 'Q9_MATLAB ',
             'Other': 'Q9_Other',},
         
         "5 - For how many years have you used machine learning methods?": {
             '1-2 years': 'Q15_1-2 years',
             '10-20 years': 'Q15_10-20 years',
             '2-3 years': 'Q15_2-3 years',
             '20 or more years': 'Q15_20 or more years',
             '3-4 years': 'Q15_3-4 years',
             '4-5 years': 'Q15_4-5 years',
             '5-10 years': 'Q15_5-10 years',
             'I do not use machine learning methods': 'Q15_I do not use machine learning methods',
             'Under 1 year': 'Q15_Under 1 year',},
         
         "6 - What is the primary tool that you use at work or school to analyze data?": {
             'Advanced statistical software (SPSS, SAS, etc.)': 'Q38_Advanced statistical software (SPSS, SAS, etc.)',
             'Basic statistical software (Microsoft Excel, Google Sheets, etc.)': 'Q38_Basic statistical software (Microsoft Excel, Google Sheets, etc.)',
             'Business intelligence software (Salesforce, Tableau, Spotfire, etc.)': 'Q38_Business intelligence software (Salesforce, Tableau, Spotfire, etc.)',
             'Cloud-based data software & APIs (AWS, GCP, Azure, etc.)': 'Q38_Cloud-based data software & APIs (AWS, GCP, Azure, etc.)',
             'Local development environments (RStudio, JupyterLab, etc.)': 'Q38_Local development environments (RStudio, JupyterLab, etc.)',
             'Other': 'Q38_Other'}
     }


# Créer un formulaire pour les réponses de l'utilisateur

     responses = {}

     for section, qs in mapping_questions.items():
         st.header(section)
         for display_text, original_key in qs.items():
             if 'Q7' in original_key or 'Q9' in original_key or 'Q23' in original_key: 
                 response = st.radio(display_text, list(mapping_multiple.values()),key=original_key)
                 responses[original_key] = inverse_mapping_multiple[response]
             else: 
                 response = st.radio(display_text, list(mapping_unique.values()),key=original_key)
                 responses[original_key] = inverse_mapping_unique[response]
        
     if st.button('Prédire'):
        new_row = pd.DataFrame([responses])
        if modele_selectionne is not None:
            prediction = modele_selectionne.predict(new_row)
            probabilites = modele_selectionne.predict_proba(new_row)
            classes = modele_selectionne.classes_

    
            st.subheader(f'Le modèle {modele_choisi} prédit : {prediction}')
            st.subheader(f'Les probalités du modèle {modele_choisi} sont : ')
            for classe, probabilite in zip(classes, probabilites[0]):
                st.subheader(f'{classe} : {probabilite* 100:.2f}%')

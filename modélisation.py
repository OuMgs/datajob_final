# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:11:00 2024

@author: AncaE - Olivia - Oumou
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
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

sidebar_name = "Modélisation"

def run():
    st.title(":orange[Modélisation]")
    q5_mapping = {
        'Business Analyst': 0, 'DBA/Database Engineer': 1, 'Data Analyst': 2,
        'Data Engineer': 3, 'Data Scientist': 4, 'Machine Learning Engineer': 5,
        'Product/Project Manager': 6, 'Research Scientist': 7,
        'Software Engineer': 8, 'Statistician': 9
    }

    # Charger les données
    df = pd.read_csv("data_job_donnees_encodéesML.csv", low_memory=False)

    # Mapping inverse pour les affichages
    inverse_mapping = {v: k for k, v in q5_mapping.items()}

    # Compter le nombre de chaque titre
    count_by_title = df['Q5'].map(inverse_mapping).value_counts().reset_index()
    count_by_title.columns = ['Métiers', 'Volume']

    # Créer le graphique
    fig = px.bar(count_by_title, x='Métiers', y='Volume', title='Nombre de répondants par métier')
    fig.update_layout(xaxis=dict(tickangle=45))
    st.plotly_chart(fig)

    st.image("matrice_de_confusion.png", use_column_width=True)
    
    st.write("")
    
    st.write("Réduction du nombre de questions à la suite de l'exploration du Top10 Chi2")

    st.image("comparaison_modeles.png", use_column_width=True)
    
    grouped_columns = {}

    for column in df:
        question = column[:3]
        if question in grouped_columns:
            grouped_columns[question].append(column)
        else:
            grouped_columns[question] = [column]

    # Liste des groupes de questions à garder
    groupes_de_questions_a_garder = ['Q5', 'Q23', 'Q4_', 'Q7_', 'Q9_', 'Q15', 'Q38']
    colonnes_a_garder = []

    for groupe in groupes_de_questions_a_garder:
        if groupe in grouped_columns:
            colonnes_a_garder.extend(grouped_columns[groupe])

    # Créer le nouveau dataframe
    df2 = df[colonnes_a_garder]

    # Définir les données et les cibles
    data2 = df2.drop('Q5', axis=1)
    target2 = df2['Q5']

    # Inverser les valeurs de Q5 en utilisant le mapping inverse
    df2['Q5_inverse'] = df2['Q5'].map(inverse_mapping)

    # Supprimer les métiers ambigus
    df2 = df2[~df2['Q5_inverse'].isin(['Data Engineer', 'Statistician', 'Product/Project Manager'])]

    # Regrouper les métiers similaires
    q5_grouped_mapping = {
        'Business Analyst': 'Analyst',
        'DBA/Database Engineer': 'Engineer',
        'Data Analyst': 'Analyst',
        'Data Scientist': 'Scientist',
        'Machine Learning Engineer': 'Scientist',
        'Research Scientist': 'Scientist',
        'Software Engineer': 'Engineer',
    }

    # Mapper les classes regroupées dans une nouvelle colonne
    df2['Q5_grouped'] = df2['Q5_inverse'].map(q5_grouped_mapping)
    
    st.write("")

    # Compter le nombre de chaque titre
    st.subheader(":orange[Regroupement des métiers similaires]")
    st.markdown("""
- Analyst = Business Analyst / Data Analyst 
- Engineer = DBA/Database Engineer / Software Engineer
- Scientist = Data Scientist / Machine Learning Engineer / Research Scientist
"""
)
    st.write("Suppression des métiers trop ambigus et touche-à-tout : Data Engineer, Statistician, Product/Project Manager")

    count_by_title_df2 = df2['Q5_grouped'].value_counts().reset_index()
    count_by_title_df2.columns = ['Métiers', 'Volume']

    # Créer le graphique
    fig2 = px.bar(count_by_title_df2, x='Métiers', y='Volume', title='Nombre de répondants par métier')
    fig2.update_layout(xaxis=dict(tickangle=45))
    st.plotly_chart(fig2)

    st.title(":orange[Initialisation des modèles]")
    st.write("")
    st.image("accuracy.png", use_column_width=True)

    # Supprimer les colonnes inutiles
    df2.drop(['Q5', 'Q5_inverse'], axis=1, inplace=True)

    # Assurer la cohérence des fonctionnalités pour l'entraînement et les tests
    X = df2.drop('Q5_grouped', axis=1)
    y = df2['Q5_grouped']

    # Séparer les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Trouver les colonnes manquantes dans X_test et les ajouter
    missing_cols = set(X_train.columns) - set(X_test.columns)
    for c in missing_cols:
        X_test[c] = 0

    # Réordonner les colonnes pour qu'elles soient dans le même ordre que dans X_train
    X_test = X_test[X_train.columns]

    # Charger les modèles
    ANN = joblib.load('ANN_model.joblib')
    arbre_decision = joblib.load("Arbre de Décision_model.joblib")
    extra_tree = joblib.load("Extra Trees_model.joblib")
    foret_aleatoire = joblib.load("Forêt Aléatoire_model.joblib")
    gradient_boosting = joblib.load("Gradient Boosting Classifier_model.joblib")
    KNN = joblib.load("K Plus Proches Voisins (KNN)_model.joblib")
    naive_bayes = joblib.load("Naive Bayes_model.joblib")
    regression_logistique = joblib.load("Régression Logistique_model.joblib")
    SVM = joblib.load("SVM_model.joblib")

    # Sélection du modèle
    modele_choisi = st.selectbox(label='Modèle', options=["ANN", "Arbre de décision", "Extra trees", "Forêt Aléatoire", "Gradient Boosting", "K Plus Proches Voisins (KNN)", "Naives Bayes", "Régression Logistique", "SVM"])

    # Fonction pour obtenir les prédictions
    def obtenir_predictions(modele_choisi):
        if modele_choisi == "ANN":
            y_pred = ANN.predict(X_test)
        elif modele_choisi == "Arbre de décision":
            y_pred = arbre_decision.predict(X_test)
        elif modele_choisi == "Extra trees":
            y_pred = extra_tree.predict(X_test)
        elif modele_choisi == "Forêt Aléatoire":
            y_pred = foret_aleatoire.predict(X_test)
        elif modele_choisi == "Gradient Boosting":
            y_pred = gradient_boosting.predict(X_test)
        elif modele_choisi == "K Plus Proches Voisins (KNN)":
            y_pred = KNN.predict(X_test)
        elif modele_choisi == "Naives Bayes":
            y_pred = naive_bayes.predict(X_test)
        elif modele_choisi == "Régression Logistique":
            y_pred = regression_logistique.predict(X_test)
        elif modele_choisi == "SVM":
            y_pred = SVM.predict(X_test)
        return y_pred

    # Obtenir les prédictions en fonction du modèle sélectionné
    y_pred = obtenir_predictions(modele_choisi)

    # Calculer la précision et le rapport de classification
    accuracy = accuracy_score(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Afficher les résultats
    st.write("Accuracy", accuracy)
    st.write("Rapport de classification:", class_report)

    # Calculer la matrice de confusion avec toutes les classes possibles
    all_classes = list(set(y_train) | set(y_test))
    conf_matrix = confusion_matrix(y_test, y_pred, labels=all_classes)

    # Convertir la matrice de confusion en dataframe avec les labels appropriés
    conf_matrix_df = pd.DataFrame(conf_matrix, index=all_classes, columns=all_classes)
    conf_matrix_percent = conf_matrix_df.div(conf_matrix_df.sum(axis=1), axis=0) * 100

    # Créer la heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(conf_matrix_percent, annot=True, fmt=".2f", cmap='RdYlBu' )
    heatmap.set_xlabel('Valeurs Prédites')
    heatmap.set_ylabel('Valeurs Réelles')
    heatmap.set_title('Matrice de Confusion (Pourcentages)')
    st.pyplot(plt)


    # # Calcul des taux à partir de la matrice de confusion
    # TP = conf_matrix[1, 1]
    # FP = conf_matrix[0, 1]
    # TN = conf_matrix[0, 0]
    # FN = conf_matrix[1, 0]

    # TPR = TP / (TP + FN)  # Taux de vrais positifs
    # FPR = FP / (FP + TN)  # Taux de faux positifs
    # TNR = TN / (TN + FP)  # Taux de vrais négatifs
    # FNR = FN / (FN + TP)  # Taux de faux négatifs
    # st.write("Taux de vrais positifs", TPR*100)
    # st.write("Taux de faux positifs", FPR*100)
    # st.write("Taux de vrais négatifs", TNR*100)
    # st.write("Taux de faux négatifs", FNR*100)
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:11:40 2024

@author: AncaE - Olivia - Oumou
"""
from collections import OrderedDict
import streamlit as st

from tabs import projet, données, exploration, transformation, modélisation, démo

TABS = OrderedDict(
    [
        (projet.sidebar_name, projet),
        (données.sidebar_name, données),
        (exploration.sidebar_name, exploration),
        (transformation.sidebar_name, transformation),
        (modélisation.sidebar_name, modélisation),
        (démo.sidebar_name, démo)
    ]
)

# Définir les couleurs
primaryColor="#FF4B4B"
backgroundColor="#C18E60"
secondaryBackgroundColor="#B1B7CB"
textColor="#31333F"
font="serif"

def run():
    st.sidebar.title("DataJob")
    st.sidebar.text("")
    tab_name = st.sidebar.radio("Menu", list(TABS.keys()), 0)
    st.sidebar.image(
        r"C:\Users\AncaE\projet_fil_rouge\photo_data.jpg", use_column_width=True,
    )
    st.sidebar.text("")
    container = st.sidebar.container(border=True)
    container.write("Formation continue - Data Analyst - Octobre 2023")
    container.write("Olivia SOULABAILLE")
    container.write ("Oumou MAGASSA")
    container.write("Anca DELVAL-CULCEA")
    
    tab = TABS[tab_name]

    tab.run()

if __name__ == "__main__":
    run()
 
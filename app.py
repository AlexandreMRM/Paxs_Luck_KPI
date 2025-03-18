import streamlit as st
import Paxs_IN
import Ranking_Vendedores
import Paxs_Luck_Geral


st.set_page_config(layout='wide')

abas = st.tabs(['Paxs IN', 'Paxs Luck Geral', 'Ranking Vendedores'])

with abas[0]:
    Paxs_IN.Paxs_IN()

with abas[1]:
    Paxs_Luck_Geral.Paxs_Luck_Geral()

with abas[2]:
    Ranking_Vendedores.Ranking_Vendedores()
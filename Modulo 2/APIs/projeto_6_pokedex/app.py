import streamlit as st
import requests 
import json

st.title("Pokedex")

with open("pokemon_index.json", "r", encoding="utf-8") as arquivo:
    lista_pokemons = json.load(arquivo)

st.title("Pokedex")

nome_pokemon = st.selectbox("Escolha um Pokemón", lista_pokemons.values())

dados_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_pokemon}').json()

st.subheader(dados_pokemon['name'].title())
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import json
from PIL import Image

# Load Model
with open('model.pkl', 'rb') as file_1:
  model = joblib.load(file_1) 

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = joblib.load(file_2) 

with open('list_num_cols.txt', 'r') as file_3: 
  list_num_cols = json.load(file_3) 

with open('list_cat_columns.txt', 'r') as file_4: 
  list_cat_cols = json.load(file_4)

def run():
    logo= Image.open('lol logo.png')
    st.image(logo, caption='source: https://www.leagueoflegends.com/en-us/ ')
    
    # membuat title
    st.title('Predict Your Ranked Games Base on First 10 minutes')
    # membuat Form
    with st.form(key= 'form_parameter'):
        gold_diff = st.number_input('Gold Difference', min_value=-15000, max_value=15000, value=0)# 'value=' merupakan nilai default
        jung_monster_killed = st.number_input('Jungle Monsters Killed', min_value= 0,max_value= 150, value=40)
        tower_destroyed = st.number_input('Towers Destroyed', min_value= 0,max_value= 9, value=0)
        blue_death = st.number_input('Team Deaths', min_value= 0,max_value= 40, value=0)

        dragon = st.selectbox('First Dragons (1 for Yes)', (0,1), index=1)
        first_blood = st.selectbox('First Blood (1 for Yes)',(0,1),index=1)
        st.markdown('---')


        submitted = st.form_submit_button('Predict')

    data_inf={
        "blueGoldDiff": gold_diff,
        'blueTotalJungleMinionsKilled': jung_monster_killed,
        'blueTowersDestroyed': tower_destroyed,
        'blueDragons': dragon,
        'blueFirstBlood': first_blood,
        'blueDeaths': blue_death,
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        # membuat kolom numerik dan kategorik
        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Feature Scaling
        data_inf_num_scaled = model_scaler.transform(data_inf_num)

        # Menggabungkan kembali kolom numerik dan kategorik
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat], axis=1)

        # melakukan prediksi
        y_pred_inf = model.predict(data_inf_final)

        # membuat probabilitas dari prediksi
        proba_df = model.predict_proba(data_inf_final)

        if y_pred_inf == 1:
          output= 'Win'
        else:
          output= 'Lost'

        st.write('## Prediction = ', output )
        st.write('## Winning probability = ', str(proba_df[:,1]*100),'%')


if __name__ == '__main__':
    run()
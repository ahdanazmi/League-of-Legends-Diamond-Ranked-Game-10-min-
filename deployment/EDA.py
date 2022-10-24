import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def run():
    logo= Image.open('lol logo.png')
    st.image(logo, caption='source: https://www.leagueoflegends.com/en-us/ ')
    # membuat title
    st.title('League of Legends Diamond Ranked Games (10 min)')

    # Membuat sub header
    st.subheader("Classify LoL ranked games outcome by looking at the first 10min worth of data")
    st.write('By Ahdan')
    # Membuat garis lurus dengan markdown

    st.markdown('---')

    # Magic Syntax
    st.write(
    """
    League of Legends is a MOBA (multiplayer online battle arena) where 2 teams (blue and red) face off. There are 3 lanes, a jungle, and 5 roles. The goal is to take down the enemy Nexus to win the game.

    This dataset contains the first 10min. stats of approx. 10k ranked games (SOLO QUEUE) from a high ELO (DIAMOND I to MASTER). Players have roughly the same level.

    Each game is unique. The gameId can help you to fetch more attributes from the Riot API.

    File source: https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min

    Data source: https://developer.riotgames.com/apis
    """
    )
   # load data
    st.write('#### Raw Table')
    df= pd.read_csv('high_diamond_ranked_10min.csv')
    st.dataframe(df)

    # Analisa data

    # First Blood
    st.write('### Whats make your team win the game?')
    st.write('#### First Blood')

    

    fig= plt.figure(figsize = (18,7))
    sns.countplot(x=df['blueFirstBlood'], hue=df['blueWins'], data=df)
    positions = (0,1)
    labels = ('No','Yes')
    plt.title('Blue Team Win vs Get First Blood')
    plt.xticks(positions,labels)
    plt.xlabel('Blue Team get the First Blood?')
    st.pyplot(fig)
    st.write('Getting the First Blood will give your team extra gold and make your team more confident')
    
    # Herald
    st.write('#### Rift Herald')
    herald= Image.open('herald.jpg')
    st.image(herald)
    
    fig= plt.figure(figsize = (18,7))
    sns.countplot(x=df['blueHeralds'], hue=df['blueWins'], data=df)
    positions = (0,1)
    labels = ('No','Yes')
    plt.title('Blue Team Win vs Get First Herald')
    plt.xticks(positions,labels)
    plt.xlabel('Blue Team get the First Herald?')
    st.pyplot(fig)
    st.write('Getting the Herald will give your team extra gold, exp poin and a tower destroyer. But its definitely not the end of the game if your team dont get the Rift Herald. So dont worry and try to find other objectives')

    
    # First Dragon
    st.write('#### First Dragon')
    dragon= Image.open('elemental dragon.jpg')
    st.image(dragon)
    
    fig= plt.figure(figsize = (18,7))
    sns.countplot(x=df['blueDragons'], hue=df['blueWins'], data=df)
    positions = (0,1)
    labels = ('No','Yes')
    plt.title('Blue Team Win vs Get First Dragon')
    plt.xticks(positions,labels)
    plt.xlabel('Blue Team get the First Dragon?')
    st.pyplot(fig)
    st.write('Getting the first dragon will give your team extra gold, exp poin and a stacks for Dragon Soul Buff. But its okay if your team dont get it. So dont push your self into a team fight and try to farm first')

    # membuat grafik persebaran 
    st.write('#### More Gold and Exp Poin')
    victory= Image.open('victory2.jpg')
    st.image(victory)
    
    fig= plt.figure(figsize = (18,7))
    sns.scatterplot(x=df.blueTotalGold,y=df.blueTotalExperience, hue=df['blueWins'], data=df)
    plt.title('Blue Teams win base on total Gold and Experience')
    st.pyplot(fig)
    st.write('Having a better farming will put your team ahead in the mid game battle. But if you are dominated by the enemy at the early the game, just be patient and try to find a way out. Because based on the data, your team still have a chance to comeback')
if __name__ == '__main__':
    run()
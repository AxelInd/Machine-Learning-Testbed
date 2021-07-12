# -*- coding: utf-8 -*-
"""

A small script I wrote to see a list of my current steam games and their associated titles
It allows me to randomly choose a game to play
"""

import pandas




def getMyGamesAsDataFrame (path="myGameList.json"):
    myGames=pandas.read_json(path)
    games = myGames['response']['games']
    
    #the list of informationa about games is stored in an array format
    myGamesList=[]
    for game in games:
        gameAsDict = dict(game)
        myGamesList.append(gameAsDict)
    df_myGamesList=pandas.DataFrame(myGamesList)
    return df_myGamesList

DESTINATIONPATH="combinedGameData.json"

df_myGames=getMyGamesAsDataFrame()


def selectGameAtRandom (df):
    return df.sample()

randomGame = selectGameAtRandom(df_myGames)
print ("The game you are going to play is ", list(randomGame['name'])[0])




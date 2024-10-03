import pickle

data = {
    'streak' : 0,
    'totalPlayed' : 0,
    'totalWon' : 0,
    'highestScore' : 0,
    'winRate' : 0
    }

with open("D:\PythonProjects\RandomNumberGuessGame\data.pickle", 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

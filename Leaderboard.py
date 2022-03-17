import pickle

with open('TeamUserName.pkl', 'rb') as SavName:
    savedname = pickle.load(SavName)
    print(savedname)

with open('Snake_Score.pkl', 'rb') as Snake_Scr:
    snake_score = pickle.load(Snake_Scr)
    print(snake_score)
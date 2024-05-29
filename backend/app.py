import pickle

with open('data/processed_games.pkl', 'rb') as f:
    processed_games_df = pickle.load(f)

print(processed_games_df.head())

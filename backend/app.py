import pickle

from backend.models.tfidf_model import TFIDFModel

with open('data/processed_games.pkl', 'rb') as f:
    processed_games_df = pickle.load(f)

model = TFIDFModel()
model.train(processed_games_df['game_content'].tolist())

title = "Baldur's Gate 3"
game_content = processed_games_df.loc[processed_games_df['Title'] == title, 'game_content'].iloc[0]
similar_games = model.find_similar_games(game_content, processed_games_df)

for game in similar_games:
    print(game)

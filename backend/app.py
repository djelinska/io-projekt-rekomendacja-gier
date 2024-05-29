import pickle

from flask import Flask, jsonify, request
from backend.models.tfidf_model import TFIDFModel

app = Flask(__name__)

with open('data/processed_games.pkl', 'rb') as f:
    processed_games_df = pickle.load(f)

model = TFIDFModel()
model.train(processed_games_df['game_content'].tolist())


@app.route('/api/games', methods=['GET'])
def get_games():
    games = processed_games_df[['Title', 'Link', 'Game Description', 'Popular Tags']].to_dict(orient='records')
    return jsonify(games), 200


@app.route('/api/recommend', methods=['GET'])
def recommend():
    query_title = request.args.get('title')
    if not query_title:
        return jsonify({'error': 'Missing title parameter'}), 400

    try:
        game_content = processed_games_df.loc[processed_games_df['Title'] == query_title, 'game_content'].iloc[0]
    except IndexError:
        return jsonify({'error': 'Game title not found'}), 404

    similar_games = model.find_similar_games(game_content, processed_games_df)
    return jsonify(similar_games), 200


if __name__ == '__main__':
    app.run(debug=True)

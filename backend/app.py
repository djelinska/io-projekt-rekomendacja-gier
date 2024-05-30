import pickle

from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.models.tfidf_model import TFIDFModel

app = Flask(__name__)
CORS(app)

with open('data/processed_games.pkl', 'rb') as f:
    processed_games_df = pickle.load(f)

model = TFIDFModel()
model.train(processed_games_df['game_content'].tolist())


@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    results = processed_games_df[processed_games_df['title'].str.contains(query, case=False, na=False)]
    results_sorted = results.sort_values(by='title')
    results_list = results_sorted['title'].tolist()

    return jsonify(results_list)


@app.route('/api/recommend', methods=['GET'])
def recommend():
    query_title = request.args.get('title')
    if not query_title:
        return jsonify({'error': 'Missing title parameter'}), 400

    try:
        game_content = processed_games_df.loc[processed_games_df['title'] == query_title, 'game_content'].iloc[0]
    except IndexError:
        return jsonify({'error': 'Game title not found'}), 404

    similar_games = model.find_similar_games(game_content, processed_games_df)
    return jsonify(similar_games), 200


if __name__ == '__main__':
    app.run(debug=True)

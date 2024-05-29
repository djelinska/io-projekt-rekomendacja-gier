from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class TFIDFModel:
    def __init__(self):
        self.tfidf_matrix = None
        self.vectorizer = TfidfVectorizer()

    def train(self, corpus):
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)

    def find_similar_games(self, query, data, n=11):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = linear_kernel(query_vector, self.tfidf_matrix).flatten()
        related_indices = cosine_similarities.argsort()[:-n-1:-1]

        similar_games = data.iloc[related_indices][['title', 'link', 'description', 'popular_tags']].to_dict(orient='records')
        return similar_games

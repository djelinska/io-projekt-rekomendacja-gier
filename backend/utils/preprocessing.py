import pickle
import re

import nltk
import pandas as pd
from nltk import word_tokenize, WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('wordnet')


def load_data(data_filename):
    data = pd.read_csv(data_filename, low_memory=False)

    return data


def process_text(game_content):
    game_content = game_content.lower()
    game_content = re.sub(r'[^a-zA-Z\s]', '', game_content)

    tokens = word_tokenize(game_content)

    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    preprocessed_game_content = ' '.join(tokens)

    return preprocessed_game_content


def process_tags(tags):
    if isinstance(tags, str):
        tags = eval(tags)
    if isinstance(tags, list):
        return ' '.join(tags)
    return ''


def preprocess_data(games_df):
    print(games_df.shape)
    print(games_df.info())

    print('Liczba pustych kolumn z opisem gry:', games_df['Game Description'].isna().sum())
    print('Liczba pustych list z popularnymi tagami:', games_df['Popular Tags'].isnull().sum())

    games_df.fillna('', inplace=True)
    games_df['processed_popular_tags'] = games_df['Popular Tags'].apply(process_tags)
    games_df['game_content'] = games_df['Game Description'] + ' ' + games_df['processed_popular_tags']
    games_df['game_content'] = games_df['game_content'].apply(process_text)

    new_column_names = {
        'Title': 'title',
        'Link': 'link',
        'Game Description': 'description',
        'Popular Tags': 'popular_tags',
    }
    games_df.rename(columns=new_column_names, inplace=True)

    with open('../data/processed_games.pkl', 'wb') as f:
        pickle.dump(games_df, f)


games_df = load_data('../data/games.csv')
preprocess_data(games_df)

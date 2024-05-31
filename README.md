# Aplikacja Rekomendacji Gier

Ten projekt to system rekomendacji gier, oparty na analizie tekstu i algorytmach rekomendacji, takich jak TF-IDF i podobieństwo cosinusowe. Wykorzystuje on bazę danych zawierającą ponad 70,000 gier dostępnych na platformie Steam.

Aplikacja przeprowadza przetwarzanie opisów gier oraz popularnych tagów, obejmujące tokenizację, usuwanie stop-słów, lematyzację i stemming. Dzięki temu użytkownicy mogą łatwo przeglądać dostępne gry oraz otrzymywać rekomendacje podobnych tytułów.

## Funkcje

- **Wyszukiwanie gier**: Użytkownicy mogą wyszukiwać gry, wpisując tytuł lub fragment tytułu.

- **Rekomendacje gier**: Użytkownicy otrzymują 10 podobnych rekomendowanych gier na podstawie wybranego tytułu.

- **Przetwarzanie wstępne**: Opisy gier i tagi są tokenizowane, usuwane są stop-słowa, a także przeprowadzana jest lematyzacja i stemming.

- **Optymalizacja wydajności**: Przetworzone dane gier są zapisywane do pliku pickle, aby skrócić czas rekomendacji.

## Instalacja i konfiguracja

### Konfiguracja backendu

1. Sklonuj repozytorium:

   ```sh
   git clone https://github.com/djelinska/io-projekt-rekomendacja-gier.git
   ```

2. Przejdź do folderu backend:

   ```sh
   cd io-projekt-rekomendacja-gier\backend
   ```

3. Zainstaluj wymagane biblioteki Pythona:

   ```sh
   pip install -r requirements.txt
   ```

4. Uruchom API Flask:

   ```sh
   flask run
   ```

### Konfiguracja frontendu

1. Przejdź do folderu frontend:

   ```sh
   cd io-projekt-rekomendacja-gier\frontend
   ```

2. Zainstaluj wymagane pakiety NPM:

   ```sh
   npm install
   ```

3. Uruchom serwer deweloperski dla aplikacji frontendowej:

   ```sh
   npm run dev
   ```

## Użycie

Otwórz przeglądarkę i przejdź do http://localhost:3000.
Użyj paska wyszukiwania, aby znaleźć gry, wpisując słowa kluczowe. Wybierz tytuł gry z wyników wyszukiwania.
Zobacz rekomendowane gry wyświetlone na stronie.

## Technologie

- **Backend**: Python, Flask

- **Frontend**: Vite + React

## Źródła

- [31.05.2024] Zbiór danych Steam Games Dataset na Kaggle [link](https://www.kaggle.com/datasets/nikatomashvili/steam-games-dataset)

- [31.05.2024] Przykład implementacji systemu rekomendacji opartego na treści [link](https://github.com/krishnaik06/Recommendation_complete_tutorial/blob/master/Content%20Based%20Recommendation%20Engines%20using%20Python.ipynb)

- [31.05.2024] System rekomendacji oparty na treści krok po kroku [link](https://medium.com/@prateekgaurav/step-by-step-content-based-recommendation-system-823bbfd0541c)

- [31.05.2024] Poradnik dotyczący stworzenia aplikacji z systemem rekomendacji muzyki [link](https://youtu.be/jm9JamrbSv8?si=xG78ZlaffSpXvL5R)

- [31.05.2024] ChatGPT [link](https://chatgpt.com)

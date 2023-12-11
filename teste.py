import json
import requests



def getMovieDetails(titulo):

    api_key = '737233b'
    base_url = 'http://www.omdbapi.com/'

    params = {'apikey': api_key, 't': titulo}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        dados_filme = response.json()
        if dados_filme['Response'] == 'True':
            return {
                'Título': dados_filme['Title'],
                'Ano': dados_filme['Year'],
                'Classificação': dados_filme['Rated'],
                'IMDb Rating': dados_filme['imdbRating']
            }
        else:
            print(f"Filme não encontrado: {dados_filme['Error']}")
            return None
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None
    
movies = []

for filmTitle in ["Blade Runner", "The Little Mermaid", "Fast & Furious: 8", "Guardians of the Galaxy Vol. 3"]:
    movieDetails = getMovieDetails(filmTitle)
    if movieDetails:
        movies.append(movieDetails)

for movie in movies:
    print(f"Título: {movie['Título']}")
    print(f"Ano: {movie['Ano']}")
    print(f"Classificação: {movie['Classificação']}")
    print(f"IMDb Rating: {movie['IMDb Rating']}")
    print("-----")
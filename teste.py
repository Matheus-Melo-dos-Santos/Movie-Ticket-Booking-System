import json
import requests



def getMovieDetails(titulo, genero):

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
                'Gênero': genero,  # Adicionando o gênero como um novo campo
                'Classificação': dados_filme['Rated'],
                'IMDb Rating': dados_filme['imdbRating']
            }
        else:
            print(f"Filme não encontrado: {dados_filme['Error']}")
            return None
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

def listar_filmes_por_genero(genero):
    filmes_por_genero = []

    # Exemplo de uso
    for titulo_do_filme in ["Blade Runner", "The Little Mermaid", "Fast & Furious: 8", "Guardians of the Galaxy Vol. 3"]:
        detalhes_filme = getMovieDetails(titulo_do_filme, genero)
        if detalhes_filme:
            filmes_por_genero.append(detalhes_filme)

    return filmes_por_genero

# Lista para armazenar os dados dos filmes de diferentes gêneros
filmes_romance = listar_filmes_por_genero("Romance")
filmes_acao = listar_filmes_por_genero("Ação")
filmes_aventura = listar_filmes_por_genero("Aventura")

# Unir todas as listas em uma única lista
todos_filmes = filmes_romance + filmes_acao + filmes_aventura

# Salvar os dados em um arquivo JSON
with open('todos_filmes.json', 'w', encoding='utf-8') as json_file:
    json.dump(todos_filmes, json_file, ensure_ascii=False, indent=4)

# Ler os dados do arquivo JSON e exibir detalhes dos filmes
with open('todos_filmes.json', 'r', encoding='utf-8') as json_file:
    dados_salvos = json.load(json_file)

for filme in dados_salvos:
    print(f"Título: {filme['Título']}")
    print(f"Ano: {filme['Ano']}")
    print(f"Gênero: {filme['Gênero']}")
    print(f"Classificação: {filme['Classificação']}")
    print(f"IMDb Rating: {filme['IMDb Rating']}")
    print("-----")
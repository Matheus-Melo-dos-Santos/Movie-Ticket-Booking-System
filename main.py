import json
import requests

class Profile():
    
    def __init__ (self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    
    def toDictionary(self):
        return{

            "name": self.name,
            "email": self.email,
            "password": self.password

        }
        
    def changePassword(self):
        
        newPassword = input('Digite sua nova senha: ')
        self.password = newPassword
 
    
    def changeName(self):
        
        newName = input('digite o novo nome: ')
        self.name = newName
    
    def changeEmail(self):

        newEmail = input('digite seu email: ')
        self.email = newEmail

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

def showListOfMovies():
    
    movies = []

    for movieTitle in ["Blade Runner", "The Little Mermaid", "Fast & Furious: 8", "Guardians of the Galaxy Vol. 3"]:
        movieDetails = getMovieDetails(movieTitle)
        if movieDetails:
            movies.append(movieDetails)

    for movie in movies:
        print(f"Título: {movie['Título']}")
        print(f"Ano: {movie['Ano']}")
        print(f"Classificação: {movie['Classificação']}")
        print(f"IMDb Rating: {movie['IMDb Rating']}")
        print("-----")

def showNameOfMovies():

    movies = []

    for movieTitle in ["Blade Runner", "The Little Mermaid", "Fast & Furious: 8", "Guardians of the Galaxy Vol. 3"]:
        movieDetails = getMovieDetails(movieTitle)
        if movieDetails:
            movies.append(movieDetails)

    return movies

while True:

    Users = []
    with open ("profiles.json", "r") as file:
        Users = json.load(file)

    print(f"""
    |....................................       |
    |                                           |  
    |    1. Mostrar lista de filmes;            |
    |    2. Seleção e Reserva de Assentos;      |
    |    3. funcionalidade 3;                   |
    |    4. Contas de Usuários;                 |
    |    5. funcionalidade 5;                   |
    |    6. funcionalidade 6;                   |
    |    7. funcionalidade 7;                   |
    |    8. funcionalidade 8;                   |
    |    9. Críticas e Avaliações de Clientes;  |
    |    10. funcionalidade 10;                 |
    |    0. Sair                                |
    |                                           |
    |....................................       |
        """)

    action = int(input('funcionalidade: '))

    if action == 1:
        showListOfMovies()

    if action == 4:
        
        print("""
        |.....................|
        |                     |
        | 1. criar usuario    |
        | 2. editar usuario   |
        |                     |
        |.....................|
              """)

        choose = int(input(': '))

        if choose == 1:

            name = input("digite o nome do seu usuario: ")
            email = input("digite seu email: ")
            password = input("digite sua senha: ")

            newUser = Profile(name, password, email)

            Users.append(newUser.toDictionary())

            with open("profiles.json", 'w') as file:
                json.dump(Users, file)
            
            print(f"Usuário {newUser.name} criado com sucesso!")

        if choose == 2:
            
            name = input("digite o nome do seu usuario: ")
            password = input("digite sua senha: ")

            for i in range(0, len(Users)):
                if Users[i]["name"] == name and Users[i]["password"] == password:

                    editUser = Profile(Users[i]["name"], Users[i]["password"], Users[i]["email"])

                    editUser.changeName()
                    editUser.changePassword()
                    editUser.changeEmail()

                    Users[i] = editUser.toDictionary()

                    with open ("profiles.json", 'w') as file:
                        json.dump(Users, file)

        
    
    if action == 9:
        movies = showNameOfMovies()
        for movie in movies:
            print(f"{movie['Título']}")
        
        print('...adicionar comentario em construcao ...')
        


    if action == 0:
        break
    

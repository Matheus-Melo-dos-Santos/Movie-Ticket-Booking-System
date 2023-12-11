import json
import requests

class Profile():
    
    def __init__ (self, name, password):
        self.name = name
        self.password = password
        
    def changePassword(self):
        
        enableChange = input('Digite sua senha: ')
        
        if enableChange == self.password:
            
            newPassword = input('Digite sua nova senha: ')
            self.password = newPassword
            print('Senha atualizada com sucesso!')
            
        else:
            print('senha invalida, tente novamente.')
    
    def changeName(self):
        
        enableChange = input('Digite sua senha: ')
        
        if enableChange == self.password:
            
            newName = input('digite o novo nome: ')
            self.name = newName
            
        else:
            
            print('senha invalida')


while True:

    print(f"""
    |...................................|
    |                                   |  
    |    1. funcionalidade 1;           |
    |    2. funcionalidade 2;           |
    |    3. funcionalidade 3;           |
    |    4. Criar e gerenciar perfil;   |
    |    5. funcionalidade 5;           |
    |    6. funcionalidade 6;           |
    |    7. funcionalidade 7;           |
    |    8. funcionalidade 8;           |
    |    9. funcionalidade 9;           |
    |    10. funcionalidade 10;         |
    |    0. Sair                        |
    |                                   |
    |...................................|
        """)

    action = int(input('funcionalidade: '))

    if action == 4:
        
        print("""
              
        | ------------------- |    
        | 1. criar usuario    |
        | 2. editar usuario   |
        | ------------------- |
              
              """)

        choose = int(input(': '))

        if choose == 1:

            name = input("digite o nome do seu usuario: ")
            password = input("digite sua senha: ")

            newUser = Profile(name, password)

            print(f"Usuário {newUser.name} criado com sucesso!")

        if choose == 2:
            print('...em construcao...')
            
    if action == 0:
        break
    

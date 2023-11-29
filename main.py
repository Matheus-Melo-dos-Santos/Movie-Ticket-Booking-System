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
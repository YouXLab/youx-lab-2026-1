  #Declaraçao de classes
class Funcionario:
    def __init__(self, nome = '', setor = '', cargo = '' ): #metodo construtor
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def Apresentacao(self):
        return f"Ola sou o {self.nome} do setor de {self.setor} da empresa {self.cargo} "

#Declaraçao de objetos
funcionario1 = Funcionario('Joao', 'Administraçao', 'Curso em video')
print(funcionario1.Apresentacao())


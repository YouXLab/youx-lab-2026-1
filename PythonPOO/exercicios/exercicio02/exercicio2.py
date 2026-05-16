#Declaraçao de classes
class Teste:
    def __init__(self, nomw = '', idade = 0): #metodo construtor
        self.nome = input('')
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"O {self.nome} tem {self.idade} anos"

#Declaraçao de objetos
g1 = Teste('Joao', 17)
g1.aniversario()
print(f"{g1.mensagem()}")
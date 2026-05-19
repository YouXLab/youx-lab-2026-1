class funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentar(self):
        print(f'Olá! sou {self.nome} e sou {self.cargo} do setor {self.setor} do YouX-Lab!')

c1 = funcionario('Artur', 'BackEnd', 'Desenvolvedor')
print(c1.apresentar())
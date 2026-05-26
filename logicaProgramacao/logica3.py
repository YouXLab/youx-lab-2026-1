
dados = {}
usuarios = [{'nome': 'joao', 'email': 'joaobi2182009', 'senha': '21082009'}]
opcao = 0
print("SEJA BEM VINDO")
while opcao != '3':
    opcao = input("[1] LOGIN \n [2] CADASTRO \n [3] EXIT \n ")
    # SITEMAS DE CADASTRO
    if opcao =='2':
        dados['nome'] = input("Crie seu nome de usuario: ")
        dados['email'] = input("Cadastre seu email: ")
        senha = input("Crie sua senha: ")
        while len(senha)<8:
            print("A senha deve conter no minimo 8 caracteres")
            senha = input("Crie sua senha")
        validador_senha = input("Digite a senha novamente: ")
        while validador_senha != senha:
            print("As senhas precisam ser identicas!")
            validador_senha = input("Digite a senha novamente: ")
        dados['senha'] = senha
        usuarios.append(dados.copy())
        dados.clear()
    print(usuarios)
    if opcao =='1':
        #SISTEMA DE LOGIN
        print("BEM VINDO DE VOLTA")
        validador_email = input("Digite o seu email: ")
        for indice, pessoas in enumerate(usuarios):
            while not validador_email in usuarios[indice]['email']:
                print(usuarios[indice]['email'])
                print("Email incorreto")
                validador_email = input("Digite o seu email")
            validador_senha = input("Digite a sua senha")
            if not validador_senha in usuarios[indice]['senha']:
                print("Senha incorreta(Voce possui mais 3 tentativas)")
                for tentativas in range(1,3+1):
                    validador_senha = input(f"Digite sua senha:({tentativas} restantes)")
                print("Tente novamente daqui a alguns minutos")
print(f"Ola {usuarios['nome']}")









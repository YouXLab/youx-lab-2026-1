const btnBotaoCadastrar = document.getElementById("botaoCadastrar")
const corpoTabela = document.getElementById("corpoTabela")

btnBotaoCadastrar.addEventListener("click", (evt) => {
    evt.preventDefault() 
    const nomeInput = document.getElementById("inputNome")
    const tipoInput = document.getElementById("inputTipo")
    const cadastroInput = document.getElementById("inputDataCadastro")
    const terminoInput = document.getElementById("dataParaTermino")
    const statusInput = document.getElementById("inputStatus")
     
    const novaLinha = document.createElement('tr')
    
    const celulaNomeTarefa = document.createElement('td')
    celulaNomeTarefa.innerText = nomeInput.value
    
    novaLinha.appendChild(celulaNomeTarefa)

    const celulaTipo = document.createElement('td')
    celulaTipo.innerText = tipoInput.value
    novaLinha.appendChild(celulaTipo)

    const celulaCadastro = document.createElement('td')
    celulaCadastro.innerText = cadastroInput.value
    novaLinha.appendChild(celulaCadastro)

    const celulaTermino = document.createElement('td')
    celulaTermino.innerText = terminoInput.value
    novaLinha.appendChild(celulaTermino)

    const celulaStatus = document.createElement('td')
    const textoStatus = document.createElement('p')
    textoStatus.innerText = statusInput.value

    if (statusInput.value== "Em andamento"){
        textoStatus.classList.add('texto-status-em_andamento')
    } else if (statusInput.value == "Não iniciado"){
         textoStatus.classList.add('texto-status-nao_iniciado')
    } else if(statusInput.value == "Finalizado"){
         textoStatus.classList.add('texto-status-finalizado')
    }
    celulaStatus.appendChild(textoStatus)

    novaLinha.appendChild(celulaStatus)

    const celulaPrazo = document.createElement('td')
    const textoPrazo = document.createElement('p')
    textoPrazo.classList.add('texto-prazo')

    const dataAtual = new Date()
    const dataParaTermino = new Date(terminoInput.value)

    if (dataAtual < dataParaTermino){
        textoPrazo.innerText = "Em dia"
        textoPrazo.classList.add('emdia')
    } else {
        textoPrazo.innerText = "Atrasado"
        textoPrazo.classList.add('atrasado')
    }

    celulaPrazo.appendChild(textoPrazo)
    novaLinha.appendChild(celulaPrazo)



    const botoesAcoes = document.createElement('td')
    botoesAcoes.classList.add("container-acoes")

    const botaoEditar = document.createElement("button")
    botaoEditar.textContent = "Editar"
    botaoEditar.classList.add('botaoEditar')

    botaoEditar.addEventListener('click', (ev) => {
        
        nomeInput.value= celulaNomeTarefa.innerText
        tipoInput.valu= celulaTipo.innerText
        cadastroInput.value= celulaCadastro.innerText
        terminoInput.value= celulaTermino.innerText
        statusInput.value= celulaStatus.innerText
        novaLinha.remove()
    })

    botoesAcoes.appendChild(botaoEditar)

    const botaoDeletar = document.createElement("button")
    botaoDeletar.textContent = "Deletar"
    botaoDeletar.classList.add('botaoDeletar')

    botaoDeletar.addEventListener('click', (ev) => {
        novaLinha.remove()
    })

    botoesAcoes.appendChild(botaoDeletar)

    novaLinha.appendChild(botoesAcoes)
    corpoTabela.appendChild(novaLinha)
})
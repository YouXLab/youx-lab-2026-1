const form = document.getElementById("formTarefa");
const nome = document.getElementById("nomeTarefa");
const tipo = document.getElementById("tipoTarefa");
const cadastro = document.getElementById("dataCadastro");
const termino = document.getElementById("dataTermino");
const status = document.getElementById("statusTarefa");
const lista = document.getElementById("listaTarefas");
const botaoCadastrar = document.getElementById("botaoCadastrar");
let linhaEditando = null;

form.addEventListener("submit", function(event) {
    event.preventDefault();/*importante*/
    let prazo = verificarPrazo(termino.value);/*em dia ou n*/

    if (linhaEditando == null) {
        criarTarefa(prazo);
    } else {
        atualizarTarefa(prazo);
    }

    limparFormulario();
});

function criarTarefa(prazo) {

    let linha = document.createElement("tr");

    let colunaNome = document.createElement("td");
    let colunaTipo = document.createElement("td");
    let colunaTermino = document.createElement("td");
    let colunaStatus = document.createElement("td");
    let colunaPrazo = document.createElement("td");
    let colunaAcoes = document.createElement("td");

    colunaNome.textContent = nome.value;
    colunaTipo.textContent = tipo.value;
    colunaTermino.textContent = formatarData(termino.value);
    colunaStatus.textContent = status.value;
    colunaPrazo.textContent = prazo;

    linha.dataset.cadastro = cadastro.value;
    linha.dataset.termino = termino.value;
    /*BOTOES*/
    let botaoEditar = document.createElement("button");
    botaoEditar.textContent = "Editar";
    botaoEditar.type = "button";
    botaoEditar.className = "botao-editar";

    let botaoDeletar = document.createElement("button");
    botaoDeletar.textContent = "Deletar";
    botaoDeletar.type = "button";
    botaoDeletar.className = "botao-deletar";
    /*BOTOES*/
    botaoEditar.addEventListener("click", function() {
        editarTarefa(linha);
    });

    botaoDeletar.addEventListener("click", function() {
        deletarTarefa(linha);
    });

    colunaAcoes.appendChild(botaoEditar);
    colunaAcoes.appendChild(botaoDeletar);

    linha.appendChild(colunaNome);
    linha.appendChild(colunaTipo);
    linha.appendChild(colunaTermino);
    linha.appendChild(colunaStatus);
    linha.appendChild(colunaPrazo);
    linha.appendChild(colunaAcoes);

    lista.appendChild(linha);
}

function editarTarefa(linha) {

    nome.value = linha.children[1].textContent;
    tipo.value = linha.children[2].textContent;
    cadastro.value = linha.dataset.cadastro;
    termino.value = linha.dataset.termino;
    status.value = linha.children[3].textContent;

    linhaEditando = linha;

    botaoCadastrar.textContent = "Salvar Alterações";
}

function atualizarTarefa(prazo) {

    linhaEditando.children[0].textContent = nome.value;
    linhaEditando.children[1].textContent = tipo.value;
    linhaEditando.children[2].textContent = formatarData(termino.value);
    linhaEditando.children[3].textContent = status.value;
    linhaEditando.children[4].textContent = prazo;

    linhaEditando.dataset.cadastro = cadastro.value;
    linhaEditando.dataset.termino = termino.value;

    linhaEditando = null;

    botaoCadastrar.textContent = "+ Cadastrar Tarefa";
}

function deletarTarefa(linha) {
    linha.remove();
}

function verificarPrazo(data) {

    let hoje = new Date();
    let dataTermino = new Date(data);

    if (dataTermino < hoje) {
        return "ATRASADO";
    } else {
        return "EM DIA";
    }
}

function formatarData(data) {

    let partes = data.split("-");

    return partes[2] + "/" + partes[1] + "/" + partes[0];
}

function limparFormulario() {
    form.reset();
}
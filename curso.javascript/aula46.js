const caixaCursos = document.querySelector("#caixaCursos")
const btn_c = [...document.querySelectorAll(".curso")]
const c1_2 = document.querySelector("#c1_2")
const cursos = ["HTML", "CSS", "Javascript", "PHP", "React", "MySQL", "ReactNative"]
const btnCursoSelecionado = document.getElementById("btnCursoSelecionado")
const btnRemoveCurso = document.getElementById("btnRemoveCurso")
const btnAdicionarNovoCursoAntes = document.getElementById("btnAdicionarNovoCursoAntes")
const btnAdicionarNovoCursoDepois = document.getElementById("btnAdicionarNovoCursoDepois")
const nomeCurso = document.getElementById("nomeCurso")

let indice = 0

const tirarSelecao = () => {
    const cursoSelecionado = [...document.querySelectorAll(".selecionado")]
    cursoSelecionado.map((el) => {
        el.classList.remove("Selecionado")
    })
}

const criarNovoCurso = (curso) => {
    const novoElemento = document.createElement("div")
    novoElemento.setAttribute("id", "c" + indice)
    novoElemento.setAttribute("class", "curso c1")
    novoElemento.innerHTML = curso
    novoElemento.addEventListener("click", (evt) => {
        tirarSelecao()
        evt.target.classList.toggle("selecionado")
    })
    return novoElemento
}


cursos.map((el, chave) => {
    const novoElemento = criarNovoCurso(el)
    caixaCursos.appendChild(novoElemento)
    indice++
})

const cursoSelecionado = () => {
    const todosRadios = [...document.querySelectorAll("input[type=radio")]
    return cursoSelecionado[0]
}

btnCursoSelecionado.addEventListener("click", (evt) => {
    try {
        const cursoSelecionado = rs.parentNode.previouSibling.textContent
        alert("Curso selecionado: " + cursoSelecionado().innerHTML)
    } catch (ex) {
        alert("Selecione um curso")
    }
})

btnRemoveCurso.addEventListener("click", (evt) => {
    const rs = radioSelecionado()
    if (rs != undefined) {
        const cursoSelecionado = rs.parentNode.parentNode
        cursoSelecionado.remove()
    } else {
        alert("Selecione um curso")
    }
})
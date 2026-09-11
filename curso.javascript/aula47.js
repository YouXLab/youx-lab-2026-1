const p_array = document.querySelector("#array")
const txt_pesquisar = document.querySelector("#txt_pesquisar")
const btnPesquisar = document.querySelector("#btnPesquisar")
const resultado = document.querySelector("#resultado")


const elemento_array=["html","css","javascript"]
p_array.innerHTML="["+elemento_array+"]"


btnPesquisar.addEventListener("click",(evt)=>{
    resultado.innerHTML="Valor nao encontrado"
    const ret=elemento_array.find((e,i)=>{
        if(e.toUpperCase()===txt_pesquisar.value.toUpperCase()){
            resultado.innerHTML="Valor encontrado " + e + " na posiçao" + i
            return e
        } 
    })
    console.log(ret)
})



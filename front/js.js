
async function puxar_api() {
    await axios.get("http://127.0.0.1:8000/api/v1/transformer").then((response) =>{
        const personagens = response.data
        const container = document.getElementById("transformers-container")
        personagens.forEach(element =>{
            const personagemDiv = document.createElement("div")
            personagemDiv.classList.add("element")
            personagemDiv.innerHTML = `
            <h2>Nome: ${element.name}</h2>
            <p>Time: ${element.team}</p>
            <p>Color: ${element.color}</p>
            `
            container.append(personagemDiv)
        })
    })
}
(async () => {
    await puxar_api()
})()


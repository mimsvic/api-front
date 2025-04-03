// async function puxando_api(){
//     const response = await fetch("http://127.0.0.1:8000/api/v1/personagem");
//     const data = await response.json(); 0
//     return data;
// }

// async function mostrar_personagens(){
//     const personagens = await puxando_api();
//     const container = document.getElementById("transformers-container");

//     personagens.forEach(personagem => {
//         const personagemDiv = document.createElement("div");
//         personagemDiv.classList.add("Personagem");

//         personagemDiv.innerHTML = ` 
//             <h2>${personagem.nome}</h2>
//             <img src="${personagem.foto}"/>
//             <p>${personagem.time}</p>
//         `;
//         container.appendChild(personagemDiv);
//     });
// }

// mostrar_personagem()


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


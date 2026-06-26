console.log("registro.js carregado");

const form = document.getElementById("formRegistro");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = new FormData(form);

    const resposta = await fetch("/registro", {
        method: "POST",
        body: dados
    });

    console.log(await resposta.text());
});
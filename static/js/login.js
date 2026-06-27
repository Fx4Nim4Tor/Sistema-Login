const form = document.getElementById("formLogin");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const dados = new FormData(form);

    const resposta = await fetch("/login", {
        method: "POST",
        body: dados
    });

    console.log(await resposta.text());
});
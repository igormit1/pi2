// script.js

document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Captura os valores dos campos do formulário
    const fullName = document.getElementById('full-name').value;
    const usuario = document.getElementById('username').value;
    const cpf = document.getElementById('cpf').value;
    const email = document.getElementById('email').value;
    const address = document.getElementById('address').value;
    const occupation = document.getElementById('occupation').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    // Verifica se as senhas coincidem
    if (password !== confirmPassword) {
        alert("As senhas não coincidem!");
        return;
    }

    // Cria um objeto para armazenar os dados
    const userData = {
        fullName,
        usuario,
        cpf,
        email,
        address,
        occupation,
        password
    };

    // Envia os dados para o servidor Python
    fetch('http://localhost:5000/index', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Cadastro realizado com sucesso!");
            document.getElementById('registration-form').reset(); // Limpa o formulário
        } else {
            alert("Erro ao cadastrar. Tente novamente.");
        }
    })
    .catch((error) => {
        console.error('Erro:', error);
        alert("Erro ao conectar com o servidor.");
    });
});

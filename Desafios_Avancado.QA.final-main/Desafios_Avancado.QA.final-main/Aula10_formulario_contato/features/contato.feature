# language: pt
Funcionalidade: Acessar o formulario de contato e preencher com os dados

  Cenário: Usuário acessar o formulario de contato com sucesso e preenche com seus dados
    Dado que o site do formulario esta acessivel
    Quando eu preencho o formulario com nome, email e telefone validos
    Então clico para enviar o formulario

# language: pt
Funcionalidade: Automação de Envio de Mensagem no WhatsApp Web
  Como um aluno do IJJ
  Eu quero enviar uma mensagem automática para meu grupo de estudos
  Para completar o desafio de automação

  Cenário: Enviar mensagem para o grupo de estudos
    Dado que o WhatsApp Web está logado no navegador Edge
    Quando eu enviar uma mensagem para o grupo "[QA IBTECH | AGO/25]"
    Então a mensagem "Automação do WhatsApp - NOME DO SEU SQUAD" deve ser enviada com sucesso
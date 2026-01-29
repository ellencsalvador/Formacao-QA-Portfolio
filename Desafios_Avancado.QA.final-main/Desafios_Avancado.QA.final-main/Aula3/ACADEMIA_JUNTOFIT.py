def verificar_acesso(dias_consecutivos, veio_dia_anterior):
    """
    Esta função representa a lógica da catraca.
    Ela decide qual mensagem mostrar com base na frequência do aluno.
    """

    if not veio_dia_anterior:
        print("\nQUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
        dias_consecutivos = 1

    elif dias_consecutivos == 21:
        print("\nUHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ.")
        dias_consecutivos = 0

    else:
        print("\nVOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO.")

    return dias_consecutivos

print("--- BEM-VINDO AO SIMULADOR DA CATRACA JUNTOFIT ---")

contagem_atual_aluno = int(input("Digite quantos dias você está vindo a academia? Sem mentiras: "))

while True:
    print(f"\nSituação atual do aluno: {contagem_atual_aluno} dias consecutivos.")
    print("-----------------------------------------------------")
    print("Escolha o cenário para simular a passagem na catraca:")
    print("1 - Aluno veio ontem (sequência continua)")
    print("2 - Aluno faltou ontem (sequência quebrou)")
    print("3 - Aluno está completando 21 dias HOJE")
    print("4 - Sair do simulador")
    print("-----------------------------------------------------")
    escolha = input("Digite sua escolha (1, 2, 3 ou 4): ")

    if escolha == '1':
        contagem_atual_aluno += 1 
        verificar_acesso(dias_consecutivos=contagem_atual_aluno, veio_dia_anterior=True)
    
    elif escolha == '2':
        contagem_atual_aluno = verificar_acesso(dias_consecutivos=contagem_atual_aluno, veio_dia_anterior=False)

    elif escolha == '3':
        contagem_atual_aluno = 21
        contagem_atual_aluno = verificar_acesso(dias_consecutivos=contagem_atual_aluno, veio_dia_anterior=True)

    elif escolha == '4':
        print("Simulador encerrado. Agradecemos sua participação!")
        break
        
    else:
        print("Opção inválida. Por favor, tente novamente.")

print("-----------------------------------------------------")

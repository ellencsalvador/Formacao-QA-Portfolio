dominio_correto = "@jogajuntoinstituto.org"

email_usuario = input("Por favor, insira seu e-mail para verificação: ").strip()

if email_usuario.endswith(dominio_correto):
    print("\n[SUCESSO] O e-mail inserido pertence ao domínio do Instituto Joga Junto.")
else:
    print(f"\n[FALHA] O e-mail '{email_usuario}' não é um e-mail válido do Instituto Joga Junto.")
    print(f"Lembre-se, o e-mail deve terminar com '{dominio_correto}'.")

    
def contar_vogais(palavra):
    vogais = "aeiou"
    contador_vogais = 0
    for letra in palavra.lower():
        if letra in vogais:
            contador_vogais = contador_vogais + 1
    return contador_vogais

palavra_usuario = input("Digite uma palavra para contar as vogais: ")

total_de_vogais = contar_vogais(palavra_usuario)

print(f"\nA palavra '{palavra_usuario}' possui {total_de_vogais} vogais.")
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"

consoantes = 0

for letra in palavra:
    if letra not in vogais:
        consoantes += 1

print(f"A palavra {palavra} tem {consoantes} consoante(s).")
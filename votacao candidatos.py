candidatos = {
    1: "Anderson",
    2: "Manoel",
    3: "José",
    4: "Emanoelli",
}

#Contadores
votos_dos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulos = 0
votos_em_brancos = 0
total_votos = 0

print("Digite os votos:")
print("1-4 para candidatos")
print("5 para voto nulo")
print("6 para voto em branco")
print("0 para encerrar\n")

#Entrada dos votos
while True:
    try:
        voto = int(input("Voto: "))
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        continue

    if voto == 0:
        break
    elif voto in votos_dos_candidatos:
        votos_dos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Voto inválido! Digite novamente.")
        continue

    total_votos += 1

#Resultados
print("\n Resultado da eleição:")
for codigo, nome in candidatos.items():
    votos = votos_dos_candidatos[codigo]
    percentual = (votos / total_votos) * 100 if total_votos > 0 else 0
    print(f"{nome}: {votos} votos ({percentual:.2f}%)")

print(f"\nVotos nulos: {votos_nulos} ({(votos_nulos / total_votos * 100 if total_votos > 0 else 0):.2f}%)")
print(f"Votos em branco: {votos_brancos} ({(votos_brancos / total_votos * 100 if total_votos > 0 else 0):.2f}%)")

#Vencedor
maior_votos = max(votos_dos_candidatos.values())
vencedores = [nome for codigo, nome in candidatos.items() if votos_dos_candidatos[codigo] == maior_votos]

if len(vencedores) == 1:
    print(f"\nCandidato vencedor: {vencedores[0]}")
else:
    print(f"\nEmpate entre: {', '.join(vencedores)}")

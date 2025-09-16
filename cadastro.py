nome = input("Digite seu nome: ").strip().capitalize()
try:
    idade = int(input("Digite sua idade: "))
except:
    while True:
        print()
        print("Idade Inválida")
        idade = int (input("Digite sua idade: "))
        if isinstance(idade, int):
            break

dados = {
    "usuario": nome,
    "idade_usuario": idade
}

for us, i in dados.items():
    print(us, i)
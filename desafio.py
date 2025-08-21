CONSTANTE_BONUS = 1000
nome_usuario = input("Digite o seu nome: ")


salario_usuario = float(input(
    "Digite o seu salário: "
))
bonus_usuario = float(input("Digite o seu bonus: "))

valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

print(f"O usuário {nome_usuario} possui o bonus {valor_bonus}")
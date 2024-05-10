
print("o--------------------------------o")
print("|   Escola a base de conversão   |")
print("|--------------------------------|")
print("|          (1) Binario           |")
print("|          (2) Decimal           |")
print("|          (3) Octal             |")
print("|          (4) Hexadeciaml       |")
print("o--------------------------------o")
opcao = int(input("       Digite sua escolha: ")) 

print("o--------------------------------o")
print("| Escola a base a ser convertida |")
print("|--------------------------------|")
print("|          (1) Binario           |")
print("|          (2) Decimal           |")
print("|          (3) Octal             |")
print("|          (4) Hexadeciaml       |")
print("o--------------------------------o")
opcao2 = int(input("       Digite sua escolha: "))




    #base 1


if opcao and opcao2 ==  1:
    print("As bases são iguais, portante o resultado é o mesmo")


elif opcao == 1 and opcao2 == 2:
    a = int(input("Digite o numero Binario a ser convertido em decimal: "))
    num = []
    b = ''
    cont = 0
    while a < 0:
        a[len(a):] = [a] (a % 2)
        a //= 2
        cont += 1
    for i in range(cont-1,-1,-1):
        b += str(num[i])
    print(f"Seu numero em binario é: {b}")



elif opcao == 1 and opcao2 == 3:
    a = int(input("Digite o numero Binario a ser convertido em octal: "))

    print("teste 3")


elif opcao == 1 and opcao2 == 4:
    a = int(input("Digite o numero Binario a ser convertido em hexadecimal: "))

    print("teste 4")


    #base 2


elif opcao == 2 and opcao2 == 1:
    a = int(input("Digite o numero Decimal a ser convertido em binario: "))

    print("teste 5")


elif opcao == 2 and opcao2 == 2:
    print("As bases são iguais, portante o resultado é o mesmo")


elif opcao == 2 and opcao2 == 3:
    a = int(input("Digite o numero Decimal a ser convertido em octal: "))

    print("teste 6")


elif opcao == 2 and opcao2 == 4:
    a = int(input("Digite o numero Decimal a ser convertido em hexadecimal: "))

    print("teste 6")


    #base 3


elif opcao == 3 and opcao2 == 1:
    a = int(input("Digite o numero Octal a ser convertido em binario: "))

    print("teste 7")


elif opcao == 3 and opcao2 == 2:
    a = int(input("Digite o numero Octal a ser convertido em decimal: "))

    print("teste 8")


elif opcao == 3 and opcao2 == 3:
    print("As bases são iguais, portante o resultado é o mesmo")


elif opcao == 3 and opcao2 == 4:
    a = int(input("Digite o numero Octal a ser convertido em hexadecimal: "))

    print("teste 9")


    #  Base 4


elif opcao == 4 and opcao2 == 1:
    a = int(input("Digite o numero Hexadecimal a ser convertido em binario: "))

    print("teste 10")


elif opcao == 4 and opcao2 == 2:
    a = int(input("Digite o numero Hexadecimal a ser convertido em decimal: "))

    print("teste 11")


elif opcao == 4 and opcao2 == 3:
    a = int(input("Digite o numero Hexadecimal a ser convertido em octal: "))

    print("teste 12")


elif opcao == 4 and opcao2 == 4:
    print("As bases são iguais, portante o resultado é o mesmo")
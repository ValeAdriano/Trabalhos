import matplotlib.pyplot as plt

def primeira_opcao():
    print("Opção 1 selecionada: Função do primeiro grau")
    # Implemente a lógica para a função do primeiro grau aqui

def segunda_opcao():
    print("Opção 2 selecionada: Função do segundo grau")
    # Solicitar os dados necessários (a, b) para a função do segundo grau
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    while True:
        print("\nEscolha uma opção:")
        print("1) Determinar se a função é crescente ou decrescente")
        print("2) Determinar o zero da função")
        print("3) Desafio: Gerar o gráfico da função")
        print("4) Voltar")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            if a > 0:
                print("A função é crescente.")
            elif a < 0:
                print("A função é decrescente.")
            else:
                print("A função é constante.")
        elif opcao == "2":
            if a != 0:
                zero = -b / a
                print("O zero da função é:", zero)
            else:
                print("Não é uma função do segundo grau.")
        elif opcao == "3":
            x = []
            y = []
            for i in range(-10, 11):
                x.append(i)
                y.append(a * i**2 + b * i)
            
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Gráfico da função do segundo grau')
            plt.grid(True)
            plt.show()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

print("Bem-vindo ao programa!")

while True:
    print("\nEscolha uma opção:")
    print("1) Função do primeiro grau")
    print("2) Função do segundo grau")
    print("3) Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        primeira_opcao()
    elif opcao == "2":
        segunda_opcao()
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")

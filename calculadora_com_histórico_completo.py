def menu():
    adicao = []
    subtracao = []
    multiplicacao = []
    divisao = []
    potencia = []
    raiz = []
    
    opcao = None
    
    while opcao != "8":
        print("\n====== MENU PRINCIPAL ======")
        print("1 - Fazer conta de adição (x + x)")
        print("2 - Fazer conta de subtração (x - x)")
        print("3 - Fazer conta de multiplicação (x * x)")
        print("4 - Fazer conta de divisão (x / x)")
        print("5 - Fazer conta de potênciação (x²)")
        print("6 - Fazer conta de raiz (√x) ")
        print("7 - Ver histórico")
        print("8 - Encerrar calculadora")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite um número: "))
            resultado = n1 + n2
            print(f"O resultado da adição é de: {resultado}")
            adicao.append(f"{n1} + {n2} = {resultado}")
            
        elif opcao == "2":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite um número: "))
            resultado = n1 - n2
            print(f"O resultado da subtração é de: {resultado}")
            subtracao.append(f"{n1} - {n2} = {resultado}")
            
        elif opcao == "3":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite um número: "))
            resultado = n1 * n2
            print(f"O resultado da multiplicação é de: {resultado}")
            multiplicacao.append(f"{n1} x {n2} = {resultado}")
            
        elif opcao == "4":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite um número: "))
            if n2 == 0:
                print("Não é possível fazer uma divisão com 0")
            else:
                resultado = n1 / n2
                print(f"O resultado da divisão é de: {resultado}")
                divisao.append(f"{n1} / {n2} = {resultado}")
                
        elif opcao == "5":
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite um número: "))
            resultado = n1 ** n2
            print(f"O resultado da potênciação é de: {resultado}")
            potencia.append(f"{n1} ^ {n2} = {resultado}")
            
        elif opcao == "6":
            n1 = float(input("Digite um número: "))
            if n1 < 0:
                print("Não é possível calcular com número negativo")
            else:
                resultado = n1 ** 0.5
                print(f"O resultado da raiz é de: {resultado:.2f}")
                raiz.append(f"√{n1} = {resultado:.2f}")
                
        elif opcao == "7":
            print("\n=== HISTÓRICO ===")

            print("\nAdição:")
            if adicao:
                for i, op in enumerate(adicao, 1):
                    print(f"{i}) {op}")
            else:
                print("Nenhuma operação realizada")

            print("\nSubtração:")
            if subtracao:
                for i, op in enumerate(subtracao, 1):
                    print(f"{i}) {op}")
            else:
                print("Nenhuma operação realizada")

            print("\nMultiplicação:")
            if multiplicacao:
                for i, op in enumerate(multiplicacao, 1):
                    print(f"{i}) {op}")
            else:
                print("Nenhuma operação realizada")

            print("\nDivisão:")
            if divisao:
                for i, op in enumerate(divisao, 1):
                    print(f"{i}) {op}")
            else:
                print("Nenhuma operação realizada")

            print("\nPotência:")
            if potencia:
                for i, op in enumerate(potencia, 1):
                    print(f"{i}) {op}")
            else:
                print("Nenhuma operação realizada")

            print("\nRaiz:")
            if raiz:
                for i, op in enumerate(raiz, 1):
                    print(f"{i}) {op}")
            else:
                print("Nenhuma operação realizada")
                
        elif opcao == "8":
            print("Encerrando a calculadora...")
            
        else:
            print("Insira as opções de 1 à 6 para fazer contas, 7 para ver o histórico completo e 8 para encerrar o sistema")
menu()
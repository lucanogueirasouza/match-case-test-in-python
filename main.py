import pyfiglet, os, sys, time 

text = pyfiglet.figlet_format("Calculadora", font="doom")

def nome_cal(): 
    global text
    print (text)

def exibir_opcoes(): 
    print (
        "[1] - Adição\n" \
        "[2] - Subtração\n" \
        "[0] - Sair\n"
    )

def limpar_tela(): 
    os.system(
        "Cls"
    )

def congelar(): 
    time.sleep(2)

def fechar_app(): 
    os.system(
        "Cls"
    )
    print (
        "Finalizando app..."
    )
    sys.exit()

def escolher_opcoes(): 
    try: 
        escolha = int(input(
            ">>> "
        ))
        match escolha: 
            case 1:
                numero1 = int(input(
                    "Digite o 1º Número: "
                ))
                numero2 = int(input(
                    "Digite o 2º Número: "
                ))
                print(numero1 + numero2) 
            case 2: 
                numero1 = int(input(
                    "Digite o 1º Número: "
                ))

                numero2 = int(input(
                    "Digite o 2º Número: "
                ))
                print(numero1 - numero2)
            case 0: 
                fechar_app()
            case _: 
                print (
                    "Tente uma opção válida."
                )
    except (ValueError): 
        print (
            "Escolha uma opção válida."
        )

        
def voltar_menuPrincipal(): 
    global main
    main()

def main(): 
    nome_cal()
    exibir_opcoes()
    escolher_opcoes()
    congelar()
    limpar_tela()
    voltar_menuPrincipal()

if __name__ == "__main__": 
    main()




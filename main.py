

from models.cliente import Cliente

def main() -> None:
    menu()

def menu() -> None:
    print('====================================')
    print('==========Bem-Vindo(a)==============')
    print('====================================')
    print('====================================')

    print('Selesione uma opçao')
    print('1 - Cadastrar cliente')
    print('2 - Listar todos clientes cadastrado')
    print('3 - Emitir comprovente')
    print('4 -')
    print('5 -')
    print('6 -')
    
    opcao: int = int(input())
    
    if opcao == 1:
        cliente.cadastrar_cliente()
        menu()
    if opcao == 2:
        cliente.listar_cliente()
        menu()
    if opcao == 3:
        cliente.emitir_comprovante()
        menu()
    else:
        print('Opçao invalida')
    

if __name__ == '__main__':
    cliente = Cliente()
    main()

import sqlite3
import csv
class Cliente:
    
    def __init__(self) -> None:
        self.produto = {}
        
    

    def cadastrar_cliente(self) -> None:
        print('cadastrar cliente')
        print('=================')
        
        nome: str = input('Informe o nome do cliete:')
        numero: int = input('Informe o numero:')
        endereco = input('informe o endereço:')
        banco = sqlite3.connect('cliente_banco.db')
        cursor = banco.cursor()
        
        #cursor.execute('CREATE TABLE pessoas (nome text, numero integer, endereco text)')
        cursor.execute("""
        INSERT INTO pessoas (nome, numero, endereco)
        VALUES (?,?,?)""",(nome, numero, endereco))

        banco.commit()
        
        print('cliente salvo com susseso')
        banco.close

    def listar_cliente(self):
        conn = sqlite3.connect('cliente_banco.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM pessoas')
        resultados = cursor.fetchall()
        cont = 0

        for linha in resultados:
            print(f'id: {cont} Cliente: {linha[0]}')
            cont += 1
        conn.close()

    def emitir_comprovante(self):
        cont = 0
       
        conn = sqlite3.connect('cliente_banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pessoas')
        resultados = cursor.fetchall()
        for linha in resultados:
            print(f'id: {cont} Cliente: {linha[0]}')
            cont += 1
        conn.close()
        id = int(input('infome o id do cliente:'))
        celular = str(input('Informe a marca e modelo do celular:'))
        descricao = str(input('Informe a descriçao:'))
        valor = float(input('Informe o valor R$:'))
        client_comp = resultados[id]
        nome = client_comp[0]
        numero = client_comp[1]
        endereco = client_comp[2]
        
        dados: str = [
        f'''
        _______comprovante______
        Nome: {nome}
        Numero: {numero}
        Endereço: {endereco}
        Modelo do celular: {celular}
        Descriçao: {descricao}
        Valor: {valor}''']
        nome_compro = nome.replace(' ', '_')


        with open(f'comprovantes/{nome_compro}.csv', 'w', newline='') as arq:
            escritor_csv = csv.writer(arq)
            escritor_csv.writerow(dados)

        






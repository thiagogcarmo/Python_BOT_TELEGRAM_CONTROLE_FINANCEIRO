from database import SaldoDB
from plot_utils import gerar_grafico

def main():
    db = SaldoDB()

    try:
        while True:
            print("\n1. Inserir transação")
            print("2. Ver saldo atual")
            print("3. Ver gasto diário permitido")
            print("4. Gerar gráfico")
            print("5. Sair")
            op = input("Escolha uma opção: ")

            if op == '1':
                tipo = input("Tipo (credito/debito): ").strip().lower()
                valor = float(input("Valor: R$ "))
                data = input("Data (YYYY-MM-DD) [deixe em branco para hoje]: ").strip()
                db.inserir_transacao(tipo, valor, data if data else None)

            elif op == '2':
                print(f"Saldo atual: R$ {db.calcular_saldo_atual():.2f}")

            elif op == '3':
                print(f"Gasto diário permitido: R$ {db.gasto_diario_permitido():.2f}")

            elif op == '4':
                transacoes = db.get_transacoes_ordenadas()
                saldo_inicial = db.get_saldo_inicial()
                gerar_grafico(transacoes, saldo_inicial)

            elif op == '5':
                print("Encerrando...")
                break

            else:
                print("Opção inválida.")

    finally:
        db.close()

if __name__ == "__main__":
    main()

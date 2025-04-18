import sqlite3
from datetime import datetime, date
import calendar

class SaldoDB:
    def __init__(self, db_path="saldo.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._criar_tabelas()

    def _criar_tabelas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS saldo_inicial (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            valor REAL
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            tipo TEXT CHECK(tipo IN ('credito', 'debito')),
            valor REAL
        )''')
        self.conn.commit()

    def get_saldo_inicial(self):
        self.cursor.execute("SELECT valor FROM saldo_inicial WHERE id = 1")
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            valor = float(input("Digite o saldo inicial da conta: R$ "))
            self.cursor.execute("INSERT INTO saldo_inicial (id, valor) VALUES (1, ?)", (valor,))
            self.conn.commit()
            return valor

    def inserir_transacao(self, tipo, valor, data=None):
        if not data:
            data = datetime.today().strftime('%Y-%m-%d')
        self.cursor.execute("INSERT INTO transacoes (data, tipo, valor) VALUES (?, ?, ?)", (data, tipo, valor))
        self.conn.commit()

    def calcular_saldo_atual(self):
        saldo = self.get_saldo_inicial()
        self.cursor.execute("SELECT tipo, valor FROM transacoes")
        for tipo, valor in self.cursor.fetchall():
            saldo += valor if tipo == 'credito' else -valor
        return saldo

    def gasto_diario_permitido(self):
        hoje = date.today()
        _, dias_no_mes = calendar.monthrange(hoje.year, hoje.month)
        dias_restantes = dias_no_mes - hoje.day + 1
        saldo = self.calcular_saldo_atual()
        return saldo / dias_restantes if dias_restantes > 0 else 0

    def get_transacoes_ordenadas(self):
        self.cursor.execute("SELECT data, tipo, valor FROM transacoes ORDER BY data")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

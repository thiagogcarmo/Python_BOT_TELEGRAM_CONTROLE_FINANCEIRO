import plotly.graph_objects as go

def gerar_grafico(transacoes, saldo_inicial):
    # (mantém o gráfico interativo como antes)
    pass

def gerar_grafico_em_arquivo(transacoes, saldo_inicial):
    datas = []
    saldos = []
    saldo = saldo_inicial

    for data, tipo, valor in transacoes:
        saldo += valor if tipo == 'credito' else -valor
        datas.append(data)
        saldos.append(saldo)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=datas, y=saldos, mode='lines+markers', name='Saldo Diário'))
    fig.update_layout(title='Evolução do Saldo', xaxis_title='Data', yaxis_title='Saldo R$')
    caminho = "grafico_saldo.png"
    fig.write_image(caminho)
    return caminho

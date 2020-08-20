# Trabalhando com opções de ações.
# Pode ser usado para apurar o valor intrínseco no caso de haver exercício.
# Zera (vira pó) se não atravessa exercício.
# Não foi implementado o prêmio no cálculo
# Não foi implementada a corretagem: nem de aquisição/venda da opção e nem de exercício (que é a pior: tabela B3).

def resultopt(strike,spotnovenc,tipo,opera,qtd):
    lucroperda=spotnovenc-strike
    r="zerado"
    if strike>spotnovenc:
        calr=0
        putr=-lucroperda
    elif strike<spotnovenc:
        calr=lucroperda
        putr=0
    elif strike==spotnovenc: # sem efeito, mas deixado como espera para inclusão de corretagem
        calr=lucroperda
        putr=-lucroperda
    if opera=="venda":
        qtde=-qtd
    elif opera=="compra":
        qtde=qtd
    else:
        r="operacaonula"
    if r=="operacaonula":
        varcustoganho="Não foi especificada a operação"
    elif tipo=="call":
        varcustoganho=calr
    elif tipo=="put":
        varcustoganho=putr
    else:
        varcustoganho="Não foi especificado o tipo"
    return(varcustoganho*qtde)

# teste:
spotfinal=69.80
# resultopt(strike,spotnovenc,tipo,opera,qtd):
op1=resultopt(69.80,spotfinal,"call","compra",100)

print(f'R$ {op1:.2f}')

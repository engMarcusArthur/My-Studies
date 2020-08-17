"""
O código em Python cria um arquivo HTML que pode ser aberto direto no navegador usando a função(?)* open e escreve no arquivo usando o método (?)* write.
Veja também a tabela de "conversion types" em https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
O artifício pode ser usado para criar arquivos com qualquer extensão, contanto que seja um arquivo escrito.
*obs.: Estou um pouco em dúvida com os conceitos. Caso saiba, favor apontar.
Segue:
"""
pagina = open("index01.html", "w")
pagina.write("""
<html lang=\"pt-BR\">
<head>
<title>Pagina em HTML com Python</title>
</head>
<body>
<p>Listas contagem</p>
""")
for x in range(6):
    b=x/3
    pagina.write("<p>%f</p>" %(b))
pagina.write("""
</body>
</html>
""")
pagina.close()

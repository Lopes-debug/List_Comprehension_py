
# vendas = [120, 492, 184, 910]
# produtos = ['caixa','papel','envelope','papelão']
# meta = 250
# winners = [produto for i, produto in enumerate(produtos) if vendas[i]>meta]
# print(winners)

# vendedores = {'Maria': 120, 'Alan': 320, 'Junin': 114, 'Pedro':421}
# meta = 200
# lista =[]

# for winners in vendedores:
    
#     if vendedores[winners] > meta:
#         lista.append(vendedores[winners])
#     else:
#         lista.append(0)
# print(lista)

# # resumir em apenas uma linha de código usando list comprehension
# lista = [vendedores[item] * 0.1 if vendedores[item] > meta else 0 for item in vendedores]
# print (lista)

# lista = [( 'BEER', 329 ) , ( 'COCA', 832 ) , ('FANT', 431) , ( 'PEPS', 111), ('DELL', 134), ('SUCO', 811)]
# vazia = []
# for nome, numero in lista:
#     if numero < 200:
#         vazia.append(1000)
#     elif numero < 1000:
#         vazia.append(500)

# vazia = [1000 if numero < 200 else 500 for nome, numero in lista]
# print(vazia)


# from collections import Counter
# # encontrar top5 de uma lista usando modulo
# def find_top5(lista1, lista2):
#     tupla = zip(lista1, lista2)
#     dicionario = dict(tupla)
#     cont = Counter(dicionario).most_common(5)
#     result = [y for y, x in cont]
#     return result

# vendas = [120, 492, 184, 910, 621, 498, 103, 679, 921, 2000,]
# produtos = ['caixa','papel','envelope','papelão', 'isopor', 'gesso','piso','artesanato','sabao', 'copo']
# top = find_top5(produtos, vendas)
# print(top)

# percent = [sum(vendas[i] for i, produto in enumerate(produtos) if produto in top)]
# print('O percentual de vendas é de {:.2%}'.format(percent[0]/sum(vendas)))

# EXERCICIO 1

# vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016)]

# empty = []
# for nome, venda1, venda2 in vendas_produtos:
#     empty.append(venda1)
# print(empty)

# vendas = [vendas1 for nome, vendas1, vendas2 in vendas_produtos ]

#vendas_produto = [(vendas1, produto) for nome, vendas1, vendas2 in vendas_produtos]

# EXERCICIO 2

# clientes_devedores = [('462.286.561-65',14405,24),('251.569.170-81',16027,1),('297.681.579-21',8177,28),('790.223.154-40',9585,10),('810.442.219-10',18826,29),('419.210.299-79',11421,15)]

# comprehension = [cpf for cpf, valor, dias in clientes_devedores if dias >20]
# print(comprehension)


# EXERCICIO 3

# estoque = [('BSA2199',396),('PPF5239',251),('BSA1212',989),('PPF2154',449),('BEB3410',241),('PPF8999',527),('EMB9591',601),('BSA2006',314),('EMB3604',469),('EMB2070',733),('PPF9018',339),('PPF1468',906),('BSA5819',291),('PPF8666',850),('BEB2983',353),('BEB5877',456),('PPF5008',963),('PPF3877',185),('PPF7321',163),('BSA8833',644)]

# bsa = [1000 if qnt < 200 else 500 for produto, qnt in estoque if 'BSA' in produto]
# print(bsa)
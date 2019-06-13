arestas = []
arq = open('4730_286722.txt', 'r')
instancia = arq.readlines()
matriz = []*int(instancia[0])
for i in range(int(instancia[0])):
    linha = []
    for j in range(int(instancia[0])):
        linha.append(0)
    matriz.append(linha)
for aresta in instancia[2:]:
    aresta_split = aresta.split(" ")
    aresta_split.remove('e')
    matriz[int(aresta_split[0])-1][int(aresta_split[1])-1] = 1
    matriz[int(aresta_split[1])-1][int(aresta_split[0])-1] = 1
arq.close()

#Algoritmo Guloso
cores = [1]+['n']*(int(instancia[0])-1)
for i, linha in enumerate(matriz[1:]):
    usadas = []
    for j, aresta in enumerate(linha):
        if aresta == 1:
            if not(cores[j] == 'n'):
                usadas.append(cores[j])

    for k in range(int(instancia[0])-1):
        if not(k+1 in usadas):
            cores[i+1] = k+1
            break
'''
for i in range(int(instancia[0])):
    print (i+1,cores[i])
'''
print("Guloso")
print("Min Cores = ", max(cores))
print("")

#Força Bruta

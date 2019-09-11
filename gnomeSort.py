from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from random import shuffle, randint
import random
 
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
  
def geraInversa(size):
  lista=list(range(size,1,-1))
  return lista

def geraOrdenado(size):
	return list(range(size))


def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    #ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]

  

def gnomeSort(vet):
    leng = len(vet)
    idx = 0
    while idx < leng:
        if idx == 0:
            idx = idx + 1
        if vet[idx] >= vet[idx - 1]:
            idx = idx + 1
        else:
            auidx = vet[idx]
            vet[idx] = vet[idx-1]
            vet[idx-1] = auidx
            idx-=1
    return vet
            

listas=[]
listaInversa=[]
listaOrdenada=[]
x2 = [10000, 20000, 40000, 100000]
y = []
y2=[]
y3=[]

for i in range(len(x2)):
  listas.append(geraLista(x2[i]))
  listaInversa.append(geraInversa(x2[i]))


for i in range(len(x2)):
  y.append(timeit.timeit("gnomeSort({})".format(listas[i]),setup="from __main__ import gnomeSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")


print(operacoes[:])

desenhaGrafico(x2,y,'Quantidade','Tempo', 'gnomeSort')

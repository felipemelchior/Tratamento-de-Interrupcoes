import threading # Biblioteca de threads
import time # Biblioteca de tempo
import random as rd # Biblioteca usada para aleatorizar numeros

class Backend():
    def __init__(self):
        self.prioridade = [-1,-1,-1,-1] # Inicio da lista de prioridade
        self.fila = [-1,-1,-1,-1] # Inicio da fila de processos
        self.situacao = ['R','R','R','R'] # Inicio da lista de situacao
        self.tempoBloqueio = [0,0,0,0] # Inicio da lista de tempo de bloqueio

    def inicializaFila(self): # Inicializa a fila ja ordenada com a sua devida prioridade 
        aux = [[1, self.prioridade[0]],[2, self.prioridade[1]], [3, self.prioridade[2]],[4, self.prioridade[3]]]

        for i in range(len(aux)):
            for j in range(len(aux)-i-1):
                if(aux[i][1] < aux[i+1][1]):
                    aux[i],aux[i+1] = aux[i+1],aux[i]

        for i in range(len(aux)):
            self.fila[i] = aux[i][0]

    def defineSituacao(self): # Gera um numero aleatorio, e com base nesse numero, bloqueia ou nao o processo
        bloq = rd.randrange(10)

        if(bloq == 0):
            print("Thread Bloqueada")
            self.tempoBloqueio[self.fila[0]-1] = rd.randrange(5,10)
            self.situacao[self.fila[0]-1] = 'B'
            self.fila[0] = -1

    def retornaPrioridade(self): # Gera a lista de prioridade inicial
        self.prioridade = [rd.randrange(10),rd.randrange(10),rd.randrange(10),rd.randrange(10)]
        return self.prioridade

    def retornaFila(self): # Move a fila de processos e modifica as prioridades
        self.defineSituacao()
        
        for i in range(len(self.fila)-1):
            if(self.fila[i+1] == -1):
                break
            self.fila[i],self.fila[i+1] = self.fila[i+1],self.fila[i]


        for i in range(len(self.fila)):
            if(i == 0 and self.situacao[self.fila[i]-1] == 'R'):
                self.prioridade[self.fila[i]-1] -= 1
            elif(self.situacao[self.fila[i]-1] == 'R'):
                self.prioridade[self.fila[i]-1] += 1
            
        return self.fila

    def retornaSituacao(self): # Retorna a situacao
        return self.situacao

    def retornaTempoBloqueio(self): # Decrementa o tempo de bloqueio e retorna o elemento na sua devida posicao na fila
        for i in range(len(self.tempoBloqueio)):
            if(self.tempoBloqueio[i] > 0):
                self.tempoBloqueio[i] -= 1
            if(self.situacao[i] == 'B' and self.tempoBloqueio[i] == 0):
                for j in range(len(self.tempoBloqueio)):
                    if(self.fila[j] == -1):
                        self.fila[j] = i+1
                        self.situacao[i] = 'R'
                        break

        for i in range(len(self.fila)):
            for j in range(len(self.fila)-i-1):
                if(self.fila[i] == -1):
                    self.fila[i],self.fila[i+1] = self.fila[i+1], self.fila[i]

                elif(self.prioridade[self.fila[i]-1] < self.prioridade[self.fila[i+1]-1]):
                    self.fila[i],self.fila[i+1] = self.fila[i+1], self.fila[i]
                              
        return self.tempoBloqueio
        
            



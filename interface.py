import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QThread
from backend import * # Importacao da classe backend

# Variaveis globais
bk = Backend() # Instanciacao da classe backend
aux = []

# Funcao que a Thread utiliza para ficar atualizando os dados
def Atualiza():
    global aux
    aux1 = bk.retornaPrioridade()
    bk.inicializaFila()
    while True:
        aux2 = bk.retornaFila()
        aux3 = bk.retornaSituacao()
        aux4 = bk.retornaTempoBloqueio()

        aux = [aux1, aux2, aux3, aux4]
        time.sleep(1)
        print("Valores Atualizados")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        global bk
        global aux
        self.title = 'Interrupções' # Titulo da janela
        self.width = 420 # Largura da janela
        self.height = 480 # Altura da janela
        self.responsivo = 30
        self.initUI()
        self.Thread1 = threading.Thread(target=Atualiza) # Thread de atualizacao dos dados
        self.Thread1.start()
        self.stop_event = threading.Event() # Variavel do tipo evento, usada para condicao de parada da thread
        self.Thread2 = threading.Thread(target=self.updateUI,args=(self.stop_event,)) # Thread de atualizacao da janela
        self.Thread2.start()

    def initUI(self):
        # Inicia a Janela
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
       
        # Cria Botão de Ajuda
        self.button_help = QPushButton('Ajuda', self)
        self.button_help.move(20, 15)
        self.button_help.resize(166, 30)
        self.button_help.clicked.connect(self.Ajuda)

        # Texto Threads
        self.lbl = QLabel(self)
        self.lbl.setText('Threads')
        self.lbl.move(20, 15+self.responsivo)

        # Cria as Caixas de Texto das Threads
        self.thread_1 = QLineEdit(self)
        self.thread_1.move(20, 45+self.responsivo)
        self.thread_1.setText('    1')
        self.thread_1.resize(40,80)

        self.thread_2 = QLineEdit(self)
        self.thread_2.move(62, 45+self.responsivo)
        self.thread_2.setText('    2')
        self.thread_2.resize(40,80)

        self.thread_3 = QLineEdit(self)
        self.thread_3.move(104, 45+self.responsivo)
        self.thread_3.setText('    3')
        self.thread_3.resize(40,80)

        self.thread_4 = QLineEdit(self)
        self.thread_4.move(146, 45+self.responsivo)
        self.thread_4.setText('    4')
        self.thread_4.resize(40,80)

        # Texto Fila
        self.lbl = QLabel(self)
        self.lbl.setText('Fila de Prioridade')
        self.lbl.move(230, 160+self.responsivo)
        self.lbl.resize(200,10)

        # Cria as Caixas de Texto das Prioridades
        self.fila_1 = QLineEdit(self)
        self.fila_1.move(230, 180+self.responsivo)
        self.fila_1.resize(40,80)

        self.fila_2 = QLineEdit(self)
        self.fila_2.move(272, 180+self.responsivo)
        self.fila_2.resize(40,80)

        self.fila_3 = QLineEdit(self)
        self.fila_3.move(314, 180+self.responsivo)
        self.fila_3.resize(40,80)

        self.fila_4 = QLineEdit(self)
        self.fila_4.move(356, 180+self.responsivo)
        self.fila_4.resize(40,80)

        # Texto Prioridade
        self.lbl = QLabel(self)
        self.lbl.setText('Prioridade')
        self.lbl.move(20, 150+self.responsivo)

        # Cria as Caixas de Texto das Prioridades
        self.prioridade_1 = QLineEdit(self)
        self.prioridade_1.move(20, 180+self.responsivo)
        self.prioridade_1.resize(40,80)

        self.prioridade_2 = QLineEdit(self)
        self.prioridade_2.move(62, 180+self.responsivo)
        self.prioridade_2.resize(40,80)

        self.prioridade_3 = QLineEdit(self)
        self.prioridade_3.move(104, 180+self.responsivo)
        self.prioridade_3.resize(40,80)

        self.prioridade_4 = QLineEdit(self)
        self.prioridade_4.move(146, 180+self.responsivo)
        self.prioridade_4.resize(40,80)

        # Texto Situação
        self.lbl = QLabel(self)
        self.lbl.setText('Situação')
        self.lbl.move(20, 285+self.responsivo)

        # Cria as Caixas de Texto da Situação
        self.situacao_1 = QLineEdit(self)
        self.situacao_1.move(20, 315+self.responsivo)
        self.situacao_1.resize(40,80)

        self.situacao_2 = QLineEdit(self)
        self.situacao_2.move(62, 315+self.responsivo)
        self.situacao_2.resize(40,80)

        self.situacao_3 = QLineEdit(self)
        self.situacao_3.move(104, 315+self.responsivo)
        self.situacao_3.resize(40,80)

        self.situacao_4 = QLineEdit(self)
        self.situacao_4.move(146, 315+self.responsivo)
        self.situacao_4.resize(40,80)

        # Texto Tempo
        self.lbl = QLabel(self)
        self.lbl.setText('Tempo de Bloqueio')
        self.lbl.move(230, 295+self.responsivo)
        self.lbl.resize(200,10)

        # Cria as Caixas de Texto do Tempo
        self.tempo_1 = QLineEdit(self)
        self.tempo_1.move(230, 315+self.responsivo)
        self.tempo_1.resize(40,80)

        self.tempo_2 = QLineEdit(self)
        self.tempo_2.move(272, 315+self.responsivo)
        self.tempo_2.resize(40,80)

        self.tempo_3 = QLineEdit(self)
        self.tempo_3.move(314, 315+self.responsivo)
        self.tempo_3.resize(40,80)

        self.tempo_4 = QLineEdit(self)
        self.tempo_4.move(356, 315+self.responsivo)
        self.tempo_4.resize(40,80)

        self.show()

    # Funcao que atualiza janela
    def updateUI(self, stop_argument):
        while True and not stop_argument.isSet():
            self.prioridade_1.setText("    " + str(aux[0][0]))
            self.prioridade_2.setText("    " + str(aux[0][1]))
            self.prioridade_3.setText("    " + str(aux[0][2]))
            self.prioridade_4.setText("    " + str(aux[0][3]))

            self.fila_1.setText("    " + str(aux[1][0]))
            self.fila_2.setText("    " + str(aux[1][1]))
            self.fila_3.setText("    " + str(aux[1][2]))
            self.fila_4.setText("    " + str(aux[1][3]))

            self.situacao_1.setText("    " + str(aux[2][0]))
            self.situacao_2.setText("    " + str(aux[2][1]))
            self.situacao_3.setText("    " + str(aux[2][2]))
            self.situacao_4.setText("    " + str(aux[2][3]))

            self.tempo_1.setText("    " + str(aux[3][0]))
            self.tempo_2.setText("    " + str(aux[3][1]))
            self.tempo_3.setText("    " + str(aux[3][2]))
            self.tempo_4.setText("    " + str(aux[3][3]))
        
    # Função que exibe a ajuda do programa
    def Ajuda(self):
        QMessageBox.question(self, "Ajuda", "Este Software tem como objetivo simular um sistema de tratamento de interrupção\n\n1. Bloco de Threads\nNeste bloco, estarão os números das quatros threads, fixas.\n\n2.Bloco de Prioridade\nNeste bloco se localizam a prioridade de cada thread. Quanto maior este número, maior será sua prioridade.\n\n3. Fila de Processos\nAqui se encontra a situação atual da fila, atualizada a cada segundo.\n\n4. Situação\nEste bloco mostra a atual situação de cada thread. Tendo 'R' significando 'Rodando' e 'B' significando 'Bloqueada'.\n\n5. Tempo de Bloqueio\nNeste bloco estão indicadas a quantidade de ciclos que aquela thread está bloqueada. Este número decrementa a cada segundo, ou seja, 1 ciclo por segundo.", QMessageBox.Ok)
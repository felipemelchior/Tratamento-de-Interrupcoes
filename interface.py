import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Interrupções' # Titulo da janela
        self.width = 210 # Largura da janela
        self.height = 600 # Altura da janela
        self.responsivo = 30
        self.initUI()

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
        self.thread_1.resize(40,80)

        self.thread_2 = QLineEdit(self)
        self.thread_2.move(62, 45+self.responsivo)
        self.thread_2.resize(40,80)

        self.thread_3 = QLineEdit(self)
        self.thread_3.move(104, 45+self.responsivo)
        self.thread_3.resize(40,80)

        self.thread_4 = QLineEdit(self)
        self.thread_4.move(146, 45+self.responsivo)
        self.thread_4.resize(40,80)

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
        self.lbl.move(20, 420+self.responsivo)
        self.lbl.resize(200,20)

        # Cria as Caixas de Texto do Tempo
        self.tempo_1 = QLineEdit(self)
        self.tempo_1.move(20, 450+self.responsivo)
        self.tempo_1.resize(40,80)

        self.tempo_2 = QLineEdit(self)
        self.tempo_2.move(62, 450+self.responsivo)
        self.tempo_2.resize(40,80)

        self.tempo_3 = QLineEdit(self)
        self.tempo_3.move(104, 450+self.responsivo)
        self.tempo_3.resize(40,80)

        self.tempo_4 = QLineEdit(self)
        self.tempo_4.move(146, 450+self.responsivo)
        self.tempo_4.resize(40,80)

        self.show()

    def Ajuda(self): # Função que exibe a ajuda do programa
        QMessageBox.question(self, "Ajuda", "Este Software ajuda", QMessageBox.Ok)
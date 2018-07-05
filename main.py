from interface import * # Imporacao da classe interface

if __name__ == '__main__': # Inicio do programa
    app = QApplication(sys.argv)
    ex = Window() # Instanciacao da classe
    sys.exit(app.exec_())
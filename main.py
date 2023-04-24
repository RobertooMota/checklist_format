import sys
from PySide6.QtWidgets import QFileDialog, QMessageBox
from main_script import format
from ui_main import *

titulo = "CheckList - Automático v0.1"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.arquivo = None
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.setWindowTitle(titulo)
        self.show()

        # Botões
        self.main.btn_CarregarArquivos.clicked.connect(lambda: self.CarregarArquivos())
        self.main.btn_CriarCL.clicked.connect(lambda: self.CriarCL())

    def CarregarArquivos(self):
        self.arquivo = QFileDialog.getOpenFileNames(self, "Abrir arquivo", "", "Planilha do Excel (*.xlsx)")

    def CriarCL(self):
        if format(self.arquivo[0][0], '90-200'):
            Msg = QMessageBox()
            Msg.setIcon(QMessageBox.Information)
            Msg.setWindowTitle('Alerta')
            Msg.setText("Concluido com sucesso!")
            Msg.exec()
        else:
            Msg = QMessageBox()
            Msg.setIcon(QMessageBox.Critical)
            Msg.setWindowTitle('Alerta')
            Msg.setText("ERRO!")
            Msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicativo = MainWindow()
    sys.exit(app.exec())

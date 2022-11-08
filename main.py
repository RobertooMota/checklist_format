import sys
from PySide6.QtWidgets import QFileDialog, QMessageBox
from TESTE_main import formatChecklist

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
        formatChecklist(self.arquivo[0][0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicativo = MainWindow()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindgcEyr.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 201)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_CarregarArquivos = QPushButton(self.frame_2)
        self.btn_CarregarArquivos.setObjectName(u"btn_CarregarArquivos")
        self.btn_CarregarArquivos.setMinimumSize(QSize(30, 40))
        self.btn_CarregarArquivos.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout.addWidget(self.btn_CarregarArquivos)

        self.btn_CriarCL = QPushButton(self.frame_2)
        self.btn_CriarCL.setObjectName(u"btn_CriarCL")
        self.btn_CriarCL.setMinimumSize(QSize(30, 40))
        self.btn_CriarCL.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout.addWidget(self.btn_CriarCL)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CHECKLIST - AUTOM\u00c1TICO", None))
        self.btn_CarregarArquivos.setText(QCoreApplication.translate("MainWindow", u"Carregar arquivo", None))
        self.btn_CriarCL.setText(QCoreApplication.translate("MainWindow", u"Criar Checklist", None))
    # retranslateUi


from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout,QPushButton,QLabel,QTextEdit,QLineEdit

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

import sys

class Yapi(QWidget):
    def __init__(self):
        super().__init__()

        self.alan()

    def alan(self):


        self.kelimeler = QTextEdit()
        self.buton = QPushButton("Çekilişi Yap!")
        self.sonu = QLabel("")


        vbox = QVBoxLayout()
        vbox.addWidget(self.kelimeler)
        vbox.addWidget(self.sonu)
        vbox.addWidget(self.buton)
        self.setLayout(vbox)

        self.setGeometry(300, 200, 400, 400)
        self.setWindowTitle("Çekiliş Yazılımı")

        self.buton.clicked.connect(self.bas)
        self.show()

    def bas(self):
        self.sonu.setText("Kazanan : {}".format(atmaca))



class ana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = Yapi()

        self.setCentralWidget(self.pencere)

        self.devam()


    def devam(self):


        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")


        cik = QAction("Çıkış", self)
        cik.setShortcut("ctrl+q")
        dosya.addAction(cik)

        hile = QAction("Hile",self)
        hile.setShortcut("ctrl+h")
        dosya.addAction(hile)


        hile.triggered.connect(lanaaa.show())
        cik.triggered.connect(self.bana)

    def bana(self):
            qApp.quit()



class ha(QWidget):
    def __init__(self):

        super().__init__()

        self.aq()

    def aq(self):
        self.al = QLineEdit("")
        self.tkla = QPushButton("Bu hileli!")

        vh = QVBoxLayout()
        vh.addWidget(self.al)
        vh.addWidget(self.tkla)
        self.setLayout(vh)
        self.setWindowTitle("Hile")

        self.setGeometry(300,200,300,300)
        self.tkla.clicked.connect(self.lan)
        self.show()

    def lan(self):
        global atmaca
        atmaca = self.al.text()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    lanaaa = ha()
    aaa = Yapi()

    sys.exit(app.exec_())


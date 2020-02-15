from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout,QPushButton,QLabel,QTextEdit,QLineEdit,QHBoxLayout,QComboBox

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

import sys

class Yapi(QWidget):
    def __init__(self):
        super().__init__()

        self.alan()

    def alan(self):


        self.kelimeler = QTextEdit()
        self.buton = QPushButton("Çekilişi Yap!")
        self.burl_ad = QLabel("Gönderinin Bağlantısı: ")
        self.burl = QLineEdit("")
        self.sonu = QLabel("")

        self.etiket_ad = QLabel("Her etiket 1 katılım sayılsın mı ?")
        a = ["Evet","Hayır"]
        self.etiket = QComboBox(self)
        self.etiket.addItems(a)

        self.kisi = QLineEdit()
        self.kisi_ad = QLabel("Çekilişi kazanacak kişi sayısı ?")

        self.bosluk1 = QLabel("")
        self.bosluk2 = QLabel("")


        hbox = QHBoxLayout()
        hbox.addWidget(self.burl_ad)
        hbox.addWidget(self.burl)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.etiket_ad)
        hbox1.addWidget(self.etiket)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.kisi_ad)
        hbox2.addWidget(self.kisi)

        vbox = QVBoxLayout()
        vbox.addWidget(self.kelimeler)
        vbox.addWidget(self.bosluk1)
        vbox.addWidget(self.sonu)
        vbox.addWidget(self.bosluk2)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.buton)

        self.setLayout(vbox)


        self.buton.clicked.connect(self.bas)


    def bas(self):
        self.sonu.setText("Kazananlar : {}".format(atmaca))



class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kapan = Yapi()
        self.setCentralWidget(self.kapan)

        self.devam()


    def devam(self):


        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")


        cik = QAction("Çıkış", self)
        cik.setShortcut("ctrl+q")


        hile = QAction("Hile",self)
        hile.setShortcut("ctrl+h")

        dosya.addAction(hile)
        dosya.addAction(cik)

        dosya.triggered.connect(self.bana)

        self.setWindowTitle("Çekiliş Yazılımı")
        self.setGeometry(400, 100, 400, 400)
        self.show()

    def bana(self,action):
        if action.text() == "Hile":
            lanaaa.show()

        elif action.text() == "Çıkış":

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

    def lan(self):
        global atmaca
        atmaca = self.al.text()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    pakan = Menu()
    lanaaa = ha()

    sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def window_go():

    app = QApplication(sys.argv)
    window = QWidget()


    textLabel = QLabel(window)
    textLabel.setText("Belajar PyQt5")
    textLabel.move(5,5) #jarak tulisan Belajar PyQt5
    for x in range (5):
        p = QPushButton(window)
        p.resize(40,40) #ukuran kotak
        p.setStyleSheet("background-color: black; color: white; font-size: 25px; font: Times New Roman")
        p.setText(str(x+1))
        p.move(50*(x),20) #50 itu untuk jarak setiap kotak, 20 itu jarak antara tulisan belajar pyqt5 dan kotak

    window.setGeometry(100, 100, 300, 300)
    window.setWindowTitle("Contoh PyQt5")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window_go()


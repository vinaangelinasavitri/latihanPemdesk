import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel 


def window_go():

    app = QApplication(sys.argv)
    window = QWidget()


    textLabel = QLabel(window)
    label = [None]*15
    baris = 30
    for x in range (1,11):
        baris = baris + 15
        label[x] = QLabel(window)
        label[x].setText("Ini Angka " + str(x))
        label[x].move(10,baris)

    window.setGeometry(50, 50, 300, 300)
    window.setWindowTitle("Contoh PyQt5")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window_go()




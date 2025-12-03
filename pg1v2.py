from PyQt6 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from pg2full import TypewriterDemo

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cyber Sentinel")
        self.setGeometry(100, 100, 1451, 918)
        self.setStyleSheet("background-color: black;")
        self.central = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central)
        self.video_widget = QtMultimediaWidgets.QVideoWidget(self.central)
        self.video_widget.setGeometry(0, 0, 1451, 918)

        self.player = QtMultimedia.QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)

        video_path = "D:/Studies/Computer/CyberSentinal/Images/bgmainv.mp4"
        self.player.setSource(QtCore.QUrl.fromLocalFile(video_path))
        self.player.setLoops(QtMultimedia.QMediaPlayer.Loops.Infinite)
        self.player.play()

        QtCore.QTimer.singleShot(8000, self.open_next_window)

    def open_next_window(self):
        self.new_window = TypewriterDemo()
        self.new_window.showFullScreen()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec())

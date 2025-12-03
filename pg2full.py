import sys
import re
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, Qt, QDateTime
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QLabel, QWidget, QGraphicsDropShadowEffect


# Define the new primary color
NEON_BLUE = "#00ffff" # A bright cyan/electric blue
ALERT_RED = "#ff0000"

# ---------------- TYPEWRITER EFFECT FUNCTION (HTML-SAFE) ---------------- #
def typewriter_effect_html(label, html_text, speed=30, on_complete=None):
    """Typewriter animation that supports HTML styling safely."""
    plain_text = re.sub("<[^>]+>", "", html_text)
    label.setText("")
    i = 0

    def update():
        nonlocal i
        if i < len(plain_text):
            visible_text = plain_text[:i + 1]
            j = 0
            rendered = ""
            tag = False
            
            for ch in html_text:
                if ch == "<":
                    tag = True
                
                if not tag:
                    if j < len(visible_text):
                        rendered += ch
                        j += 1
                
                if tag:
                    rendered += ch
                    
                if ch == ">":
                    tag = False
                
                if j >= len(visible_text) and not tag:
                    if ch == '>': 
                        break
                    if not tag:
                        break

            label.setText(rendered)
            i += 1
        else:
            timer.stop()
            label.setText(html_text)
            if on_complete:
                on_complete()

    timer = QTimer()
    timer.timeout.connect(update)
    timer.start(speed)


# ------------------- MAIN WINDOW UI CLASS ------------------- #
class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(1450, 780)
        MainWindow1.setStyleSheet("background-color: #000000;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow1)
        self.centralwidget.setObjectName("centralwidget")

        # --- Logo ---
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(480, 70, 420, 460))
        self.logo.setPixmap(QtGui.QPixmap("D:\\Studies\\Computer\\CyberSentinal\\Images\\small logo2.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        # --- Text box for typewriter effect ---
        self.textbox1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.textbox1.setGeometry(QtCore.QRect(250, 550, 950, 151))
        self.textbox1.setStyleSheet("background-color: 000000; color: rgb(255, 255, 255);")
        self.textbox1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textbox1.setFont(QFont("Courier New", 14))
        self.textbox1.setText("")
        self.textbox1.setWordWrap(True)
        self.textbox1.setObjectName("textbox1")
        # Set the text color to NEON_BLUE
        self.textbox1.setStyleSheet("background-color: #000000; color: " + NEON_BLUE + ";")

        # Apply glow effect using QGraphicsDropShadowEffect
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(20)          # how soft the glow is
        glow.setColor(QColor(NEON_BLUE)) # glow color
        glow.setOffset(0)               # center glow
        self.textbox1.setGraphicsEffect(glow)


        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 22))
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow1)
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "CyberSentinel"))


# ------------------- EXTENDED WINDOW LOGIC ------------------- #
class TypewriterDemo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

        # Initialize persistent animation objects
        self.mission_opacity_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.training_opacity_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.mission_anim = QtCore.QPropertyAnimation(self.mission_opacity_effect, b"opacity")
        self.training_anim = QtCore.QPropertyAnimation(self.training_opacity_effect, b"opacity")


        # Neon blue glow effect for text
        glow = QGraphicsDropShadowEffect()
        # 🟢 CHANGED: Glow color to NEON_BLUE
        glow.setColor(QColor(NEON_BLUE)) 
        glow.setBlurRadius(25)
        glow.setOffset(0)
        self.ui.textbox1.setGraphicsEffect(glow)

        # Dynamic timestamp
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")

        # 🟢 CHANGED: HTML inline style color to NEON_BLUE
        intro_text = (
            f"<span style='color:{NEON_BLUE};'>SYSTEM LOG [Aethel Corp // {current_time}]</span><br>"
            "<span style='color:white;'>Welcome, Junior Security Analyst.<br>"
            "<span style='color:#ff2e2e; font-weight:bold;'>"
            "MOMENTS AGO, OUR CORE DATABASE — THE NEXUS ENGINE — DETECTED A BREACH ATTEMPT."
            "</span><br>"
            "Prepare to defend the network.</span>"
        )

        typewriter_effect_html(self.ui.textbox1, intro_text, speed=40, on_complete=self.show_alert)

        # --- Mission Buttons (Initially Hidden) ---
        self.mission_btn = self.create_button("ENTER TRAINING CENTER", 450, 720)
        self.training_btn = self.create_button("GO TO MISSION 1", 750, 720)

        self.mission_btn.hide()
        self.training_btn.hide()
        self.mission_btn.clicked.connect(self.open_training_center)
        self.training_btn.clicked.connect(self.open_missions)

        # Apply the persistent effects to the buttons
        self.mission_btn.setGraphicsEffect(self.mission_opacity_effect)
        self.training_btn.setGraphicsEffect(self.training_opacity_effect)

    def create_button(self, text, x, y):
        btn = QtWidgets.QPushButton(text, self)
        btn.setGeometry(x, y, 280, 50)
        btn.setFont(QFont("Courier New", 14))
        # 🟢 CHANGED: CSS colors and box-shadow color to NEON_BLUE
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #030527;
                color: {NEON_BLUE};
                border: 2px solid {NEON_BLUE};
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 0 15px 5px {NEON_BLUE}; 
            }}
            QPushButton:hover {{
                background-color: {NEON_BLUE};
                color: black;
                box-shadow: 0 0 15px 5px {NEON_BLUE};
            }}
        """)
        return btn

    def show_alert(self):
        """Show red system breach alert popup."""
        alert = QWidget(self)
        alert.setWindowTitle("ALERT")
        alert.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        alert.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        alert.resize(500, 200)

        parent_center = self.geometry().center()
        alert.move(parent_center.x() - alert.width() // 2, parent_center.y() - alert.height() // 2)

        label = QLabel("SYSTEM BREACH DETECTED", alert)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Consolas", 24, QFont.Weight.Bold))
        # Alert remains RED
        label.setStyleSheet(f"""
        QLabel {{
            color: {ALERT_RED};
            background-color: #1a0000;
            border: 3px solid {ALERT_RED};
            border-radius: 10px;
            padding: 30px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        """)

        glow = QGraphicsDropShadowEffect()
        # Alert glow remains RED
        glow.setColor(QColor(ALERT_RED))
        glow.setBlurRadius(40)
        glow.setOffset(0)
        label.setGraphicsEffect(glow)
        alert.show()

        QTimer.singleShot(800, self.spawn_warning_logo)
        QTimer.singleShot(1400, self.spawn_warning_logo)
        QTimer.singleShot(2000, self.spawn_warning_logo)
        QTimer.singleShot(2600, self.spawn_warning_logo)

        QTimer.singleShot(3000, alert.close)
        QTimer.singleShot(3500, self.show_buttons)

    def spawn_warning_logo(self):
        """Spawns a temporary skull warning logo at a random position."""
        import random
        skull = QLabel(self)
        skull.setPixmap(QtGui.QPixmap("D:\\Studies\\Computer\\CyberSentinal\\Images\\skull.png"))
        skull.setScaledContents(True)
        skull.resize(92, 92)
        x = random.randint(50, self.width() - 130)
        y = random.randint(50, self.height() - 130)
        skull.move(x, y)
        skull.show()
        QTimer.singleShot(700, skull.deleteLater)

    def show_buttons(self):
        """Fade in both mission and training buttons together."""
        
        # 1. Setup the mission button animation
        self.mission_btn.show()
        self.mission_anim.setDuration(1200)
        self.mission_anim.setStartValue(0)
        self.mission_anim.setEndValue(1)
        self.mission_anim.start(QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped)

        # 2. Setup the training button animation
        self.training_btn.show()
        self.training_anim.setDuration(1200)
        self.training_anim.setStartValue(0)
        self.training_anim.setEndValue(1)
        self.training_anim.start(QtCore.QAbstractAnimation.DeletionPolicy.KeepWhenStopped)

    def open_training_center(self):
        try:
            from infofinal import LoadingScreen
            self.loading = LoadingScreen()
            self.loading.show()
            self.hide()

        except Exception as e:
            print("ERROR OPENING P2:", e)
            
    def open_missions(self):
        try:
            from missions import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()   # create a real window
            self.ui = Ui_MainWindow()               # create UI object
            self.ui.setupUi(self.window)            # attach UI to window

            self.window.show()
            self.close()

        except Exception as e:
            print("ERROR OPENING P2:", e)




# ------------------- APP LAUNCH ------------------- #
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TypewriterDemo()
    window.showFullScreen()
    sys.exit(app.exec())

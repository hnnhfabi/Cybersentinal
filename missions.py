from PyQt6 import QtCore, QtGui, QtWidgets
import random
import re
import sys

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, 26 - shift)

def rot13(text):
    return caesar_encrypt(text, 13)

def is_strong(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r"[A-Z]", pwd):
        return False
    if not re.search(r"[a-z]", pwd):
        return False
    if not re.search(r"[0-9]", pwd):
        return False
    if not re.search(r"[!@#$%^&*()\-_=+?/]", pwd):
        return False
    return True


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1446, 850)
        MainWindow.setStyleSheet("background-color: #1a1a1a;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 1431, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"D:\Studies\Computer\CyberSentinal\Images\bg1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 120, 1131, 561))
        self.stackedWidget.setStyleSheet("/*background-color: #5C5C5C;*/\n"
"background-color:#1a1a1a ;")
        self.stackedWidget.setObjectName("stackedWidget")

        common_button_style = """
            QPushButton { background-color: #00ffff; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-size: 24px; font-weight: bold; }
            QPushButton:hover { background-color: #4FC3FF; }
            QPushButton:pressed { background-color: #1E90FF; padding-left: 12px; padding-top: 12px; }
        """

        # MISSION 1 SETUP
        # =========================================================
        self.m1 = QtWidgets.QWidget()
        self.m1.setObjectName("m1")

        self.all_passwords_m1 = ["admin123", "R3d_F0x!", "qwerty", "NexusCore#98", "hello123"]
        self.weak_passwords_to_fix = ["admin123", "qwerty", "hello123"]
        self.total_required_fixes = len(self.weak_passwords_to_fix)
        self.fixed_count_m1 = 0
        
        self.password_list_widget = QtWidgets.QListWidget(parent=self.m1)
        self.password_list_widget.setGeometry(QtCore.QRect(100, 250, 391, 215))
        self.password_list_widget.setStyleSheet("""
            QListWidget { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px; padding: 10px; }
            QListWidget::item { padding: 5px; }
        """)
        self.password_list_widget.setObjectName("password_list_widget")
        
        for pwd in self.all_passwords_m1:
            item = QtWidgets.QListWidgetItem(pwd)
            if is_strong(pwd):
                item.setData(QtCore.Qt.ItemDataRole.UserRole, "strong_secured") 
            else:
                 item.setData(QtCore.Qt.ItemDataRole.UserRole, "weak_unsecured")
            self.password_list_widget.addItem(item)
            
        list_title = QtWidgets.QLabel(parent=self.m1)
        list_title.setGeometry(QtCore.QRect(100, 190, 391, 40))
        list_title.setStyleSheet("font-size: 26pt; color: #ffffff;")
        list_title.setText("EMPLOYEE PASSWORDS:")

        self.label_3 = QtWidgets.QLabel(parent=self.m1)
        self.label_3.setGeometry(QtCore.QRect(600, 200, 391, 51))
        self.label_3.setStyleSheet("background-color: #1a1a1a")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.m1)
        self.label_4.setGeometry(QtCore.QRect(600, 330, 391, 51)) 
        self.label_4.setStyleSheet("background-color: #1a1a1a")
        self.label_4.setObjectName("label_4")
        
        self.strongpasswdm1 = QtWidgets.QLineEdit(parent=self.m1)
        self.strongpasswdm1.setGeometry(QtCore.QRect(600, 375, 391, 41)) 
        self.strongpasswdm1.setStyleSheet("background-color: #5C5C5C;\n"
"border: 2px solid white;\n"
" border-radius: 6px;\n"
"color: white;\n"
"font-size: 22px;")
        self.strongpasswdm1.setObjectName("strongpasswdm1")
        
        self.selectedpasswdm1 = QtWidgets.QLabel(parent=self.m1)
        self.selectedpasswdm1.setGeometry(QtCore.QRect(600, 245, 391, 41)) 
        self.selectedpasswdm1.setStyleSheet("QLabel { background-color: #2a2a2a; border: 2px solid #00ffff; border-radius: 6px; color: #00ffff; font-size: 22px; padding-left: 10px; }")
        self.selectedpasswdm1.setText("Click a weak password to select it.")
        self.selectedpasswdm1.setObjectName("selectedpasswdm1")
        self.pushButton = QtWidgets.QPushButton(parent=self.m1)
        self.pushButton.setGeometry(QtCore.QRect(540, 470, 251, 41))
        self.pushButton.setObjectName("pushButton") 
        self.dispstrength = QtWidgets.QLabel(parent=self.m1)
        self.dispstrength.setGeometry(QtCore.QRect(620, 430, 361, 20))
        self.dispstrength.setText("")
        self.dispstrength.setObjectName("dispstrength")
        self.dispstrength.setStyleSheet("color: red; font-size: 22px;")
        self.label_7 = QtWidgets.QLabel(parent=self.m1)
        self.label_7.setGeometry(QtCore.QRect(110, 40, 931, 131))
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=self.m1)
        self.label_5.setGeometry(QtCore.QRect(360, 0, 411, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.m1)
        self.pushButton_5.setGeometry(QtCore.QRect(830, 470, 251, 41))
        self.pushButton_5.setObjectName("pushButton_5") 

        self.pushButton.setStyleSheet(common_button_style)
        self.pushButton_5.setStyleSheet(common_button_style)
        
        self.stackedWidget.addWidget(self.m1)
        
        # MISSION 1 LOGIC
        self.current_selected_item = None 

        def select_password_m1(item):
            if item.data(QtCore.Qt.ItemDataRole.UserRole) in ("secured", "strong_secured"):
                self.current_selected_item = None
                self.selectedpasswdm1.setText(f"{item.text()}")
                return

            self.current_selected_item = item
            self.selectedpasswdm1.setText(item.text())
            self.strongpasswdm1.clear()

        def check_m1_revised():
            if self.current_selected_item is None:
                return

            user_pass = self.strongpasswdm1.text().strip()
            if user_pass == "":
                return

            if is_strong(user_pass):
                if self.current_selected_item.data(QtCore.Qt.ItemDataRole.UserRole) == "weak_unsecured":
                    
                    self.fixed_count_m1 += 1
                    
                    self.current_selected_item.setData(QtCore.Qt.ItemDataRole.UserRole, "secured")
                    self.current_selected_item.setText(f"{user_pass}")
                    self.label_3.setText(
                        f"<html><body><p align='center'><span style='font-size:26pt; color:#ffffff;'>PASSWORD REINFORCED!</span></p></body></html>"
                    )
                    
                    self.selectedpasswdm1.setText(f"Password reinforced: {user_pass}")
                    self.current_selected_item = None
                    self.strongpasswdm1.clear()
                    
                    if self.fixed_count_m1 == self.total_required_fixes:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setWindowTitle("Mission Complete")
                        msg.setText("All weak credentials fixed. Proceed to Next Mission.")
                        msg.setStyleSheet("QLabel { color: white; font-size: 18px; } QMessageBox { background-color: #1a1a1a; }")
                        msg.exec()
                        self.pushButton_5.setEnabled(True)
                else:
                    pass

            else:
                self.dispstrength.setStyleSheet("color: red; font-size: 22px;")
                self.dispstrength.setText("Strength: WEAK. Must contain: 8+ chars, U/L case, digit, special char.")

        self.password_list_widget.itemClicked.connect(select_password_m1)
        self.pushButton.clicked.connect(check_m1_revised)
        self.pushButton_5.setEnabled(False)

        # =========================================================
        # MISSION 2 SETUP 
        # =========================================================
        self.m2 = QtWidgets.QWidget()
        self.m2.setObjectName("m2")
        self.label_13 = QtWidgets.QLabel(parent=self.m2)
        self.label_13.setGeometry(QtCore.QRect(350, 0, 411, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.m2)
        self.label_14.setGeometry(QtCore.QRect(100, 30, 931, 131))
        self.label_14.setScaledContents(False)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(parent=self.m2)
        self.label_17.setGeometry(QtCore.QRect(120, 180, 391, 51))
        self.label_17.setStyleSheet("background-color: #1a1a1a")
        self.label_17.setObjectName("label_17")
        self.encptmsgm2 = QtWidgets.QLabel(parent=self.m2)
        self.encptmsgm2.setGeometry(QtCore.QRect(120, 240, 410, 41))
        self.encptmsgm2.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 19px; }")
        self.encptmsgm2.setText("")
        self.encptmsgm2.setObjectName("encptmsgm2")
        self.label_18 = QtWidgets.QLabel(parent=self.m2)
        self.label_18.setGeometry(QtCore.QRect(610, 180, 391, 51))
        self.label_18.setStyleSheet("background-color: #1a1a1a")
        self.label_18.setObjectName("label_18")
        self.comboBox = QtWidgets.QComboBox(parent=self.m2)
        self.comboBox.setGeometry(QtCore.QRect(710, 240, 211, 41))
        self.comboBox.setStyleSheet(" background-color: #5C5C5C; font-size: 18px; border: 2px solid white; border-radius: 6px; color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Caesar shift")
        self.comboBox.addItem("ROT13")
        self.comboBox.setCurrentText("Caesar shift") 
        self.label_19 = QtWidgets.QLabel(parent=self.m2)
        self.label_19.setGeometry(QtCore.QRect(660, 300, 221, 41))
        self.label_19.setStyleSheet("background-color: #1a1a1a")
        self.label_19.setObjectName("label_19")
        self.shiftm2 = QtWidgets.QLineEdit(parent=self.m2)
        self.shiftm2.setGeometry(QtCore.QRect(880, 310, 51, 31))
        self.shiftm2.setStyleSheet("background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px;")
        self.shiftm2.setObjectName("shiftm2")
        self.label_20 = QtWidgets.QLabel(parent=self.m2)
        self.label_20.setGeometry(QtCore.QRect(120, 360, 391, 51))
        self.label_20.setStyleSheet("background-color: #1a1a1a")
        self.label_20.setObjectName("label_20")
        self.decrypmsgm2 = QtWidgets.QLineEdit(parent=self.m2)
        self.decrypmsgm2.setGeometry(QtCore.QRect(120, 420, 410, 41))
        self.decrypmsgm2.setStyleSheet("background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px;")
        self.decrypmsgm2.setObjectName("decrypmsgm2")
        self.checkm2 = QtWidgets.QPushButton(parent=self.m2)
        self.checkm2.setGeometry(QtCore.QRect(550, 420, 151, 41))
        self.checkm2.setObjectName("checkm2")
        self.nextm2 = QtWidgets.QPushButton(parent=self.m2)
        self.nextm2.setGeometry(QtCore.QRect(790, 420, 211, 41))
        self.nextm2.setObjectName("nextm2")
        self.dispm2 = QtWidgets.QLabel(parent=self.m2)
        self.dispm2.setGeometry(QtCore.QRect(130, 480, 391, 21))
        self.dispm2.setObjectName("dispm2")
        self.dispm2.setStyleSheet("font-size: 18px; color: red;")
        self.checkm2.setStyleSheet(common_button_style)
        self.nextm2.setStyleSheet(common_button_style)
        self.stackedWidget.addWidget(self.m2)

        # MISSION 2 LOGIC
        self.original_msg_m2 = "Black cypher ready. Breach Nexus ongoing"
        self.default_shift_m2 = 3
        self.shiftm2.setText(str(self.default_shift_m2))
        self.nextm2.setEnabled(False)

        def update_encrypted_message_m2():
            cipher = self.comboBox.currentText()
            text_to_encrypt = self.original_msg_m2
            
            if cipher == "Caesar shift":
                self.shiftm2.setEnabled(True)
                try:
                    shift = int(self.shiftm2.text())
                    shift = shift % 26 
                    if shift < 1 or shift > 25:
                        shift = self.default_shift_m2
                except ValueError:
                    shift = self.default_shift_m2
                encrypted = caesar_encrypt(text_to_encrypt, shift)
            else:
                self.shiftm2.setEnabled(False)
                encrypted = rot13(text_to_encrypt)
            
            self.encptmsgm2.setText(encrypted)
            self.dispm2.setText("")

        def check_decryption_m2():
            cipher = self.comboBox.currentText()
            encrypted = self.encptmsgm2.text()
            attempt = self.decrypmsgm2.text().strip()
            correct = ""
            
            if cipher == "Caesar shift":
                try:
                    shift = int(self.shiftm2.text())
                    shift = shift % 26
                except ValueError:
                    self.dispm2.setText("<span style='color:red;'>Invalid shift value.</span>")
                    return
                correct = caesar_decrypt(encrypted, shift)
            else:
                correct = rot13(encrypted)

            if attempt == correct:
                self.dispm2.setText("<span style='color:#00FFFF; font-weight:bold;'>Decryption successful!</span>")
                self.nextm2.setEnabled(True)
            else:
                self.dispm2.setText("<span style='color:red;'>Wrong. Try again.</span>")
                self.nextm2.setEnabled(False)

        self.comboBox.currentIndexChanged.connect(update_encrypted_message_m2)
        self.shiftm2.textChanged.connect(update_encrypted_message_m2)
        self.checkm2.clicked.connect(check_decryption_m2)
        update_encrypted_message_m2()

        # MISSION 3 SETUP
        # =========================================================
        self.m3 = QtWidgets.QWidget()
        self.m3.setObjectName("m3")
        self.label_21 = QtWidgets.QLabel(parent=self.m3)
        self.label_21.setGeometry(QtCore.QRect(350, 0, 431, 31))
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(parent=self.m3)
        self.label_23.setGeometry(QtCore.QRect(90, 30, 951, 131))
        self.label_23.setScaledContents(False)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.label_6 = QtWidgets.QLabel(parent=self.m3)
        self.label_6.setGeometry(QtCore.QRect(90, 160, 951, 391))
        self.label_6.setStyleSheet("background-color:#1a1a1a ;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        
        # --- MISSION 3: QTableWidget Implementation ---
        LOG_DATA = [
            {"ts": "09:44:19", "user": "system", "ip": "10.0.0.9", "status": "Success", "details": "System diagnostics", "is_intruder": False},
            {"ts": "09:45:03", "user": "admin", "ip": "185.14.32.91", "status": "Failed", "details": "Wrong password attempt", "is_intruder": True},
            {"ts": "09:45:04", "user": "admin", "ip": "185.14.32.91", "status": "Failed", "details": "Wrong password attempt", "is_intruder": True},
            {"ts": "09:45:06", "user": "admin", "ip": "185.14.32.91", "status": "Success", "details": "Possible brute-force", "is_intruder": True},
            {"ts": "09:46:10", "user": "guest", "ip": "203.0.113.45", "status": "Failed", "details": "Account disabled", "is_intruder": True},
            {"ts": "09:47:22", "user": "root", "ip": "91.204.56.12", "status": "Success", "details": "Unauthorized access", "is_intruder": True},
            {"ts": "09:47:55", "user": "admin", "ip": "192.168.1.8", "status": "Success", "details": "Login OK", "is_intruder": False},
        ]

        self.intrusion_table = QtWidgets.QTableWidget(parent=self.m3)
        self.intrusion_table.setGeometry(QtCore.QRect(110, 170, 741, 300))
        self.intrusion_table.setColumnCount(6) 
        self.intrusion_table.setRowCount(len(LOG_DATA))
        self.intrusion_table.setHorizontalHeaderLabels(["Access", "Timestamp", "Username", "IP Address", "Status", "Details"])
        self.intrusion_table.setStyleSheet("""
            QTableWidget { background-color: #2a2a2a; color: white; gridline-color: #5C5C5C; font-size: 16pt; border-radius: 6px; }
            QHeaderView::section { background-color: #00ffff; color: black; font-weight: bold; padding: 4px; }
        """)
        self.intrusion_table.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.intrusion_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        for row, data in enumerate(LOG_DATA):
            access_widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(access_widget)
            checkbox = QtWidgets.QCheckBox()
            checkbox.setChecked(False) 
            checkbox.setProperty("is_intruder", data["is_intruder"])
            
            layout.addWidget(checkbox)
            layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.intrusion_table.setCellWidget(row, 0, access_widget)
            
            def create_item(text):
                item = QtWidgets.QTableWidgetItem(text)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                return item

            self.intrusion_table.setItem(row, 1, create_item(data["ts"]))
            self.intrusion_table.setItem(row, 2, create_item(data["user"]))
            self.intrusion_table.setItem(row, 3, create_item(data["ip"]))
            status_item = create_item(data["status"])
            if data["is_intruder"]:
                status_item.setFont(QtGui.QFont("Segoe UI", 10, QtGui.QFont.Weight.Bold))
            self.intrusion_table.setItem(row, 4, status_item)
            self.intrusion_table.setItem(row, 5, create_item(data["details"]))

        self.dispm3 = QtWidgets.QLabel(parent=self.m3)
        self.dispm3.setGeometry(QtCore.QRect(110, 480, 741, 31))
        self.dispm3.setStyleSheet("color: #00ffff; font-size: 19px;")
        self.dispm3.setText("All connections DENIED. Check to grant access to legitimate IPs only.")
        self.dispm3.setObjectName("dispm3")

        def check_m3_logic():
            correct = True
            
            for row in range(self.intrusion_table.rowCount()):
                cell_widget = self.intrusion_table.cellWidget(row, 0)
                checkbox = cell_widget.findChild(QtWidgets.QCheckBox)

                is_intruder = checkbox.property("is_intruder")
                is_checked = checkbox.isChecked()

                if is_intruder:
                    if is_checked:
                        correct = False
                        break
                else:
                    if not is_checked:
                        correct = False
                        break

            if correct:
                self.dispm3.setText(f"<span style='color: #00ffff;'>Legitimate connections granted, Intruder access DENIED. Mission Complete.</span>")
                self.nextm3.setEnabled(True)
            else:
                self.dispm3.setText("<span style='color: red;'>FAILED: Ensure access is GRANTED to ONLY the legitimate system IPs.</span>")
                self.nextm3.setEnabled(False)
        
        self.checkm3 = QtWidgets.QPushButton(parent=self.m3)
        self.checkm3.setGeometry(QtCore.QRect(870, 170, 151, 41))
        self.checkm3.setObjectName("checkm3")
        self.checkm3.clicked.connect(check_m3_logic)
        self.checkm3.setText("GRANT")
        
        self.nextm3 = QtWidgets.QPushButton(parent=self.m3)
        self.nextm3.setGeometry(QtCore.QRect(870, 490, 151, 41))
        self.nextm3.setObjectName("nextm3")
        self.nextm3.setEnabled(False) 
        
        self.checkm3.setStyleSheet(common_button_style)
        self.nextm3.setStyleSheet(common_button_style)
        
        self.stackedWidget.addWidget(self.m3)

        # MISSION 4 - INTRO
        # =========================================================
        self.m4 = QtWidgets.QWidget()
        self.m4.setObjectName("m4")
        self.label_26 = QtWidgets.QLabel(parent=self.m4)
        self.label_26.setGeometry(QtCore.QRect(260, 0, 541, 31))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.m4)
        self.label_27.setGeometry(QtCore.QRect(60, 60, 991, 161))
        self.label_27.setScaledContents(False)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.m4)
        self.label_28.setGeometry(QtCore.QRect(60, 250, 991, 231))
        self.label_28.setScaledContents(False)
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.readyp1 = QtWidgets.QPushButton(parent=self.m4)
        self.readyp1.setGeometry(QtCore.QRect(470, 480, 151, 41))
        self.readyp1.setObjectName("readyp1")
        self.readyp1.setStyleSheet(common_button_style)
        self.stackedWidget.addWidget(self.m4)

        # MISSION 4 - PHASE 1
        # =========================================================
        self.m4phase1 = QtWidgets.QWidget()
        self.m4phase1.setObjectName("m4phase1")
        self.nextm4p1 = QtWidgets.QPushButton(parent=self.m4phase1)
        self.nextm4p1.setGeometry(QtCore.QRect(830, 490, 151, 41))
        self.nextm4p1.setObjectName("nextm4p1")
        self.label_29 = QtWidgets.QLabel(parent=self.m4phase1)
        self.label_29.setGeometry(QtCore.QRect(470, 10, 141, 31))
        self.label_29.setObjectName("label_29")
        self.cpuload = QtWidgets.QLabel(parent=self.m4phase1)
        self.cpuload.setGeometry(QtCore.QRect(250, 90, 251, 31))
        self.cpuload.setObjectName("cpuload")
        self.memload = QtWidgets.QLabel(parent=self.m4phase1)
        self.memload.setGeometry(QtCore.QRect(250, 140, 241, 41))
        self.memload.setObjectName("memload")
        self.trafficl = QtWidgets.QLabel(parent=self.m4phase1)
        self.trafficl.setGeometry(QtCore.QRect(250, 200, 231, 41))
        self.trafficl.setObjectName("trafficl")
        self.intchk = QtWidgets.QLabel(parent=self.m4phase1)
        self.intchk.setGeometry(QtCore.QRect(250, 260, 241, 41))
        self.intchk.setObjectName("intchk")
        self.firewallstat = QtWidgets.QLabel(parent=self.m4phase1)
        self.firewallstat.setGeometry(QtCore.QRect(250, 320, 271, 31))
        self.firewallstat.setObjectName("firewallstat")
        self.stableml = QtWidgets.QLabel(parent=self.m4phase1)
        self.stableml.setGeometry(QtCore.QRect(690, 90, 181, 41))
        self.stableml.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 16px; }")
        self.stableml.setObjectName("stableml")
        self.stabletl = QtWidgets.QLabel(parent=self.m4phase1)
        self.stabletl.setGeometry(QtCore.QRect(690, 160, 181, 41))
        self.stabletl.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 16px; }")
        self.stabletl.setObjectName("stabletl")
        self.stableic = QtWidgets.QLabel(parent=self.m4phase1)
        self.stableic.setGeometry(QtCore.QRect(690, 230, 181, 41))
        self.stableic.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 16px; }")
        self.stableic.setObjectName("stableic")
        self.stable_reboot = QtWidgets.QLabel(parent=self.m4phase1)
        self.stable_reboot.setGeometry(QtCore.QRect(690, 300, 181, 41)) 
        self.stable_reboot.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 16px; }")
        self.stable_reboot.setObjectName("stable_reboot")
        self.stable_quarantine = QtWidgets.QLabel(parent=self.m4phase1)
        self.stable_quarantine.setGeometry(QtCore.QRect(690, 370, 181, 41)) 
        self.stable_quarantine.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 16px; }")
        self.stable_quarantine.setObjectName("stable_quarantine")
        self.comb = QtWidgets.QLineEdit(parent=self.m4phase1)
        self.comb.setGeometry(QtCore.QRect(490, 430, 391, 41))
        self.comb.setStyleSheet("background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px;")
        self.comb.setObjectName("comb")
        self.firewallstat_2 = QtWidgets.QLabel(parent=self.m4phase1)
        self.firewallstat_2.setGeometry(QtCore.QRect(260, 430, 221, 31))
        self.firewallstat_2.setObjectName("firewallstat_2")
        self.checkm4p1 = QtWidgets.QPushButton(parent=self.m4phase1)
        self.checkm4p1.setGeometry(QtCore.QRect(250, 490, 151, 41))
        self.checkm4p1.setObjectName("checkm4p1")
        self.disp = QtWidgets.QLabel(parent=self.m4phase1)
        self.disp.setGeometry(QtCore.QRect(430, 500, 391, 21))
        self.disp.setObjectName("disp")
        self.disp.setStyleSheet("font-size: 16px; color: red;")
        self.checkm4p1.setStyleSheet(common_button_style)
        self.nextm4p1.setStyleSheet(common_button_style)
        self.nextm4p1.setEnabled(False)

        correct_map = {
            "1": "D",  # CPU Overload → REBOOT
            "2": "A",  # Memory Leak → REPAIR
            "3": "B",  # Traffic Spike → PURGE
            "4": "C",  # Integrity Error → ISOLATE
            "5": "E"   # Firewall Breach → QUARANTINE
        }

        def check_m4p1_logic():
            user_input = self.comb.text().replace(" ", "").upper()
            pairs = [p for p in user_input.split(",") if p]
            
            if not all(len(pair) == 2 for pair in pairs):
                setattr(self, 'mission_done', False)
                self.disp.setText("<span style='color:red;'>Input format error. Use: 1A,2B,3C,4D,5E</span>")
                self.nextm4p1.setEnabled(False)
                return

            correct = all(
                pair[0] in correct_map and correct_map[pair[0]] == pair[1]
                for pair in pairs
            )

            mission_done = correct and len(pairs) == len(correct_map)
            setattr(self, 'mission_done', mission_done) 

            if mission_done:
                self.disp.setText("<span style='color:#00FFFF;'>All correct! Great job! Continue with the next phase</span>")
                self.nextm4p1.setEnabled(True)
            else:
                self.disp.setText("<span style='color:red;'>Some answers are wrong or incomplete!</span>")
                self.nextm4p1.setEnabled(False)

        self.checkm4p1.clicked.connect(check_m4p1_logic)
        self.stackedWidget.addWidget(self.m4phase1)
        

        self.m4phase2 = QtWidgets.QWidget()
        self.m4phase2.setObjectName("m4phase2")
        self.label_31 = QtWidgets.QLabel(parent=self.m4phase2)
        self.label_31.setGeometry(QtCore.QRect(130, 150, 321, 51))
        self.label_31.setStyleSheet("background-color: #1a1a1a")
        self.label_31.setObjectName("label_31")
        self.passwd_p2 = QtWidgets.QLineEdit(parent=self.m4phase2)
        self.passwd_p2.setGeometry(QtCore.QRect(480, 160, 421, 41))
        self.passwd_p2.setStyleSheet("background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px;")
        self.passwd_p2.setObjectName("passwd_p2")
        
        # MODIFICATION: Changed checkp2 button text/functionality
        self.checkp2 = QtWidgets.QPushButton(parent=self.m4phase2)
        self.checkp2.setGeometry(QtCore.QRect(470, 420, 300, 41)) # Adjusted size
        self.checkp2.setObjectName("checkp2")
        
        self.label_32 = QtWidgets.QLabel(parent=self.m4phase2)
        self.label_32.setGeometry(QtCore.QRect(140, 320, 391, 51))
        self.label_32.setStyleSheet("background-color: #1a1a1a")
        self.label_32.setObjectName("label_32")
        
        # MODIFICATION: Changed encrptpasswd from QLineEdit to QLabel
        self.encrptpasswd = QtWidgets.QLabel(parent=self.m4phase2)
        self.encrptpasswd.setGeometry(QtCore.QRect(560, 330, 351, 41))
        self.encrptpasswd.setStyleSheet("QLabel { background-color: #2a2a2a; border: 2px solid #00ffff; border-radius: 6px; color: #00ffff; font-size: 22px; padding-left: 10px; }")
        self.encrptpasswd.setText("Encrypted result will appear here.")
        self.encrptpasswd.setObjectName("encrptpasswd")
        
        self.cipherp2 = QtWidgets.QLabel(parent=self.m4phase2)
        self.cipherp2.setGeometry(QtCore.QRect(290, 240, 281, 41))
        self.cipherp2.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px; }")
        self.cipherp2.setText("")
        self.cipherp2.setObjectName("cipherp2")
        self.label_33 = QtWidgets.QLabel(parent=self.m4phase2)
        self.label_33.setGeometry(QtCore.QRect(140, 240, 121, 51))
        self.label_33.setStyleSheet("background-color: #1a1a1a")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(parent=self.m4phase2)
        self.label_34.setGeometry(QtCore.QRect(610, 230, 101, 51))
        self.label_34.setStyleSheet("background-color: #1a1a1a")
        self.label_34.setObjectName("label_34")
        self.shiftp2 = QtWidgets.QLabel(parent=self.m4phase2)
        self.shiftp2.setGeometry(QtCore.QRect(740, 240, 161, 41))
        self.shiftp2.setStyleSheet("QLabel { background-color: #5C5C5C; border: 2px solid white; border-radius: 6px; color: white; font-size: 22px; }")
        self.shiftp2.setText("")
        self.shiftp2.setObjectName("shiftp2")
        self.label_35 = QtWidgets.QLabel(parent=self.m4phase2)
        self.label_35.setGeometry(QtCore.QRect(30, 70, 1051, 51))
        self.label_35.setStyleSheet("background-color: #1a1a1a")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(parent=self.m4phase2)
        self.label_36.setGeometry(QtCore.QRect(450, 0, 161, 51))
        self.label_36.setStyleSheet("background-color: #1a1a1a")
        self.label_36.setObjectName("label_36")
        
        # --- REMOVED HOME BUTTON CREATION (self.home) ---
        
        self.disp_m4p2 = QtWidgets.QLabel(parent=self.m4phase2)
        self.disp_m4p2.setGeometry(QtCore.QRect(370, 380, 391, 21))
        self.disp_m4p2.setObjectName("disp_m4p2")
        self.disp_m4p2.setStyleSheet("font-size: 18px; color: red;")
        
        self.checkp2.setStyleSheet(common_button_style)
        # --- REMOVED HOME BUTTON STYLE (self.home.setStyleSheet) ---
        self.stackedWidget.addWidget(self.m4phase2)

        # MISSION 4 PHASE 2 LOGIC
        def generate_cipher_m4p2():
            cipher_choice = random.choice(["ROT13", "CAESAR"])
            self.cipherp2.setText(cipher_choice)

            if cipher_choice == "ROT13":
                self.shiftp2.setText("13")
                self.shift_val_m4p2 = 13
            else:
                shift = random.randint(1, 25)
                self.shiftp2.setText(str(shift))
                self.shift_val_m4p2 = shift
        
        def show_status_m4p2(text, color):
            self.disp_m4p2.setText(text)
            self.disp_m4p2.setStyleSheet(f"font-size: 16px; color: {color};")
            

        def mission_complete_dialog(self):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("MISSION COMPLETE")
            msg.setText("""
            <p style="font-size:20px; font-weight:600; color:white; text-align:center;">
            Black Cypher has fallen.
            The Nexus Engine holds steady.
            Your vigilance saved Aethel Corp—another win for CyberSentinel Operations.
            </p>
            """)
            msg.setStyleSheet("""
                QLabel { color: white; font-size: 18px; }
                QMessageBox { background-color: #1a1a1a; }
            """)
            pix = QtGui.QPixmap("D:/Studies/Computer/CyberSentinal/Images/badge.png")
            if not pix.isNull():
                msg.setIconPixmap(pix.scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
            else:
                print("IMAGE FAILED TO LOAD")
            exit_btn = msg.addButton("EXIT", QtWidgets.QMessageBox.ButtonRole.AcceptRole)
            msg.exec()

            if msg.clickedButton() == exit_btn:
                QtWidgets.QApplication.quit()
            

        # NEW FUNCTION: Handles live encryption preview as user types
        def live_encrypt_m4p2():
            password = self.passwd_p2.text()
            cipher_text = self.cipherp2.text()

            self.disp_m4p2.clear()
            
            if not password:
                self.encrptpasswd.setText("Encrypted result will appear here.")
                return

            encrypted_result = ""
            
            if cipher_text == "ROT13":
                encrypted_result = rot13(password)
            else:
                encrypted_result = caesar_encrypt(password, self.shift_val_m4p2)
            
            self.encrptpasswd.setText(encrypted_result)

        def set_password_m4p2():
            password = self.passwd_p2.text().strip()

            if not password:
                show_status_m4p2("Password field cannot be empty!", "red")
                return
            
            if not is_strong(password):
                show_status_m4p2("The password must be STRONG!", "red")
                return

            show_status_m4p2("Password has been set successfully and secured!", "#00FFFF")
            mission_complete_dialog(self)

        def enter_m4p2():
            generate_cipher_m4p2()
            self.disp_m4p2.clear()
            self.passwd_p2.clear()
            self.encrptpasswd.setText("Encrypted result will appear here.")

        self.passwd_p2.textChanged.connect(live_encrypt_m4p2)

        self.checkp2.clicked.connect(set_password_m4p2) 

        # FINAL CONNECTIONS AND RETRANSLATE
        # =========================================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1446, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # M1 → M2
        self.nextm2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))        # M2 → M3
        self.nextm3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))        # M3 → M4 Main
        self.readyp1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))       # M4 Main → M4P1
        self.nextm4p1.clicked.connect(lambda: (
            self.stackedWidget.setCurrentIndex(5), 
            enter_m4p2()
        ) if getattr(self, 'mission_done', False) 
        else self.disp.setText("Mission not done yet!"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cyber Sentinel: The Nexus Defense"))
        # M1 Texts
        self.label_3.setText(_translate("MainWindow", "<html><body><p align='center'><span style='font-size:26pt; color:#ffffff;'>SELECTED PASSWORD:</span></p><p align='center'><span style='font-size:18pt; color:#ffffff;'>0 / 3 required</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">CHANGE PASSWORD:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CHANGE"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Objective:</span><span style=\" font-size:14pt; color:#ffffff;\"> Strengthen Aethel Corp’s weak passwords before the breach spreads. </span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">HQ BRIEFING:</span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">“Agent, our first scans show multiple employees using weak credentials. Identify the weak passwords and reinforce them immediately.” </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">MISSION 1 — Operation: Lockdown</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "NEXT MISSION"))

        # M2 Texts
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">MISSION 2 — Codebreaker Protocol</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Objective:</span><span style=\" font-size:14pt; color:#ffffff;\"> Decrypt the enemy’s secret message. </span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">HQ BRIEFING:</span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">&quot;We’ve captured an encrypted data stream from the attackers.<br />Use the decryption terminal. Identify the cipher — Caesar or ROT13 — and reveal their plans.” </span></p>\n<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">ENCRYPTED MESSAGE:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">CHOOSE CIPHER:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Caesar shift"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ROT13"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">SHIFT VALUE:</span></p><p align=\"center\"><span style=\" font-size:26pt;\"><br/></p></body></html>"))
        self.shiftm2.setPlaceholderText(_translate("MainWindow", "1-25"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">DECRYPTED MESSAGE:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.checkm2.setText(_translate("MainWindow", "CHECK"))
        self.nextm2.setText(_translate("MainWindow", "NEXT MISSION"))

        # M3 Texts
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">MISSION 3 — Operation </span><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:18pt; font-weight:700; color:#ffffff;\">ShadowScan</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Objective:</span><span style=\" font-size:14pt; color:#ffffff;\"> Isolate all unauthorized access and whitelist critical system activity. </span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">HQ BRIEFING:</span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">“Logs indicate multiple hostiles. Use the Zero Trust firewall to DENY all access by default. You must manually GRANT access to only the known, safe system IPs.” </span></p></body></html>"))
        self.checkm3.setText(_translate("MainWindow", "GRANT"))
        self.nextm3.setText(_translate("MainWindow", "NEXT"))

        # M4 Intro Texts
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">MISSION 4 —</span><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:18pt; font-weight:700; color:#ffffff;\">Final Firewall: The Nexus Defense</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Objective:</span></p>\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:14pt; color:#ffffff;\">Block malicious traffic, reinforce encryption, and secure the Nexus Engine.</span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\"> Every mission you completed has led to this moment.If we fail now, the entire system falls into Black Cypher’s hands.</span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">    Hold the line, Analyst.Defend the Nexus. Finish this.</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\nhr { height: 1px; border-width: 0; }\nli.unchecked::marker { content: \"\\2610\"; }\nli.checked::marker { content: \"\\2612\"; }\n</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">PHASE 1 — SYSTEM STABILIZATION</span><span style=\" font-size:14pt; color:#ffffff;\"><br />Incoming anomalies detected in: </span><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">CPU, Memory, Traffic, Integrity, Firewall</span><span style=\" font-size:14pt; color:#ffffff;\">.<br />Match each anomaly with the correct fix.</span></p>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">PHASE 2 — PASSWORD REINFORCEMENT</span><span style=\" font-size:14pt; color:#ffffff;\"><br />Enter a new strong password and encrypt it using the given cipher to safely close the nexus.</span></p></body></html>"))
        self.readyp1.setText(_translate("MainWindow", "READY"))

        self.nextm4p1.setText(_translate("MainWindow", "NEXT"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:24pt; font-weight:700; color:#ffffff;\">PHASE 1</span></p></body></html>"))
        self.cpuload.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:24pt; font-weight:700; color:#ffffff;\">1.CPU Overload</span></p></body></html>"))
        self.memload.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:24pt; font-weight:700; color:#ffffff;\">2.Memory Leak</span></p></body></html>"))
        self.trafficl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:24pt; font-weight:700; color:#ffffff;\">3.Traffic Spike</span></p></body></html>"))
        self.intchk.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:24pt; font-weight:700; color:#ffffff;\">4.Integrity Error</span></p></body></html>"))
        self.firewallstat.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:24pt; font-weight:700; color:#ffffff;\">5.Firewall Breach</span></p></body></html>"))

        self.stable_quarantine.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:17pt; font-weight:700; color:#ffffff;\">e.QUARANTINE</span></p><p><br/></p></body></html>"))
        self.stable_reboot.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:20pt; font-weight:700; color:#ffffff;\">d.REBOOT</span></p><p><br/></p></body></html>"))
        self.stableml.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:20pt; font-weight:700; color:#ffffff;\">a.REPAIR</span></p></body></html>"))
        self.stabletl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:20pt; font-weight:700; color:#ffffff;\">b.PURGE</span></p></body></html>"))
        self.stableic.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:20pt; font-weight:700; color:#ffffff;\">c.ISOLATE</span></p></body></html>"))
        
        self.comb.setPlaceholderText(_translate("MainWindow", "Enter 1A,2B,3C,4D,5E"))
        self.firewallstat_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Aptos\',\'sans-serif\'; font-size:22pt; font-weight:700; color:#ffffff;\">COMBINATION:</span></p></body></html>"))
        self.checkm4p1.setText(_translate("MainWindow", "CHECK"))

        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">ENTER PASSWORD:</span></p><p align=\"center\"><br/></p></body></html>"))

        self.checkp2.setText(_translate("MainWindow", "SET PASSWORD"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">ENCRYPTED PASSWORD:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">CIPHER:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">SHIFT:</span></p><p align=\"center\"><br/></p></body></html>"))

        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">To stop further intrusion, you must create a new strong password and encrypt it using the specified cipher to safely seal the Nexus Engine.</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">PHASE 2</span></p><p align=\"center\"><br/></p></body></html>"))
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

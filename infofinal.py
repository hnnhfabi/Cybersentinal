import sys
import warnings
from PyQt6 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets

warnings.filterwarnings("ignore", category=DeprecationWarning)

VIDEO_PATH = r"D:\Studies\Computer\CyberSentinal\Images\key video.mp4"  # update if needed


# ----------------------------
# Collapsible Panel Class
# ----------------------------
class CollapsiblePanel(QtWidgets.QWidget):
    def __init__(self, title, content, color="#00334d"):
        super().__init__()

        # Toggle button for section title
        self.toggle_btn = QtWidgets.QToolButton(text=title, checkable=True, checked=False)
        self.toggle_btn.setStyleSheet(f"""
            QToolButton {{
                background-color: {color};
                color: white;
                font-weight: bold;
                font-size: 18px;
                border-radius: 10px;
                padding: 10px;
            }}
            QToolButton:hover {{
                background-color: #00ffff;
                color: black;
            }}
        """)
        self.toggle_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toggle_btn.setArrowType(QtCore.Qt.ArrowType.RightArrow)
        self.toggle_btn.clicked.connect(self.toggle_content)

        # Inner content — no nested scrollbars
        self.content_widget = QtWidgets.QWidget()
        label = QtWidgets.QLabel(content)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        label.setMinimumWidth(1200)  # widen to push text right
        label.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        label.setStyleSheet("font-size: 15px; padding: 15px; color: white;")

        layout_inner = QtWidgets.QVBoxLayout(self.content_widget)
        layout_inner.addWidget(label)
        layout_inner.setContentsMargins(20, 5, 60, 5)

        # Container used for animated expand/collapse (no inner scrollbars)
        self.content_area = QtWidgets.QWidget()
        vbox = QtWidgets.QVBoxLayout(self.content_area)
        vbox.addWidget(self.content_widget)
        vbox.setContentsMargins(0, 0, 0, 0)

        # Animation
        self.toggle_animation = QtCore.QParallelAnimationGroup(self)
        self.content_animation = QtCore.QPropertyAnimation(self.content_area, b"maximumHeight")
        self.content_animation.setDuration(400)
        self.content_animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutCubic)
        self.toggle_animation.addAnimation(self.content_animation)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.toggle_btn)
        main_layout.addWidget(self.content_area)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.content_area.setMaximumHeight(0)  # initially collapsed

    def toggle_content(self):
        checked = self.toggle_btn.isChecked()
        self.toggle_btn.setArrowType(
            QtCore.Qt.ArrowType.DownArrow if checked else QtCore.Qt.ArrowType.RightArrow
        )
        content_height = self.content_widget.sizeHint().height()
        self.content_animation.setStartValue(self.content_area.maximumHeight())
        self.content_animation.setEndValue(content_height if checked else 0)
        self.toggle_animation.start()


# ----------------------------
# Main Training Deck Window
# ----------------------------
class TrainingDeckWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 CyberSentinel Training Database")
        self.showFullScreen()
        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
                color: white;
                font-family: 'Consolas';
            }
            QLabel#title {
                font-size: 34px;
                font-weight: bold;
                color: #00ffff;
            }
            QLabel#subtitle {
                font-size: 18px;
                color: #bbbbbb;
                padding-bottom: 20px;
            }
            QPushButton#readybtn {
                background-color: #00ffff;
                border-radius: 8px;
                color: #0d1f15;
                font-weight: bold;
                font-size: 16px;
                padding: 8px 16px;
            }
            QPushButton#readybtn:hover {
                background-color: #33ffff;
            }
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(15)

        # Header
        title = QtWidgets.QLabel("🧠 CyberSentinel Training Database", objectName="title")
        subtitle = QtWidgets.QLabel("Essential knowledge for every Security Analyst.", objectName="subtitle")

        # Ready button
        readybtn = QtWidgets.QPushButton("Ready", objectName="readybtn")
        readybtn.setFixedHeight(40)
        readybtn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        readybtn.clicked.connect(self.open_mission_window)

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(readybtn)

        layout.addLayout(header_layout)
        layout.addWidget(subtitle)

        # Single scroll area for all content
        scroll = QtWidgets.QScrollArea()
        scroll.setStyleSheet("border: none;")
        scroll.setWidgetResizable(True)
        content_widget = QtWidgets.QWidget()
        content_layout = QtWidgets.QVBoxLayout(content_widget)
        content_layout.setSpacing(12)

        sections = [
            ("SECTION 1 — Password Security",
             "Strong passwords protect against brute-force and guessing attacks.\n"
             "Use at least 8–12 characters, include symbols, and avoid personal info.",
             "#00334d"),

            ("SECTION 2 — Ciphers & Encryption",
             "Encryption is the process of converting readable text (plaintext) into unreadable text (ciphertext).\n\n"
             "🔹 Caesar Cipher — One of the oldest encryption techniques. \nEach letter in the plaintext is shifted by a fixed number of positions.\n"
             "Example: shift by 3 → A → D, B → E, etc.\n\n"
             "🔹 ROT13 Cipher — A simple variation of Caesar Cipher that shifts each letter by 13 positions.\n"
             "Because the English alphabet has 26 letters, applying ROT13 twice restores the original text.\n\n"
             "Modern systems use much stronger methods like AES and RSA, but Caesar and ROT13 remain important for \nlearning certain concepts",
             "#001a33"),

            ("SECTION 3 — Log Analysis",
             "Logs record system activity. Analysts examine logs to detect failed logins, privilege escalations,\n and suspicious IP access.\n"
             "Look for repeated failed attempts, login anomalies, and irregular timestamps.",
             "#1a001a"),

            ("SECTION 4 — Firewalls & Network Packets",
             "Firewalls monitor and control incoming and outgoing traffic based on predetermined rules.\n"
             "They help block unauthorized access and mitigate DoS or scanning attacks.\n"
             "Security analysts must recognize port scans, ping floods, and malformed packets.",
             "#006680"),


            ("SECTION 5 — Incident Response",
             "Incident handling follows structured steps:\n"
             "1. Preparation — Establish policies and teams.\n"
             "2. Detection & Analysis — Identify and verify incidents.\n"
             "3. Containment — Limit damage and isolate affected systems.\n"
             "4. Eradication — Remove root cause or malware.\n"
             "5. Recovery — Restore operations.\n"
             "6. Post-Incident Review — Document and improve defenses.",
             "#001a33"),

            ("SECTION 6 — Phishing & Social Engineering",
             "Phishing tricks users into revealing sensitive information by imitating trusted sources.\n"
             "Look for misspelled domains, urgent tones, and unexpected attachments.\n"
             "Always verify the sender’s authenticity before clicking or replying.",
             "#006680"),
            ("SECTION 7 — Security Policies",
             "Policies define expected behavior for users and administrators.\n"
             "Examples include password rotation schedules, device usage rules, and access control procedures.",
             "#1a001a"),

            ("SECTION 8 — Malware & Threat Detection",
             "Malware includes viruses, worms, Trojans, and ransomware.\n"
             "Analysts use sandboxing, signature-based scanning, and behavioral analysis to detect threats.",
             "#00334d"),

            ("SECTION 9 — Node staibility",
             "REPAIR-Fix corruption-Integrity issues, tampering-Unauthorized Modification\n"
             "PURGE-Flush traffic-Packet floods, spikes-Traffic Spike Detected\n"
             "REBOOT-Reset system-CPU/memory overloads-Node Unresponsive\n"
             "ISOLATE-Quarantine-Malware/ rogue processes-Process Infection Detected\n","#00334d"),

            ("SECTION 10 — The Nexus Engine",
             "Aethel Corp’s core defense database, codename Nexus Engine, integrates firewall telemetry and encryption archives.\n"
             "Your mission: ensure no unauthorized access or data leaks occur within its infrastructure.",
             "#0a0033")
        ]

        for title_text, text, color in sections:
            content_layout.addWidget(CollapsiblePanel(title_text, text, color))

        content_layout.addStretch()
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)

    # method must be at class level (not nested inside __init__)
    def open_mission_window(self):
        try:
            from missions import Ui_MainWindow

            # Create real window
            self.mission_window = QtWidgets.QMainWindow()

            # Attach UI
            self.mission_ui = Ui_MainWindow()
            self.mission_ui.setupUi(self.mission_window)

            # Show mission screen
            self.mission_window.show()

            # Hide training deck
            self.hide()

        except Exception as e:
            print("ERROR OPENING MISSION WINDOW:", e)



# ----------------------------
# Flicker-free Loading Screen with black overlay
# ----------------------------
class LoadingScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Initializing CyberSentinel Database...")

        # Force black background immediately
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor("#000000"))
        self.setPalette(palette)
        self.setStyleSheet("background-color: #000000; border: none; border-radius: 12px;")

        # Fixed size for your square video (hardcoded as requested)
        self.setFixedSize(500, 500)

        # Center window on screen
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

        # Layout for video display
        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        # Video widget
        self.video_widget = QtMultimediaWidgets.QVideoWidget(self)
        self.video_widget.setFixedSize(500, 500)
        self.video_widget.setStyleSheet("background-color: black;")
        self.video_widget.setAttribute(QtCore.Qt.WidgetAttribute.WA_OpaquePaintEvent, True)
        layout.addWidget(self.video_widget)

        # Black overlay attached to video_widget (covers video area until first frame is ready)
        self.overlay = QtWidgets.QLabel(self.video_widget)
        self.overlay.setStyleSheet("background-color: black;")
        self.overlay.setGeometry(0, 0, self.video_widget.width(), self.video_widget.height())
        self.overlay.show()

        # Media player
        self.player = QtMultimedia.QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        try:
            self.player.setSource(QtCore.QUrl.fromLocalFile(VIDEO_PATH))
        except Exception:
            # Some Qt builds might expect a different API — but if setSource fails, we'll ignore and still show the loading screen
            pass

        # Try to loop infinitely if API supports it
        try:
            self.player.setLoops(QtMultimedia.QMediaPlayer.Loops.Infinite)
        except Exception:
            # older/newer Qt versions might not have setLoops; ignore
            pass

        # Keep a reference to the overlay animation so it doesn't get GC'd
        self._overlay_anim = None

        # More reliable signal: videoAvailableChanged(bool) — true when a frame can be shown
        try:
            self.player.videoAvailableChanged.connect(self.on_video_available)
        except Exception:
            # fallback: some PyQt6 builds may not expose videoAvailableChanged on player in same way
            try:
                self.player.mediaStatusChanged.connect(self._on_media_status_fallback)
            except Exception:
                pass

        # start playback after a short delay to let window paint
        QtCore.QTimer.singleShot(100, self._safe_player_play)

        # show main after 4s (same as before)
        QtCore.QTimer.singleShot(4000, self.show_main_window)

    def _safe_player_play(self):
        try:
            self.player.play()
        except Exception:
            pass

    def on_video_available(self, available: bool):
        if available:
            # fade overlay out smoothly (store anim on self to avoid GC)
            effect = QtWidgets.QGraphicsOpacityEffect(self.overlay)
            self.overlay.setGraphicsEffect(effect)
            anim = QtCore.QPropertyAnimation(effect, b"opacity", self)
            anim.setDuration(400)
            anim.setStartValue(1.0)
            anim.setEndValue(0.0)
            anim.finished.connect(self.overlay.hide)
            anim.start(QtCore.QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)
            self._overlay_anim = anim

    def _on_media_status_fallback(self, status):
        # fallback handler: remove overlay on common 'Loaded' statuses
        try:
            if status in (
                QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia,
                QtMultimedia.QMediaPlayer.MediaStatus.BufferedMedia,
                QtMultimedia.QMediaPlayer.MediaStatus.StalledMedia,
            ):
                self.on_video_available(True)
        except Exception:
            pass

    def show_main_window(self):
        try:
            self.player.stop()
        except Exception:
            pass
        self.close()
        self.main = TrainingDeckWindow()
        self.main.show()


# ----------------------------
# Main Application
# ----------------------------
def main():
    app = QtWidgets.QApplication(sys.argv)
    splash = LoadingScreen()
    splash.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

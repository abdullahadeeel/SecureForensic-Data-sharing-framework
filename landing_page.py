import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QLabel, QHBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class LandingPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Data Sharing Framework")
        self.resize(1000, 700)

        # Main Layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # UI Elements Setup
        self.setup_layout()
        
        # Connect Buttons to Actions
        self.connect_actions()

        # ============================================================
        # DARK MODE BUTTON SETTING (Yahan add kiya hai)
        # ============================================================
        self.dark_mode_btn.setCheckable(True)
        # Jab button dabega toh app.py ka toggle_theme function call hoga
        self.dark_mode_btn.toggled.connect(self.handle_theme_toggle)

    def handle_theme_toggle(self, checked):
        # Hum check kar rahe hain ke parent (app.py) mein function mojud hai ya nahi
        if hasattr(self.parent(), 'toggle_theme'):
            self.parent().toggle_theme(checked)
            if checked:
                self.dark_mode_btn.setText("Switch to Light Mode")
            else:
                self.dark_mode_btn.setText("Switch to Dark Mode")

    def setup_layout(self):
        # 1. Top Navigation Bar
        nav_layout = QHBoxLayout()
        self.btn_home = QPushButton("Home")
        self.btn_features = QPushButton("Features")
        self.btn_security = QPushButton("Security")
        self.btn_about = QPushButton("About Us")
        
        # DARK MODE BUTTON (Naya Button banaya hai)
        self.dark_mode_btn = QPushButton("Switch to Dark Mode")
        self.dark_mode_btn.setFixedWidth(150)
        self.dark_mode_btn.setStyleSheet("background-color: #f0f0f0; font-weight: bold;")

        nav_layout.addWidget(self.btn_home)
        nav_layout.addWidget(self.btn_features)
        nav_layout.addWidget(self.btn_security)
        nav_layout.addWidget(self.btn_about)
        nav_layout.addStretch() # Space paida karne ke liye
        nav_layout.addWidget(self.dark_mode_btn) # Dark mode button nav bar mein add kiya
        
        self.main_layout.addLayout(nav_layout)

        # 2. Hero Section (Welcome Text)
        self.hero_label = QLabel("Welcome to Secure Forensic Dashboard")
        self.hero_label.setAlignment(Qt.AlignCenter)
        self.hero_label.setStyleSheet("font-size: 28px; font-weight: bold; margin: 40px;")
        self.main_layout.addWidget(self.hero_label)

        # 3. Content Area
        self.content_label = QLabel("Select an option to get started")
        self.content_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.content_label)

    def connect_actions(self):
        self.btn_home.clicked.connect(lambda: self.update_status("Home Clicked"))
        self.btn_features.clicked.connect(lambda: self.update_status("Features Clicked"))

    def update_status(self, text):
        self.content_label.setText(f"{text} - Working!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LandingPage()
    win.show()
    sys.exit(app.exec_())








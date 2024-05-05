import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog, QAction, QMenu
)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 120)
        self.setWindowTitle('Giriş')
        self.setStyleSheet("background-color: #F0F0F0; color: black;")

        layout = QVBoxLayout()

        self.user_label = QLabel("Kullanıcı Adı:")
        self.user_input = QLineEdit()
        self.pass_label = QLabel("Şifre:")
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Giriş Yap")
        self.login_button.setStyleSheet("background-color: #3CB371; color: white;")
        self.login_button.clicked.connect(self.check_credentials)

        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.user_input.text()
        password = self.pass_input.text()

        if username == "maruf" and password == "korkutata":
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.user_label.setText("Hatalı kullanıcı adı veya şifre!")
            self.user_label.setStyleSheet("color: red;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.izlenen_dersler = [] 
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Kültür Üniversitesi Eğitim Platformu')
        self.setStyleSheet("background-color: #F0F0F0; color: black;")

        self.welcome_label = QLabel("Kültür Üniversitesi Eğitim Platformuna Hoş Geldiniz! \nBu Dönemki Dersleriniz", self)
        self.welcome_label.setStyleSheet("color: #3CB371;")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setGeometry(200, 100, 400, 50)
        self.welcome_label.setFont(self.get_font())

        self.dersler_layout = QHBoxLayout()

        
        self.add_dersler()

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.welcome_label)
        self.main_layout.addLayout(self.dersler_layout)

        cikis_button = QPushButton("Çıkış Yap", self)
        cikis_button.setGeometry(300, 500, 200, 50)
        cikis_button.setStyleSheet("background-color: #3CB371; color: white;")
        cikis_button.clicked.connect(self.cikis_yap)
        self.main_layout.addWidget(cikis_button)

        self.create_menu_bar() 

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def get_font(self):
        font = self.font()
        font.setPointSize(15)
        font.setBold(True)
        return font

    def add_dersler(self):
        dersler_sol = [
            {"ders_adi": "Matematik", "ogretmen": "Sawsan Başpınar", "icerik": "Soyut düşünme yeteneğini geliştirmek fen ve sosyal bilimler ilgili matematiksel problemleri çözmek."},
            {"ders_adi": "Fizik", "ogretmen": "Neslihan Fatma Er", "icerik": "Vektörler, moment-denge, ağırlık merkezi, ısı sıcaklık ve genleşme, hareket, iş güç enerji ve itme-momentum."},
            {"ders_adi": "Türkçe", "ogretmen": "Dr. Yakup Türkdil", "icerik": "Türk Dili'nin gramerini, dili etkin bir şekilde konuşma ve yazma."},
            {"ders_adi": "Bilgisayara Giriş I", "ogretmen": "Erdem Yücesan", "icerik": "Bilgisayar okuryazarlığı ile ilgili temel bilgi ve becerileri kazandırmak amaçlanmaktadır."},
            {"ders_adi": "Veri Tabanı ve Yönetimi", "ogretmen": "Muharrem Altunışık", "icerik": "Veritabanı yönetim sistemlerinde temel işlemlerin öğrenilmesi."}
        ]

        dersler_sag = [
            {"ders_adi": "Nesne Tabanlı Programlama", "ogretmen": "Erdem Yücesan", "icerik": "Problem odaklı bir şekilde nesne yönelimli programlamayı (OOP) öğretme."},
            {"ders_adi": "Veri Tabanı Programlama", "ogretmen": "Muharrem Altunisik", "icerik": "Öğrencilerin veri tabanı kavramını ve veri tabanının bir yazılımın temel unsuru olduğunu anlaması."},
            {"ders_adi": "İstatistik ve Olasılık", "ogretmen": "Yeliz Sevimli Saitoğlu", "icerik": "Yabancı Dil - temel istatistik kavramlarının öğretilmesi."},
            {"ders_adi": "Görsel Programlama", "ogretmen": "Erdem Yücesan", "icerik": "Görsel programlama dili bilgisinin ve GUI programlama mantığının öğretilmes."},
            {"ders_adi": "Mesleki Yabancı Dil ", "ogretmen": "Petek Sunay", "icerik": "Bilgisayar ve bilişim teknolojisi alanlarında kullanılan ingilizce terminoloji bilgisi."}
        ]

        self.dersler_layout.addWidget(self.create_dersler_widget(dersler_sol))
        self.dersler_layout.addWidget(self.create_dersler_widget(dersler_sag))

    def create_dersler_widget(self, dersler):
        widget = QWidget()
        layout = QVBoxLayout()
        for ders in dersler:
            ders_adi_label = QLabel(f"<b>{ders['ders_adi']}</b>")
            ogretmen_label = QLabel(f"Öğretmen: {ders['ogretmen']}")
            icerik_label = QLabel(f"İçerik: {ders['icerik']}")
            izlemeye_basla_button = QPushButton("İzlemeye Başla")
            izlemeye_basla_button.setStyleSheet("background-color: #3CB371; color: white;")
            izlemeye_basla_button.clicked.connect(lambda checked, ders=ders: self.izlemeye_basla_mesaj(ders))  
            odev_yukle_button = QPushButton("Ödev Yükle")
            odev_yukle_button.setStyleSheet("background-color: #3CB371; color: white;")
            odev_yukle_button.clicked.connect(lambda checked, ders=ders: self.odev_yukle_mesaj(ders))  
            ogretmene_soru_button = QPushButton("Öğretmene Soru Sor")
            ogretmene_soru_button.setStyleSheet("background-color: #3CB371; color: white;")
            ogretmene_soru_button.clicked.connect(self.ogretmene_soru_mesaj)
            layout.addWidget(ders_adi_label)
            layout.addWidget(ogretmen_label)
            layout.addWidget(icerik_label)
            layout.addWidget(izlemeye_basla_button)
            layout.addWidget(ogretmene_soru_button)
            layout.addWidget(odev_yukle_button)
        widget.setLayout(layout)
        return widget

    def izlemeye_basla_mesaj(self, ders):
        ders_adi = ders['ders_adi']
        if ders_adi not in self.izlenen_dersler:
            self.izlenen_dersler.append(ders_adi)
            QMessageBox.information(self, "İzleme Başlatıldı", f"{ders_adi} dersini izlemeye başladınız!")
        else:
            QMessageBox.warning(self, "Ders Zaten İzleniyor", f"{ders_adi} dersini zaten izlidiniz!")

    def odev_yukle_mesaj(self, ders):
        ders_adi = ders['ders_adi']
        QMessageBox.information(self, "Ödev Yükle", f"{ders_adi} dersine ödev yüklendi!")

    def ogretmene_soru_mesaj(self):
        soru, ok = QInputDialog.getText(self, "Öğretmene Soru Sor", "Sorunuzu buraya yazın:")
        if ok:
            QMessageBox.information(self, "Soru Gönderildi", "Sorunuz gönderildi!")

    def cikis_yap(self):
        self.close()

    def create_menu_bar(self):  
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("background-color: #3CB371; color: white;")
        menu_user = menu_bar.addMenu("Kullanıcı Bilgileri")

        action_user_info = QAction("Kullanıcı Bilgileri", self)
        action_user_info.triggered.connect(self.show_user_info)
        menu_user.addAction(action_user_info)

        action_izlenen_dersler = QAction("İzlediğim Dersler", self)
        action_izlenen_dersler.triggered.connect(self.show_izlenen_dersler)
        menu_bar.addAction(action_izlenen_dersler)

    def show_user_info(self):
        QMessageBox.information(self, "Kullanıcı Bilgileri", "Kullanıcı Adı: Maruf Korkutata\nBölüm: Bilgisayar Programcılığı\nOkul Numarası:2300006603\nKullanıcı Mail:2300006603@stu.iku.edu.tr")

    def show_izlenen_dersler(self):
        dersler = "\n".join(self.izlenen_dersler)
        QMessageBox.information(self, "İzlenen Dersler", dersler)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())

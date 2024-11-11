import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from quanlytaichinh_logic import Ui_MainWindow  # Nhập lớp Ui_MainWindow từ file quanlytaichinh.py

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Khởi tạo ứng dụng
    MainWindow = QMainWindow()     # Tạo cửa sổ chính
    ui = Ui_MainWindow()           # Tạo đối tượng giao diện
    ui.setupUi(MainWindow)         # Thiết lập giao diện cho cửa sổ
    MainWindow.show()              # Hiện cửa sổ

    sys.exit(app.exec())           # Chạy vòng lặp sự kiện
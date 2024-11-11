from PySide6.QtCore import Qt,QDate
from PySide6.QtGui import QScreen,QColor,QIcon
from PySide6.QtCore import QTimer, QDateTime

from PySide6.QtWidgets import (QApplication, QMainWindow,QStackedWidget,QWidget
    ,QDialog,QMessageBox, QTableWidgetItem,QTableWidget,QPushButton,QVBoxLayout,QAbstractItemView)

from UI_themchitieu import Ui_Nhapchitieu_Dialog
from UI_quanlytaichinh import Ui_MainWindow
from UI_chinhsua_CT import Ui_chinhsuachitieu_Dialog
from UI_luachon_Table import Ui_luachon_table

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter

import os
import subprocess
import sys
###############################################################################################################################################
class MyProgram (QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("WalletCare")    # Tên chương trình

        # Đặt biểu tượng cho ứng dụng
        icon_path = 'icon/iconApp.png'  # Đường dẫn tới file icon
        self.setWindowIcon(QIcon(icon_path))

        # Khởi tạo QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_real_time)  # Kết nối tín hiệu với hàm cập nhật
        self.timer.start(1000)  # Cập nhật mỗi giây

        # Bắt đầu hiển thị thời gian thực
        self.update_real_time()

        # Kết nối nút notepad_btn
        self.notepad_btn.clicked.connect(self.open_notepad)

###############################################################################################################################################
        # Khởi tạo filtered_df
        self.filtered_df = pd.DataFrame()  # Khởi tạo DataFrame rỗng
        # Đọc file CSV
        self.file_path = 'database/data_user.csv'   # Đường dẫn
        
        # Tạo folder database nếu chưa có
        if not os.path.exists('database'):
            os.makedirs('database')
#                                                       LOAD FILE CSV
        # Đọc file CSV
        self.load_data()

    
###############################################################################################################################################
#                                                XỬ LÍ SỰ KIỆN CHO CÁC NÚT


        self.icon_name_widget.setHidden(True)   # Ẩn giao diện icon_name

        self.quanlichiteu_Btn1.setChecked(True) # Hiển thị giao diện quản lý chi tiêu khi mở ứng dụng

        # Xử lí logic khi ấn vào quản lí chi tiêu
        self.quanlichiteu_Btn1.clicked.connect(self.switch_QLCT_page)
        self.quanlichiteu_Btn2.clicked.connect(self.switch_QLCT_page)

        #Xử lí logic khi ấn vào phân tích chi tiêu
        self.phantichchiteu_Btn1.clicked.connect(self.switch_PTCT_page)
        self.phantichchiteu_Btn2.clicked.connect(self.switch_PTCT_page)

        #Xử lí logic khi ấn vào quản lý tiết kiệm
        self.goiytietkiem_Btn1.clicked.connect(self.switch_GYTK_page)
        self.goiytietkiem_Btn2.clicked.connect(self.switch_GYTK_page)

        #Xử lí logic khi ấn vào quản lí mục tiêu
        self.quanlymuctieu_Btn1.clicked.connect(self.switch_QLMT_page)
        self.quanlymuctieu_Btn2.clicked.connect(self.switch_QLMT_page)

        #Xử lí logic khi ấn vào setting
        self.setting_Btn1.clicked.connect(self.switch_setting_page)
        self.setting_Btn2.clicked.connect(self.switch_setting_page)

        # Xử lí logic khi ấn nút Thu
        self.them_Btn.clicked.connect(lambda:self.show_themchitieu("Thu"))

        # Xử lí logic khi ấn nút Chi
        self.themchi_Btn.clicked.connect(lambda:self.show_themchitieu("Chi"))

        # Vô hiệu hóa chức năng click vào table
        self.chitieu_table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        
        # Kết nối sự kiện double click vào hàng
        self.chitieu_table.cellDoubleClicked.connect(self.on_cell_double_clicked)

        # Xử lí sự kiện tìm kiếm
        self.Chondanhmuc_comboBox.currentIndexChanged.connect(self.search_on_chitieuTable)
        self.timchitieu_lineEdit.textChanged.connect(self.search_on_chitieuTable)

        self.bieudo_tron_Thu.setLayout(QVBoxLayout())  # Đặt layout cho QFrame
        self.bieudo_tron_Chi.setLayout(QVBoxLayout())
        # Kết nối sự kiện clicked của button circle_chart
        self.circle_chart.setChecked(True)

        self.circle_chart.clicked.connect(self.show_pie_chart)

        self.bieudo_cot_ThuChi.setLayout(QVBoxLayout())
        # Kết nối sự kiện clicked của button chart
        self.chart.clicked.connect(self.show_bar_chart)

        # Xử lí sự kiện lọc giá trị theo ngày/tháng/năm khi ấn submit_day
        self.submit_date.clicked.connect(self.on_submit_day_clicked)
        
    def on_cell_double_clicked(self):
        # Hiện cửa sổ luachon_Table
        luachon_dialog = LuachonTable(self)
        luachon_dialog.exec()


    def switch_QLCT_page(self):
        self.stackedWidget_page.setCurrentIndex(0)
        self.stackedWidget_phantichchitieu.setCurrentIndex(0)
        self.circle_chart.setChecked(True)

    def switch_PTCT_page(self):
        self.stackedWidget_page.setCurrentIndex(1)
        self.load_data()  # Tải dữ liệu từ file CSV

    def switch_GYTK_page(self):
        self.stackedWidget_page.setCurrentIndex(2)
    
    def switch_QLMT_page(self):
        self.stackedWidget_page.setCurrentIndex(3)
    
    def switch_setting_page(self):
        self.stackedWidget_page.setCurrentIndex(4)

    #-------------------------------------------------#
    def show_themchitieu(self,loai):
        self.themchitieu_dialog = ChiTieu(self,loai)
        self.themchitieu_dialog.exec()
    #-------------------------------------------------#
#
    def update_real_time(self):
        # Lấy ngày hiện tại và định dạng thành dd/mm/yyyy
        current_date = QDate.currentDate().toString("dd/MM/yyyy")
        self.realTime.setText(f"Today: {current_date}")  # Cập nhật giá trị cho QLineEdit

    def open_notepad(self):
        # Đường dẫn tới file txt
        file_path = 'HDSD.txt'  
        
        # Nội dung bạn muốn ghi vào file
        content = "HƯỚNG DẪN SỬ DỤNG TRƯỚC KHI DÙNG."

        # Ghi nội dung vào file (tạo file nếu chưa tồn tại)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        # Mở file bằng Notepad
        # Kiểm tra và mở Notepad
        try:
            subprocess.run(['notepad.exe', file_path], check=True)
        except FileNotFoundError:
            print("Không tìm thấy Notepad. Kiểm tra cài đặt hệ thống.")
    #-------------------------------------------------#
#                   Kết nối sự kiện page phân tích chi tiêu
    def show_pie_chart(self):
        # Chuyển đến pie_chart trong stackedWidget_phantichchitieu
        self.stackedWidget_phantichchitieu.setCurrentIndex(0)

        # Gọi hàm vẽ biểu đồ
        self.draw_pie_charts_1() 
        self.draw_pie_charts_2() 

    def show_bar_chart(self):
        # Chuyển đến bar_chart trong stackedWidget_phantichchitieu
        self.stackedWidget_phantichchitieu.setCurrentIndex(1)

        # Gọi hàm vẽ biểu đồ
        self.draw_bar_chart()

    def on_submit_day_clicked(self):
        # Lấy giá trị từ QDateEdit
        first_date = self.first_date.date().toString("dd/MM/yyyy")
        second_date = self.second_date.date().toString("dd/MM/yyyy")
        
        # Chuyển đổi thành định dạng datetime để so sánh
        first_date_dt = pd.to_datetime(first_date, format='%d/%m/%Y')
        second_date_dt = pd.to_datetime(second_date, format='%d/%m/%Y')

        # Lọc dữ liệu theo ngày
        self.filtered_df = self.df[
            (pd.to_datetime(self.df["Thời gian"], format='%d/%m/%Y') >= first_date_dt) &
            (pd.to_datetime(self.df["Thời gian"], format='%d/%m/%Y') <= second_date_dt)
        ]

        # Vẽ lại biểu đồ với dữ liệu đã lọc
        try:
            self.draw_pie_charts_1()  # Biểu đồ tròn cho Thu
            self.draw_pie_charts_2()  # Biểu đồ tròn cho Chi
            self.draw_bar_chart()      # Biểu đồ cột
            print("Tạo biểu đồ khi chọn Date thành công.")
        except Exception as e:
            print(f"Không tạo được biểu đồ khi chọn Date: {e}")


    #-------------------------------------------------#
    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path, sep=";")

            # Kiểm tra tên cột
            
            print("Dữ liệu đã được đọc thành công từ file CSV.")
            
            self.chitieu_table.setRowCount(0)  # Xóa tất cả các hàng hiện tại
            for index, row in self.df.iterrows():
                row_position = self.chitieu_table.rowCount()
                self.chitieu_table.insertRow(row_position)
                self.chitieu_table.setItem(row_position, 0, QTableWidgetItem(str(index + 1)))  # STT
                self.chitieu_table.setItem(row_position, 1, QTableWidgetItem(str(row["Thời gian"])))  # Ngày
                self.chitieu_table.setItem(row_position, 2, QTableWidgetItem(str(row["Danh mục"])))  # Danh mục
                self.chitieu_table.setItem(row_position, 3, QTableWidgetItem(str(row["Tên chi tiêu"])))  # Tên chi tiêu
                
                loai_hinh = row.get("Loại hình", "")
                so_tien = row.get("Số tiền", "0")
                
                try:
                    sotien = str(so_tien)
                    item = QTableWidgetItem()  # Tạo một QTableWidgetItem mới

                    if loai_hinh == "Thu":
                        item.setText(f"+{sotien}")
                        item.setForeground(QColor("#188037"))
                    elif loai_hinh == "Chi":
                        item.setText(f"-{sotien}")
                        item.setForeground(QColor("#CC181F"))
                    else:
                        item.setText(sotien)

                    self.chitieu_table.setItem(row_position, 4, item)  # Đặt item vào bảng
                except (ValueError, OverflowError):
                    print(f"Lỗi khi chuyển đổi số tiền: {so_tien}. Đặt ô trống.")
                    self.chitieu_table.setItem(row_position, 4, QTableWidgetItem("0"))  # Đặt ô trống hoặc giá trị mặc định
                
                 # Xử lý giá trị ghi chú
                ghi_chu = row.get("Ghi chú", "")
                ghi_chu = str(ghi_chu)  # Chuyển đổi thành chuỗi
                
                # Loại bỏ .0 nếu ghi chú là số thực
                if ghi_chu.isdigit() == False and ghi_chu.endswith('.0'):
                    ghi_chu = ghi_chu[:-2]  # Loại bỏ .0
                elif pd.isna(ghi_chu) or ghi_chu == "nan":  # Kiểm tra NaN
                    ghi_chu = ""  # Gán chuỗi rỗng
                
                # print(f"Ghi chú trước khi thêm vào bảng: '{ghi_chu}'")  # In ra giá trị ghi chú với dấu nháy
                self.chitieu_table.setItem(row_position, 5, QTableWidgetItem(ghi_chu))  # Ghi chú

        except FileNotFoundError:
            print("File không tồn tại. Một file mới sẽ được tạo.")
            self.df = pd.DataFrame(columns=["STT", "Thời gian", "Danh mục", "Tên chi tiêu", "Số tiền", "Ghi chú", "Loại hình"])
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file: {e}")

###############################################################################################################################################
    def update_csv(self):#                          CẬP NHẬT DATA VÀO DATABASE
        try:
            # Lấy dữ liệu từ chitieu_table và lưu vào file CSV
            rows = []
            for row in range(self.chitieu_table.rowCount()):
                row_data = []
                for column in range(self.chitieu_table.columnCount()):
                    item = self.chitieu_table.item(row, column)
                    row_data.append(item.text() if item else "")
                rows.append(row_data)

            # Kiểm tra nếu bảng không trống
            if not rows:
                print("Không có dữ liệu để cập nhật.")
                return
            
            # Thêm loại hình vào dữ liệu cho hàng mới
            for row in rows:
                # Xử lý số tiền để loại bỏ dấu
                so_tien = row[4]  # Số tiền
                if so_tien.startswith("+"):
                    row[4] = so_tien[1:]  # Loại bỏ dấu "+"
                    row.append("Thu")  # Thêm loại hình
                elif so_tien.startswith("-"):
                    row[4] = so_tien[1:]  # Loại bỏ dấu "-"
                    row.append("Chi")  # Thêm loại hình
                else:
                    row.append(" ")  # Nếu không có dấu, để trống

            # Chuyển đổi danh sách thành DataFrame và thêm cột "Loại hình"
            df = pd.DataFrame(rows, columns=["STT", "Thời gian", "Danh mục", "Tên chi tiêu", "Số tiền","Ghi chú", "Loại hình"])
            
            # Chuyển đổi cột "Số tiền" để loại bỏ dấu
            df["Số tiền"] = df["Số tiền"].str.replace("+", "").str.replace("-", "").str.strip()  # Loại bỏ dấu và khoảng trắng

            # Lưu vào file CSV
            df.to_csv(self.file_path, sep=";", index=False)
            print("Dữ liệu đã được cập nhật vào file CSV.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi cập nhật file CSV: {e}")
###############################################################################################################################################
#                                      CHỨC NĂNG TÌM KIẾM THEO DANH MỤC VÀ TÊN CHI TIÊU
    def search_on_chitieuTable(self):

        luachon_danhmuc = self.Chondanhmuc_comboBox.currentText() # Lấy giá trị hiện tại của box để tìm kiếm
        tim_tenchitieu = self.timchitieu_lineEdit.text().lower()  # Lấy giá trị hiện tại của lineEdit để tìm kiếm

        self.chitieu_table.setRowCount(0)   # Xóa tất cả các hàng ở hiện tại

        for index , row in self.df.iterrows():
            danh_muc = str(row["Danh mục"])
            ten_chi_tieu = str(row["Tên chi tiêu"]).lower()

            danhmuc_hople = (luachon_danhmuc == "Tất cả" or danh_muc == luachon_danhmuc)
            tenchitieu_hople = tim_tenchitieu in ten_chi_tieu

            if danhmuc_hople and tenchitieu_hople:
                row_position = self.chitieu_table.rowCount()
                self.chitieu_table.insertRow(row_position)
                self.chitieu_table.setItem(row_position, 0, QTableWidgetItem(str(index + 1)))
                self.chitieu_table.setItem(row_position, 1, QTableWidgetItem(str(row["Thời gian"])))
                self.chitieu_table.setItem(row_position, 2, QTableWidgetItem(str(row["Danh mục"])))
                self.chitieu_table.setItem(row_position, 3, QTableWidgetItem(str(row["Tên chi tiêu"])))

                loai_hinh = row.get("Loại hình", "")
                so_tien = row.get("Số tiền", "0")

                try:
                    sotien = str(so_tien)
                    item = QTableWidgetItem()

                    if loai_hinh == "Thu":
                        item.setText(f"+{sotien}")
                        item.setForeground(QColor("#188037"))
                    elif loai_hinh == "Chi":
                        item.setText(f"-{sotien}")
                        item.setForeground(QColor("#CC181F"))
                    else:
                        item.setText(sotien)

                    self.chitieu_table.setItem(row_position, 4, item)
                except (ValueError, OverflowError):
                    print(f"Lỗi khi chuyển đổi số tiền: {so_tien}. Đặt ô trống.")
                    self.chitieu_table.setItem(row_position, 4, QTableWidgetItem("0"))

                ghi_chu = row.get("Ghi chú", "")
                ghi_chu = str(ghi_chu)

                if ghi_chu.isdigit() == False and ghi_chu.endswith('.0'):
                    ghi_chu = ghi_chu[:-2]
                elif pd.isna(ghi_chu) or ghi_chu == "nan":
                    ghi_chu = ""

                self.chitieu_table.setItem(row_position, 5, QTableWidgetItem(ghi_chu))

###############################################################################################################################################
#                                               BIỂU ĐỒ TRÒN
#   BIỂU ĐỒ TRÒN THU
    def draw_pie_charts_1(self):
    
        if self.bieudo_tron_Thu.layout() is not None:
            QWidget().setLayout(self.bieudo_tron_Thu.layout())  # Xóa layout hiện tại

        # Tách dữ liệu thành hai loại hình Thu
        thu_data = self.filtered_df[self.filtered_df["Loại hình"] == "Thu"]

        # Tổng hợp số tiền theo danh mục
        thu_summary = thu_data.groupby("Danh mục")["Số tiền"].sum()

        # Tạo Figure và FigureCanvas
        fig = Figure(figsize=(4, 4))  # Kích thước của figure
        self.canvas = FigureCanvas(fig)  # Lưu canvas vào thuộc tính
        
        # Tạo danh sách explode, tách từng phần từ nhỏ đến lớn
        explode = [0.0009 * (i + 1) for i in range(len(thu_summary))]  # Tách rời từ nhỏ đến lớn

        # Vẽ biểu đồ
        ax = fig.add_subplot(111)
        wedges, texts, autotexts = ax.pie(
            thu_summary,
            labels=thu_summary.index,  # Hiển thị nhãn cho biểu đồ
            autopct='%1.1f%%',
            startangle=90,
            radius=0.1,
            explode=explode  # Thêm tham số explode
        )
        ax.axis('equal')  # Đảm bảo biểu đồ là hình tròn
        ax.set_title('Những Khoản Thu')

        # Thêm legend
        ax.legend(wedges, thu_summary.index, title="Danh mục", loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=2)

        # Kiểm tra và xóa layout cũ
        if self.bieudo_tron_Thu.layout() is not None:
            QWidget().setLayout(self.bieudo_tron_Thu.layout())  # Xóa layout cũ

        # Tạo layout mới và gán cho QFrame
        new_layout = QVBoxLayout(self.bieudo_tron_Thu)
        new_layout.addWidget(self.canvas)

        # Vẽ lại canvas
        self.canvas.draw()

#   BIỂU ĐỒ TRÒN CHI
    def draw_pie_charts_2(self):
        if self.bieudo_tron_Chi.layout() is not None:
            QWidget().setLayout(self.bieudo_tron_Chi.layout())
        # Tách dữ liệu thành hai loại hình Chi
        chi_data = self.filtered_df[self.filtered_df["Loại hình"] == "Chi"]
        
        # Tổng hợp số tiền theo danh mục
        chi_summary = chi_data.groupby("Danh mục")["Số tiền"].sum()

        # Tạo Figure và FigureCanvas
        fig = Figure(figsize=(4, 4))  # Kích thước của figure
        canvas = FigureCanvas(fig)
        
        # Tạo danh sách explode, tách từng phần từ nhỏ đến lớn
        explode = [0.0009 * (i + 1) for i in range(len(chi_summary))]  # Tách rời từ nhỏ đến lớn

        # Vẽ biểu đồ
        ax = fig.add_subplot(111)
        wedges, texts, autotexts = ax.pie(
            chi_summary,
            labels=chi_summary.index,  # Hiển thị nhãn cho biểu đồ
            autopct='%1.1f%%',
            startangle=90,
            radius=0.1,
            explode=explode  # Thêm tham số explode
        )
        ax.axis('equal')  # Đảm bảo biểu đồ là hình tròn
        ax.set_title('Những Khoản Chi')

        # Thêm legend
        ax.legend(wedges, chi_summary.index, title="Danh mục", loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=2)

        # Tạo layout mới và gán cho QFrame
        new_layout = QVBoxLayout(self.bieudo_tron_Chi)
        new_layout.addWidget(canvas)

        # Vẽ lại canvas
        canvas.draw()

###############################################################################################################################################

###############################################################################################################################################
#                                               BIỂU ĐỒ CỘT + ĐƯỜNG
    def draw_bar_chart(self):

        thu_data = self.filtered_df[self.filtered_df["Loại hình"] == "Thu"]
        chi_data = self.filtered_df[self.filtered_df["Loại hình"] == "Chi"]

        # Tổng hợp số tiền theo thời gian
        thu_summary = thu_data.groupby("Thời gian")["Số tiền"].sum()
        chi_summary = chi_data.groupby("Thời gian")["Số tiền"].sum()

        # Chuyển đổi chỉ số "Thời gian" thành datetime
        thu_summary.index = pd.to_datetime(thu_summary.index, format='%d/%m/%Y', dayfirst=True)
        chi_summary.index = pd.to_datetime(chi_summary.index, format='%d/%m/%Y', dayfirst=True)

        # Lấy tất cả các mốc thời gian
        all_dates = thu_summary.index.union(chi_summary.index)
        thu_summary = thu_summary.reindex(all_dates, fill_value=0)
        chi_summary = chi_summary.reindex(all_dates, fill_value=0)

        # Tạo Figure và FigureCanvas
        fig, ax = plt.subplots(figsize=(8, 6))  # Kích thước của figure
        self.canvas = FigureCanvas(fig)
        width = 0.35  # Chiều rộng của các cột

        # Tạo vị trí cho các cột
        x_indices = range(len(all_dates))

        # Vẽ cột cho Thu
        ax.bar(
            [x - width / 2 for x in x_indices],  # Đặt cột Thu bên trái
            thu_summary.values,
            width,
            label='Thu',
            color='green'  # Màu xanh lá cho Thu
        )

        # Vẽ cột cho Chi
        ax.bar(
            [x + width / 2 for x in x_indices],  # Đặt cột Chi bên phải
            chi_summary.values,
            width,
            label='Chi',
            color='red'  # Màu đỏ cho Chi
        )

        # Vẽ đường line chart cho Thu
        ax.plot(
            [x - width / 2 for x in x_indices], 
            thu_summary.values, 
            label='Đường Thu', 
            color='#23DE38', 
            linewidth=2
        )

        # Vẽ đường line chart cho Chi
        ax.plot(
            [x + width / 2 for x in x_indices],  # Điều chỉnh vị trí x cho đường Chi
            chi_summary.values, 
            label='Đường Chi', 
            color='#DE3923', 
            linewidth=2
        )

        # Đặt nhãn cho các trục
        ax.set_xlabel('Thời gian')
        ax.set_ylabel('Số tiền')
        ax.set_title('Biểu đồ cột tổng thu và chi theo thời gian')
        ax.set_xticks(x_indices)
        ax.set_xticklabels(all_dates.strftime('%d/%m/%Y'), rotation=45, ha='right')
        ax.legend()

        # Tùy chỉnh trục y
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))  # Định dạng số tiền với dấu phẩy
        ax.set_ylim(0, max(thu_summary.max(), chi_summary.max()) * 1.1 if max(thu_summary.max(), chi_summary.max()) > 0 else 1000)  # Đặt giới hạn cho trục y

        # Thêm nhãn cho các cột, với giá trị là 0 nếu giá trị thực tế là 0
        for i in range(len(all_dates)):
            thu_value = thu_summary.values[i]
            chi_value = chi_summary.values[i]

            # Nhãn cho cột Thu
            ax.text(
                x_indices[i] - width / 2, 
                max(thu_value, 0),  # Đảm bảo giá trị y là 0 nếu thu_value < 0
                f'{int(thu_value):,}' if thu_value > 0 else '0',  # Hiển thị giá trị hoặc '0'
                ha='center', 
                va='bottom'
            )

            # Nhãn cho cột Chi
            ax.text(
                x_indices[i] + width / 2, 
                max(chi_value, 0),  # Đảm bảo giá trị y là 0 nếu chi_value < 0
                f'{int(chi_value):,}' if chi_value > 0 else '0',  # Hiển thị giá trị hoặc '0'
                ha='center', 
                va='bottom'
            )


        # Xóa nội dung cũ trong bieudo_cot_ThuChi trước khi thêm biểu đồ mới
        for i in reversed(range(self.bieudo_cot_ThuChi.layout().count())):
            widget = self.bieudo_cot_ThuChi.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()


        # Thêm FigureCanvas vào QFrame
        self.bieudo_cot_ThuChi.layout().addWidget(self.canvas)

        # Hiển thị biểu đồ
        plt.tight_layout()
        self.canvas.draw()  # Vẽ lại canvas


###############################################################################################################################################
class ChiTieu (QDialog,Ui_Nhapchitieu_Dialog):
    def __init__(self, main_app,loai):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Them Chi Tieu")
        self.main_app = main_app

        # Thu và Chi
        self.loai = loai

        # Xử lí logic khi ấn nút thêm
        self.them_Btn.clicked.connect(self.save_data)

        # Xử lí logic khi ấn nút trở lại
        self.exit_btn.clicked.connect(self.close)

        # Điều kiện
    def check_info(self):

        # Lấy giá trị từ các trường nhập liệu
        danh_muc = self.Luachondanhmuc_combobox.currentText()
        ten_chi_tieu = self.nhaptenchitieu.text()
        so_tien = self.nhapsotien_linedit.text()

        # Kiểm tra xem có trường nào bị bỏ trống không
        errors = [] # Lưu các thông báo lỗi
        if not danh_muc:
            errors.append((self.Chon_label, "Vui lòng chọn danh mục."))
        if not ten_chi_tieu:
            errors.append((self.tenchitieu_label, "Vui lòng nhập tên chi tiêu."))
        if not so_tien:
            errors.append((self.sotien_lable, "Vui lòng nhập số tiền."))
        else :
            # Kiểm tra xem số tiền nhập vào có phải là số nguyên
            if not so_tien.isdigit():
                errors.append((self.sotien_lable, "Số tiền phải là số nguyên."))  

        # Nếu có lỗi, hiển thị thông báo và đổi màu chữ
        if errors:
            for label, message in errors:
                label.setStyleSheet("color: red;")
                QMessageBox.warning(self, "Thông báo", message)
                return False
        else:
            # Xử lý thêm chi tiêu ở đây
            return True

    # Xử lí dữ liệu đưa vào Table
    def save_data(self):
        # Gọi check_info và chỉ lưu dữ liệu nếu kiểm tra thành công
        if self.check_info():
            # Lấy dữ liệu từ các trường nhập liệu
            danh_muc = self.Luachondanhmuc_combobox.currentText()
            ngay_chi_tieu = self.chonngay_editdate.date().toString("dd/MM/yyyy")
            ten_chi_tieu = self.nhaptenchitieu.text()
            so_tien = self.nhapsotien_linedit.text()
            ghi_chu = self.ghichu_text.toPlainText()

            # Thêm một hàng mới vào chitieu_table từ main_app
            row_position = self.main_app.chitieu_table.rowCount()
            self.main_app.chitieu_table.insertRow(row_position)

            # Gán dữ liệu cho các ô trong hàng mới
            self.main_app.chitieu_table.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))  # STT
            self.main_app.chitieu_table.setItem(row_position, 1, QTableWidgetItem(ngay_chi_tieu))   # Ngày/tháng/năm
            self.main_app.chitieu_table.setItem(row_position, 2, QTableWidgetItem(danh_muc))    # Danh mục chi tiêu
            self.main_app.chitieu_table.setItem(row_position, 3, QTableWidgetItem(ten_chi_tieu))    # Tên Chi tiêu
            
            # Thêm kí tự "+"(Thu) hoặc "-"(Chi) và đổi Color để phân biệt đâu là tiền thu và tiền chi trong table
            if self.loai == "Thu":
                sotien = "+" + so_tien
            else:
                sotien = "-" + so_tien
            
            item = QTableWidgetItem(sotien)
            
            #Dùng toán tử 3 ngôi thay if else để đổi màu sotien
            item.setForeground(QColor("#188037") if self.loai == "Thu" else QColor("#CC181F"))

            self.main_app.chitieu_table.setItem(row_position, 4, item)  # Số tiền Thu (+) và Chi (-)

            self.main_app.chitieu_table.setItem(row_position, 5, QTableWidgetItem(ghi_chu)) # Note

###############################################################################################################################################
            # Cập nhật dữ liệu vào file CSV
            self.main_app.update_csv()

            # Gọi lại load_data để nạp lại dữ liệu từ file
            self.main_app.load_data()

            # self.close()  # Đóng cửa sổ thêm chi tiêu

###############################################################################################################################################
class LuachonTable(QDialog, Ui_luachon_table):
    def __init__(self, main_app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Lua Chon")
        self.main_app = main_app

        # Kết nối nút Chỉnh sửa
        self.edit_table_btn.clicked.connect(self.open_chinhsua)
        # Kết nối nút Xóa
        self.delete_table_btn.clicked.connect(self.delete_data)
        # Kết nối nút Đóng
        self.close_WidgetEdit.clicked.connect(self.close_Dialog)

    def open_chinhsua(self):
        # Hiện giao diện chỉnh sửa
        current_row = self.main_app.chitieu_table.currentRow()
        if current_row >= 0:  # Kiểm tra nếu có hàng được chọn
            # Hiện giao diện chỉnh sửa và truyền main_app
            chinhsua_dialog = ChinhsuaCT(self.main_app)
            chinhsua_dialog.load_data(current_row)  # Gọi phương thức để load dữ liệu
            self.close()  # Đóng dialog hiện tại
            chinhsua_dialog.exec()
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một hàng để chỉnh sửa.")

    def delete_data(self):
        current_row = self.main_app.chitieu_table.currentRow()
        
        if current_row >= 0:  # Kiểm tra nếu có hàng được chọn
            # Xóa hàng tương ứng
            self.main_app.chitieu_table.removeRow(current_row)
            # Cập nhật lại STT cho tất cả các hàng còn lại
            for row in range(self.main_app.chitieu_table.rowCount()):
                self.main_app.chitieu_table.item(row, 0).setText(str(row + 1))  # Cột STT là cột 0

            self.main_app.update_csv()

            self.accept()  # Đóng cửa sổ lựa chọn
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một hàng để xóa.")
    
    def close_Dialog(self):
        self.close()

class ChinhsuaCT(QDialog, Ui_chinhsuachitieu_Dialog):
    def __init__(self, main_app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Chinh Sua Chi Tieu")
        self.main_app = main_app  # Lưu đối tượng main_app để sử dụng sau

        # Kết nối nút Lưu với phương thức lưu dữ liệu
        self.hoantat_btn.clicked.connect(self.save_data)

    def load_data(self, current_row):
        # Lấy dữ liệu từ hàng
        date_item = self.main_app.chitieu_table.item(current_row, 1)
        category_item = self.main_app.chitieu_table.item(current_row, 2)
        name_item = self.main_app.chitieu_table.item(current_row, 3)
        amount_item = self.main_app.chitieu_table.item(current_row, 4)
        note_item = self.main_app.chitieu_table.item(current_row, 5)

        # Điền dữ liệu vào các trường nhập liệu
        if date_item:
            self.chonngay_editdate.setDate(QDate.fromString(date_item.text(), "dd/MM/yyyy"))
        if category_item:
            self.Luachondanhmuc_combobox.setCurrentText(category_item.text())
        if name_item:
            self.nhaptenchitieu.setText(name_item.text())
        if amount_item:
            # Phân biệt dấu "+" và "-"
            text = amount_item.text()
            if text.startswith('+'):
                self.nhapsotien_linedit.setText(text[1:])  # Loại bỏ dấu "+" và hiển thị "Thu"
                self.luachonloaihinh.setCurrentText("Thu")
            elif text.startswith('-'):
                self.nhapsotien_linedit.setText(text[1:])  # Loại bỏ dấu "-" và hiển thị "Chi"
                self.luachonloaihinh.setCurrentText("Chi")
            else:
                self.nhapsotien_linedit.setText(text)  # Không có dấu, giữ nguyên và không chọn loại hình
        if note_item:
            self.ghichu_text.setPlainText(note_item.text())

    def save_data(self):
        current_row = self.main_app.chitieu_table.currentRow()
        if current_row >= 0:
            danh_muc = self.Luachondanhmuc_combobox.currentText()
            ngay_chi_tieu = self.chonngay_editdate.date().toString("dd/MM/yyyy")
            ten_chi_tieu = self.nhaptenchitieu.text()
            so_tien = self.nhapsotien_linedit.text()
            ghi_chu = self.ghichu_text.toPlainText()
            loai_hinh = self.luachonloaihinh.currentText()  # Thu hoặc Chi

            # Cập nhật dữ liệu vào bảng
            self.main_app.chitieu_table.item(current_row, 1).setText(ngay_chi_tieu)
            self.main_app.chitieu_table.item(current_row, 2).setText(danh_muc)
            self.main_app.chitieu_table.item(current_row, 3).setText(ten_chi_tieu)

            if loai_hinh == "Thu":
                st = "+" + so_tien
            elif loai_hinh == "Chi":
                st = "-" + so_tien
            else:
                st = so_tien  # Nếu không phải "Thu" hoặc "Chi", để mặc định

            item = QTableWidgetItem(st)
            item.setForeground(QColor("#188037") if loai_hinh == "Thu" else QColor("#CC181F"))  # Đặt màu cho số tiền
            self.main_app.chitieu_table.setItem(current_row, 4, item)
            self.main_app.chitieu_table.item(current_row, 5).setText(ghi_chu)

            self.main_app.update_csv()
            self.accept()  # Đóng cửa sổ chỉnh sửa
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn một hàng để chỉnh sửa.")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MyProgram()  # Khởi tạo ct
    # main_app.setWindowFlags(Qt.FramelessWindowHint)  # Thiết lập thuộc tính cửa sổ (nếu cần)
    # main_app.setAttribute(Qt.WA_TranslucentBackground)  # Thiết lập nền trong suốt (nếu cần)

    main_app.show()  # Hiển thị ứng dụng

    app.exec()
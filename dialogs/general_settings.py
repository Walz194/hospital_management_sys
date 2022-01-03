from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QVBoxLayout, QLabel, QSizePolicy, \
    QPushButton, QComboBox, QLineEdit


class GeneralSettingsWidget(QWidget):

    def __init__(self):
        super().__init__()
        # self.tab_content = QWidget()
        # self.horizontalLayout_7 = QHBoxLayout(self.tab_content)
        self.horizontalLayout_7 = QHBoxLayout(self)
        self.left_side_wrap = QVBoxLayout(self)
        # self.data_category = QLabel(self.tab_content)
        self.data_category = QLabel(self)
        self.data_category.setText('Data Category')

        font = QtGui.QFont()
        font.setPointSize(11)
        self.data_category.setFont(font)
        self.left_side_wrap.addWidget(self.data_category)
        # self.data_category_list = QListWidget(self.tab_content)
        self.data_category_list = QListWidget(self)

        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_list.addItem(item)

        self.data_category_list.addItem("Admit Type");
        self.data_category_list.addItem("Arrival Mode");
        self.data_category_list.addItem("Bank Account Type");
        self.data_category_list.addItem("Billing Method");
        self.data_category_list.addItem("Block Details");
        self.data_category_list.addItem("Blood Group");
        self.data_category_list.addItem("Booking Mode");

        self.left_side_wrap.addWidget(self.data_category_list)
        self.horizontalLayout_7.addLayout(self.left_side_wrap)

        self.right_side_wrap = QVBoxLayout(self)
        self.data_category_options_wrap = QVBoxLayout(self)
        # self.data_category_options = QLabel(self.tab_content)
        self.data_category_options = QLabel(self)
        self.data_category_options.setText('Account Status')
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.data_category_options.sizePolicy().hasHeightForWidth())
        self.data_category_options.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.data_category_options.setFont(font)
        self.data_category_options_wrap.addWidget(self.data_category_options)
        # self.data_category_options_list = QListWidget(self.tab_content)
        self.data_category_options_list = QListWidget(self)
        # item = QListWidgetItem()
        # self.data_category_options_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_options_list.addItem(item)
        # item = QListWidgetItem()
        # self.data_category_options_list.addItem(item)

        self.data_category_options_list.addItem("Active");
        self.data_category_options_list.addItem("Inactive");
        self.data_category_options_list.addItem("Discharged");

        self.data_category_options_wrap.addWidget(self.data_category_options_list)
        self.right_side_wrap.addLayout(self.data_category_options_wrap)
        self.input_form_wrap = QVBoxLayout(self)

        self.data_id_and_edit_wrap = QHBoxLayout(self)
        # self.data_id = QLabel(self.tab_content)
        self.data_id = QLabel(self)
        self.data_id.setMinimumSize(QtCore.QSize(100, 0))
        self.data_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.data_id_and_edit_wrap.addWidget(self.data_id)
        # self.data_id_entry = QLineEdit(self.tab_content)
        self.data_id_entry = QLineEdit(self)
        self.data_id_and_edit_wrap.addWidget(self.data_id_entry)
        # self.edit_change_btn = QPushButton(self.tab_content)
        self.edit_change_btn = QPushButton(self)
        self.data_id_and_edit_wrap.addWidget(self.edit_change_btn)
        self.input_form_wrap.addLayout(self.data_id_and_edit_wrap)

        self.description_wrap = QHBoxLayout(self)
        # self.description = QLabel(self.tab_content)
        self.description = QLabel(self)
        self.description.setMinimumSize(QtCore.QSize(100, 0))
        self.description.setMaximumSize(QtCore.QSize(100, 16777215))
        self.description_wrap.addWidget(self.description)
        # self.description_entry = QLineEdit(self.tab_content)
        self.description_entry = QLineEdit(self)
        self.description_wrap.addWidget(self.description_entry)
        self.input_form_wrap.addLayout(self.description_wrap)

        self.parent_data_wrap = QHBoxLayout(self)
        # self.parent_data = QLabel(self.tab_content)
        self.parent_data = QLabel(self)
        self.parent_data.setMinimumSize(QtCore.QSize(100, 0))
        self.parent_data.setMaximumSize(QtCore.QSize(100, 16777215))
        self.parent_data_wrap.addWidget(self.parent_data)
        # self.parent_data_options = QComboBox(self.tab_content)
        self.parent_data_options = QComboBox(self)
        self.parent_data_wrap.addWidget(self.parent_data_options)
        self.input_form_wrap.addLayout(self.parent_data_wrap)

        self.status_wrap = QHBoxLayout(self)
        # self.status = QLabel(self.tab_content)
        self.status = QLabel(self)
        self.status.setMinimumSize(QtCore.QSize(100, 0))
        self.status.setMaximumSize(QtCore.QSize(100, 16777215))
        self.status_wrap.addWidget(self.status)
        # self.status_options = QComboBox(self.tab_content)
        self.status_options = QComboBox(self)
        self.status_wrap.addWidget(self.status_options)
        self.input_form_wrap.addLayout(self.status_wrap)

        self.locked_wrap = QHBoxLayout(self)
        # self.locked = QLabel(self.tab_content)
        self.locked = QLabel(self)
        self.locked.setMinimumSize(QtCore.QSize(100, 0))
        self.locked.setMaximumSize(QtCore.QSize(100, 16777215))
        self.locked_wrap.addWidget(self.locked)
        # self.locked_options = QComboBox(self.tab_content)
        self.locked_options = QComboBox(self)
        self.locked_wrap.addWidget(self.locked_options)
        self.input_form_wrap.addLayout(self.locked_wrap)

        self.buttons_wrap = QHBoxLayout(self)
        # self.save_btn = QPushButton(self.tab_content)
        self.save_btn = QPushButton(self)
        self.buttons_wrap.addWidget(self.save_btn)
        # self.clear_btn = QPushButton(self.tab_content)
        self.clear_btn = QPushButton(self)
        self.buttons_wrap.addWidget(self.clear_btn)
        # self.close_btn = QPushButton(self.tab_content)
        self.close_btn = QPushButton(self)
        self.buttons_wrap.addWidget(self.close_btn)
        self.input_form_wrap.addLayout(self.buttons_wrap)
        self.right_side_wrap.addLayout(self.input_form_wrap)
        self.horizontalLayout_7.addLayout(self.right_side_wrap)

        self.data_id.setText("Data ID")
        self.edit_change_btn.setText("Edit")
        self.description.setText("Description")
        self.parent_data.setText("Parent Data")
        self.status.setText("Status")
        self.locked.setText("Locked")
        self.save_btn.setText("Save")
        self.clear_btn.setText("Clear")
        self.close_btn.setText("Close")

        #
        # self.tab_two = QWidget()
        # self.tabWidget.addTab(self.tab_two, "")
        # self.verticalLayout_5.addWidget(self.tabWidget)

        # self.retranslateUi(MainWindow)
        # self.tabWidget.setCurrentIndex(0)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)'
        # self.tab_content.show()

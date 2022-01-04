from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QVBoxLayout, QLabel, QSizePolicy, QPushButton, QComboBox, QLineEdit


class GeneralSettingsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.horizontalLayout_7 = QHBoxLayout(self)
        self.left_side_wrap = QVBoxLayout(self)
        self.data_category = QLabel(self)
        self.data_category.setText('Data Category')

        font = QtGui.QFont()
        font.setPointSize(11)
        self.data_category.setFont(font)
        self.left_side_wrap.addWidget(self.data_category)
        self.data_category_list = QListWidget(self)

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
        self.data_category_options_list = QListWidget(self)

        self.data_category_options_list.addItem("Active");
        self.data_category_options_list.addItem("Inactive");
        self.data_category_options_list.addItem("Discharged");

        self.data_category_options_wrap.addWidget(self.data_category_options_list)
        self.right_side_wrap.addLayout(self.data_category_options_wrap)
        self.input_form_wrap = QVBoxLayout(self)

        self.data_id_and_edit_wrap = QHBoxLayout(self)
        self.data_id = QLabel(self)
        self.data_id.setMinimumSize(QtCore.QSize(100, 0))
        self.data_id.setMaximumSize(QtCore.QSize(100, 16777215))
        self.data_id_and_edit_wrap.addWidget(self.data_id)
        self.data_id_entry = QLineEdit(self)
        self.data_id_and_edit_wrap.addWidget(self.data_id_entry)
        self.edit_change_btn = QPushButton(self)
        self.data_id_and_edit_wrap.addWidget(self.edit_change_btn)
        self.input_form_wrap.addLayout(self.data_id_and_edit_wrap)

        self.description_wrap = QHBoxLayout(self)
        self.description = QLabel(self)
        self.description.setMinimumSize(QtCore.QSize(100, 0))
        self.description.setMaximumSize(QtCore.QSize(100, 16777215))
        self.description_wrap.addWidget(self.description)
        self.description_entry = QLineEdit(self)
        self.description_wrap.addWidget(self.description_entry)
        self.input_form_wrap.addLayout(self.description_wrap)

        self.parent_data_wrap = QHBoxLayout(self)
        self.parent_data = QLabel(self)
        self.parent_data.setMinimumSize(QtCore.QSize(100, 0))
        self.parent_data.setMaximumSize(QtCore.QSize(100, 16777215))
        self.parent_data_wrap.addWidget(self.parent_data)
        self.parent_data_options = QComboBox(self)
        self.parent_data_wrap.addWidget(self.parent_data_options)
        self.input_form_wrap.addLayout(self.parent_data_wrap)

        self.status_wrap = QHBoxLayout(self)
        self.status = QLabel(self)
        self.status.setMinimumSize(QtCore.QSize(100, 0))
        self.status.setMaximumSize(QtCore.QSize(100, 16777215))
        self.status_wrap.addWidget(self.status)
        self.status_options = QComboBox(self)
        self.status_wrap.addWidget(self.status_options)
        self.input_form_wrap.addLayout(self.status_wrap)

        self.locked_wrap = QHBoxLayout(self)
        self.locked = QLabel(self)
        self.locked.setMinimumSize(QtCore.QSize(100, 0))
        self.locked.setMaximumSize(QtCore.QSize(100, 16777215))
        self.locked_wrap.addWidget(self.locked)
        self.locked_options = QComboBox(self)
        self.locked_wrap.addWidget(self.locked_options)
        self.input_form_wrap.addLayout(self.locked_wrap)

        self.buttons_wrap = QHBoxLayout(self)
        self.save_btn = QPushButton(self)
        self.buttons_wrap.addWidget(self.save_btn)
        self.clear_btn = QPushButton(self)
        self.buttons_wrap.addWidget(self.clear_btn)
        self.close_btn = QPushButton(self)
        self.buttons_wrap.addWidget(self.close_btn)
        self.input_form_wrap.addLayout(self.buttons_wrap)
        self.right_side_wrap.addLayout(self.input_form_wrap)
        self.horizontalLayout_7.addLayout(self.right_side_wrap)

        self.side_button_wrap = QVBoxLayout()
        self.side_button_wrap.setContentsMargins(-1, 30, -1, 250)
        self.side_button_wrap.setSpacing(6)
        self.side_button_wrap.setObjectName("side_button_wrap")
        self.down_btn = QPushButton(self)
        self.down_btn.setIcon(QIcon('./icons/down-right-arrow.png'))
        self.down_btn.setIconSize(QSize(30, 30))
        self.down_btn.setObjectName("down_btn")
        self.side_button_wrap.addWidget(self.down_btn)
        self.up_btn = QPushButton(self)
        self.up_btn.setObjectName("up_btn")
        self.up_btn.setIcon(QIcon('./icons/upward-arrow.png'))
        self.up_btn.setIconSize(QSize(30, 30))
        self.side_button_wrap.addWidget(self.up_btn)
        self.save_btn_2 = QPushButton(self)
        self.save_btn_2.setObjectName("save_btn_2")
        self.save_btn_2.setIcon(QIcon('./icons/diskette.png'))
        self.save_btn_2.setIconSize(QSize(30, 30))
        self.side_button_wrap.addWidget(self.save_btn_2)
        self.delete_2 = QPushButton(self)
        self.delete_2.setObjectName("delete_2")
        self.side_button_wrap.addWidget(self.delete_2)
        self.delete_2.setIcon(QIcon('./icons/cancel.png'))
        self.delete_2.setIconSize(QSize(30, 30))
        self.horizontalLayout_7.addLayout(self.side_button_wrap)

        self.data_id.setText("Data ID")
        self.edit_change_btn.setText("Edit")
        self.description.setText("Description")
        self.parent_data.setText("Parent Data")
        self.status.setText("Status")
        self.locked.setText("Locked")
        self.save_btn.setText("Save")
        self.clear_btn.setText("Clear")
        self.close_btn.setText("Close")


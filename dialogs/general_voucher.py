from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QFrame, QSizePolicy, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QComboBox, \
    QPushButton, QLineEdit, QDateEdit, QTableWidget, QAbstractScrollArea, QTableWidgetItem, QLayout, QSpacerItem


class GeneralVoucher(QWidget):

    def __init__(self):
        super().__init__()
        self.verticalLayout_3 = QVBoxLayout(self)
        self.frame = QFrame(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())

        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(711, 201))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 611, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)

        self.formLayout_2 = QFormLayout()
        self.transaction_type_label = QLabel(self.layoutWidget)
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.transaction_type_label)
        self.transaction_type_menu = QComboBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction_type_menu.sizePolicy().hasHeightForWidth())
        self.transaction_type_menu.setSizePolicy(sizePolicy)
        self.transaction_type_menu.addItem("")
        self.transaction_type_menu.addItem("")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.transaction_type_menu)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.formLayout_3 = QFormLayout()
        self.payment_mode_label = QLabel(self.layoutWidget)
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.payment_mode_label)
        self.payment_mode_menu = QComboBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payment_mode_menu.sizePolicy().hasHeightForWidth())
        self.payment_mode_menu.setSizePolicy(sizePolicy)
        self.payment_mode_menu.addItem("")
        self.payment_mode_menu.addItem("")
        self.payment_mode_menu.addItem("")
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.payment_mode_menu)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        self.new_mode_btn = QPushButton(self.layoutWidget)
        self.horizontalLayout_3.addWidget(self.new_mode_btn)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 671, 31))
        self.formLayout_4 = QFormLayout(self.horizontalLayoutWidget)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.narration_label = QLabel(self.horizontalLayoutWidget)
        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.narration_label)
        self.narration = QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.narration.sizePolicy().hasHeightForWidth())
        self.narration.setSizePolicy(sizePolicy)
        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.narration)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 10, 671, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout = QHBoxLayout()
        self.formLayout_5 = QFormLayout()
        self.batch_id_label = QLabel(self.layoutWidget1)
        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.batch_id_label)
        self.batch_id = QLineEdit(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batch_id.sizePolicy().hasHeightForWidth())
        self.batch_id.setSizePolicy(sizePolicy)
        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.batch_id)
        self.horizontalLayout.addLayout(self.formLayout_5)
        self.f2_btn = QPushButton(self.layoutWidget1)
        self.f2_btn.setMaximumSize(QtCore.QSize(41, 16777215))
        self.horizontalLayout.addWidget(self.f2_btn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.formLayout_6 = QFormLayout()
        self.transaction_date_label = QLabel(self.layoutWidget1)
        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.transaction_date_label)
        self.transaction_date = QDateEdit(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction_date.sizePolicy().hasHeightForWidth())
        self.transaction_date.setSizePolicy(sizePolicy)
        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.transaction_date)
        self.horizontalLayout_2.addLayout(self.formLayout_6)
        self.transaction_list_btn = QPushButton(self.layoutWidget1)
        self.horizontalLayout_2.addWidget(self.transaction_list_btn)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout = QVBoxLayout()
        self.accounts_table = QTableWidget(self)
        self.accounts_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.accounts_table.setColumnCount(3)
        self.accounts_table.setRowCount(0)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.accounts_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.accounts_table)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_5.setContentsMargins(500, -1, 0, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.total_label = QLabel(self)
        self.total_label.setMaximumSize(QtCore.QSize(43, 16777215))
        self.horizontalLayout_5.addWidget(self.total_label)
        self.total_entry = QLineEdit(self)
        self.total_entry.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_entry.sizePolicy().hasHeightForWidth())
        self.total_entry.setSizePolicy(sizePolicy)
        self.total_entry.setMinimumSize(QtCore.QSize(358, 0))
        self.total_entry.setMaximumSize(QtCore.QSize(444, 16777215))
        self.horizontalLayout_5.addWidget(self.total_entry)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.frame_2 = QFrame(self)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.utility_btn = QPushButton(self.frame_2)
        self.horizontalLayout_4.addWidget(self.utility_btn)
        self.clear_btn = QPushButton(self.frame_2)
        self.horizontalLayout_4.addWidget(self.clear_btn)
        self.cancel_batch_btn = QPushButton(self.frame_2)
        self.horizontalLayout_4.addWidget(self.cancel_batch_btn)
        self.print_btn = QPushButton(self.frame_2)
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout_4.addWidget(self.print_btn)
        self.close_btn = QPushButton(self.frame_2)
        self.horizontalLayout_4.addWidget(self.close_btn)
        self.save_btn = QPushButton(self.frame_2)
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.verticalLayout_3.addWidget(self.frame_2)

        self.retranslateUi()

    def retranslateUi(self):
        self.transaction_type_label.setText("Transaction Type")
        self.transaction_type_menu.setItemText(0, "Receipt")
        self.transaction_type_menu.setItemText(1, "Payment")
        self.payment_mode_label.setText("Payment Mode")
        self.payment_mode_menu.setItemText(0, "Cash")
        self.payment_mode_menu.setItemText(1, "Cheque")
        self.payment_mode_menu.setItemText(2, "Transfer")
        self.new_mode_btn.setText("New Mode")
        self.narration_label.setText("Narration")
        self.batch_id_label.setText("BATCH ID")
        self.f2_btn.setText("F2")
        self.transaction_date_label.setText("TRANSACTION DATE")
        self.transaction_list_btn.setText("Show Transaction List")
        item = self.accounts_table.horizontalHeaderItem(0)
        item.setText("Account Head")
        item = self.accounts_table.horizontalHeaderItem(1)
        item.setText("Remarks")
        item = self.accounts_table.horizontalHeaderItem(2)
        item.setText("Amount")
        self.total_label.setText("Total: ")
        self.utility_btn.setText("Utility")
        self.clear_btn.setText("Clear")
        self.cancel_batch_btn.setText("Cancel Batch")
        self.print_btn.setText("Print")
        self.close_btn.setText("Close")
        self.save_btn.setText("Save")
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayo_btn.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.right_tabwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.right_tabwidget.setObjectName("right_tabwidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.right_tabwidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.right_tabwidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.right_tabwidget, 1, 1, 1, 1)
        self.left_menu_Tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.left_menu_Tree.setMinimumSize(QtCore.QSize(200, 0))
        self.left_menu_Tree.setMaximumSize(QtCore.QSize(300, 16777215))
        self.left_menu_Tree.setStyleSheet("QTreeWidget{\n"
"    border: None;\n"
"}")
        self.left_menu_Tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.left_menu_Tree.setObjectName("left_menu_Tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.left_menu_Tree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.left_menu_Tree, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 26))
        self.menubar.setObjectName("menubar")
        self.menuFIles = QtWidgets.QMenu(self.menubar)
        self.menuFIles.setObjectName("menuFIles")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFeatures = QtWidgets.QMenu(self.menubar)
        self.menuFeatures.setObjectName("menuFeatures")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.empty_toolbar = QtWidgets.QToolBar(MainWindow)
        self.empty_toolbar.setObjectName("empty_toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.empty_toolbar)
        self.empty_statusbar = QtWidgets.QStatusBar(MainWindow)
        self.empty_statusbar.setObjectName("empty_statusbar")
        MainWindow.setStatusBar(self.empty_statusbar)
        self.menubar.addAction(self.menuFIles.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFeatures.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.right_tabwidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.right_tabwidget.setTabText(self.right_tabwidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.right_tabwidget.setTabText(self.right_tabwidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.left_menu_Tree.headerItem().setText(0, _translate("MainWindow", "School"))
        __sortingEnabled = self.left_menu_Tree.isSortingEnabled()
        self.left_menu_Tree.setSortingEnabled(False)
        self.left_menu_Tree.topLevelItem(0).setText(0, _translate("MainWindow", "School Items"))
        self.left_menu_Tree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Ruler"))
        self.left_menu_Tree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Pencil"))
        self.left_menu_Tree.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Biro"))
        self.left_menu_Tree.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Eraser"))
        self.left_menu_Tree.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "Divider"))
        self.left_menu_Tree.topLevelItem(0).child(5).setText(0, _translate("MainWindow", "Mathset"))
        self.left_menu_Tree.topLevelItem(1).setText(0, _translate("MainWindow", "School Members"))
        self.left_menu_Tree.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Cleaners"))
        self.left_menu_Tree.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Teacher"))
        self.left_menu_Tree.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Security"))
        self.left_menu_Tree.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "Head master"))
        self.left_menu_Tree.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "Baddo"))
        self.left_menu_Tree.topLevelItem(2).setText(0, _translate("MainWindow", "School Facilites"))
        self.left_menu_Tree.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Swings"))
        self.left_menu_Tree.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Toilets"))
        self.left_menu_Tree.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "Labs"))
        self.left_menu_Tree.topLevelItem(2).child(3).setText(0, _translate("MainWindow", "Storage"))
        self.left_menu_Tree.topLevelItem(2).child(4).setText(0, _translate("MainWindow", "Computer Lab"))
        self.left_menu_Tree.topLevelItem(2).child(5).setText(0, _translate("MainWindow", "Home Econmic Lab"))
        self.left_menu_Tree.setSortingEnabled(__sortingEnabled)
        self.menuFIles.setTitle(_translate("MainWindow", "FIles"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFeatures.setTitle(_translate("MainWindow", "Features"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.empty_toolbar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

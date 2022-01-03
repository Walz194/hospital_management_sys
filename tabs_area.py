from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QPoint,\
    QRect, QSize, QUrl, Qt
from PyQt5.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont,\
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,\
    QRadialGradient
from PyQt5.QtWidgets import *
from dialogs import dialog_maps


class TabsArea:

    def __init__(self,parent,layout):
        self.p = parent
        self.right_tabwidget = QTabWidget(parent)
        self.right_tabwidget.setTabsClosable(True)
        self.init_UI()
        layout.addWidget(self.right_tabwidget, 1, 1, 1, 1)



    def tabChanged(self):
        print(f'Tab was changed to : {self.right_tabwidget.currentIndex()}')


    def init_UI(self):
        self.right_tabwidget.setMinimumSize(QSize(654, 0))
        # self.right_tabwidget.addTab(self.tab_1, "One")
        # self.right_tabwidget.addTab(self.tab_2, "Two")

        # print(self.right_tabwidget.tabText(1))


    def changeTab(self):
        # setTabText(index of the tab, tab name)
        self.right_tabwidget.setTabText(0,'Alrighty')

    def addTabs(self,text):
        # self.right_tabwidget.addTab(self.right_tabwidget,text)
        # self.right_tabwidget.
        # print(text)
        dialog_maps.on_tree_item_clicked(self.right_tabwidget,text)

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from dialogs import dialog_maps


class TabsArea:

    def __init__(self,parent,layout):
        self.p = parent
        self.right_tabwidget = QTabWidget(parent)
        self.right_tabwidget.setMinimumSize(QSize(654, 0))
        self.right_tabwidget.setTabsClosable(True)

        # Code to ensure that the tab is destroyed on click
        self.right_tabwidget.tabCloseRequested.connect(lambda index: self.right_tabwidget.removeTab(index))
        layout.addWidget(self.right_tabwidget, 1, 1, 1, 1)

    def addTabs(self,text):
        dialog_maps.on_tree_item_clicked(self.right_tabwidget,text)

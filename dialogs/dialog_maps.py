from dialogs import general_settings
from dialogs import dialog_open_states
from PyQt5.QtWidgets import QWidget



def on_tree_item_clicked(tabwidget,text):

    # General Methods
    if text == 'General Settings':

        if dialog_open_states.general_settings == False:
            tabwidget.addTab(general_settings.GeneralSettingsWidget(),text)
            dialog_open_states.involved_index = dialog_open_states.get_indices(tabwidget, text)[0]
            tabwidget.setCurrentIndex(dialog_open_states.involved_index)
            dialog_open_states.general_settings = True
        else:
            try:
                dialog_open_states.involved_index = dialog_open_states.get_indices(tabwidget,text)[0]
            except IndexError:
                # dialog_open_states.general_settings = False
                tabwidget.addTab(general_settings.GeneralSettingsWidget(), text)
            tabwidget.setCurrentIndex(dialog_open_states.involved_index)


    if text == 'OP Settings Master':
        if dialog_open_states.op_settings == False:
            tabwidget.addTab(QWidget(), text)
            dialog_open_states.involved_index = dialog_open_states.get_indices(tabwidget,text)[0]
            tabwidget.setCurrentIndex(dialog_open_states.involved_index)
            dialog_open_states.op_settings = True
        else:
            try:
                dialog_open_states.involved_index = dialog_open_states.get_indices(tabwidget,text)[0]
            except IndexError:
                # dialog_open_states.op_settings = False
                tabwidget.addTab(QWidget(), text)
            tabwidget.setCurrentIndex(dialog_open_states.involved_index)
        # Do this

    if text == 'General Voucher':
        # Do this
        pass
    if text == 'Work Shop Form':
        # Do this
        pass
    if text == 'Photo Scanning Utility':
        # Do this
        pass

    # Patient Information Methods
    if text == 'Patient Registration':
        # Do this
        pass
    if text == 'Patient Info Sheet':
        # Do this
        pass
    if text == 'Patient Deposit Register':
        # Do this
        pass

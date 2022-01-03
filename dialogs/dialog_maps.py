from dialogs import general_settings

def on_tree_item_clicked(tabwidget,text):

    # General Methods
    if text == 'General Settings':
        tabwidget.addTab(general_settings.GeneralSettingsWidget(),text)
        # Do this
        print('Ayo is dumb')

    if text == 'OP Settings Master':
        # Do this
        pass
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

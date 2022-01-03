involved_index = -1
general_settings = False
op_settings = False

def get_indices(tab_widget,tab_name):
    return [index for index in range(tab_widget.count())
        if tab_name == tab_widget.tabText(index)]
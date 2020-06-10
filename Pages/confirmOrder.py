from Library import configReader

class confirmOrderClass:
    def __init__(self, obj):
        global driver1
        driver1 = obj

    def ContniueBut(self):
        driver1.find_element_by_xpath(configReader.readElementData('ConfirmOrder', 'continue_but')).click()
from Library import  configReader

class paymentMethodClass:
    def __init__(self, obj):
        global driver1
        driver1 = obj

    def paymentmeth(self):
        driver1.find_element_by_id(configReader.readElementData('Paymentmode', 'cod')).click()

    def ContniueBut(self):
        driver1.find_element_by_xpath(configReader.readElementData('Paymentmode', 'continue_but')).click()
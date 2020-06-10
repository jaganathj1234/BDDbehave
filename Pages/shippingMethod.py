from Library import configReader

class shippingMethodClass:

    def __init__(self, obj):
        global driver1
        driver1 = obj

    def shipMethod(self):
        driver1.find_element_by_id(configReader.readElementData('ShippingMethod', 'ground')).click()

    def ContniueBut(self):
        driver1.find_element_by_xpath(configReader.readElementData('ShippingMethod', 'continue_but')).click()
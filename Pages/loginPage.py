from Library import configReader


class loginPageClass:

    def __init__(self, obj):
        global driver1
        driver1 = obj

    def loginLink(self):
        driver1.find_element_by_xpath(configReader.readElementData('DemoWebMainPage', 'login_link')).click()


    def emailId(self, emailid):
        driver1.find_element_by_id(configReader.readElementData('LoginPage', 'email_id')).send_keys(emailid)

    def password(self, password):
        driver1.find_element_by_id(configReader.readElementData('LoginPage', 'pass')).send_keys(password)

    def loginBut(self):
        driver1.find_element_by_xpath(configReader.readElementData('LoginPage', 'login_but')).click()

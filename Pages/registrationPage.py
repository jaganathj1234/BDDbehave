from Library import configReader


class registrationPageClass:

    def __init__(self, obj):
        global driver1
        driver1 = obj

    def registerLink(self):
        driver1.find_element_by_xpath(configReader.readElementData('DemoWebMainPage', 'register_link')).click()

    def enterGender(self):
        driver1.find_element_by_id(configReader.readElementData('RegisterPage', 'male_radio')).click()

    def enterFirstName(self, firstname):
        driver1.find_element_by_name(configReader.readElementData('RegisterPage', 'first_name')).send_keys(firstname)

    def enterlastName(self, lastname):
        driver1.find_element_by_name(configReader.readElementData('RegisterPage', 'last_name')).send_keys(lastname)

    def emailId(self,emailid):
        driver1.find_element_by_name(configReader.readElementData('RegisterPage', 'email_id')).send_keys(emailid)

    def password(self, password):
        driver1.find_element_by_name(configReader.readElementData('RegisterPage', 'pass')).send_keys(password)

    def confirmPass(self,confirmpass):
        driver1.find_element_by_name(configReader.readElementData('RegisterPage', 'confirm_pass')).send_keys(confirmpass)

    def registerButton(self):
        driver1.find_element_by_name(configReader.readElementData('RegisterPage', 'register_but')).click()

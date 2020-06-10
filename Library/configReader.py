import configparser



def readConfigData(section, key):
    cfg = configparser.ConfigParser()
    cfg.read("./ConfigurationFile/config.cfg")
    return cfg.get(section, key)

def readElementData(section, key):
    cfg1 = configparser.ConfigParser()
    cfg1.read("./ConfigurationFile/Elements.cfg")
    return cfg1.get(section, key)



#print(readConfigData('Details', 'Url'))

import configparser
import os

def crudConfig(path):
    """
    Create, read, update, delete config
    """

    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # read some values from the config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")
    name = config.get("BYE", "byebye~")
    
    # change a value in the config
    config.set("Settings", "font_size", "12")
    config.set("BYE", "name", "BB.KIM")

    # delete a value from the config
    config.remove_option("Settings", "font_style")

    # write changes back to the config file
    with open(path, "w",) as config_file:
        config.write(config_file)

    print(font, font_size, name)

if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)

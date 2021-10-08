import yaml


class Config:
    def __init__(self):
        self.configFile = None
        self.yamlConfig = None

    def openFile(self, fileName):
        self.configFile = open(fileName, "w")
        self.yamlConfig = yaml.load(self.configFile)

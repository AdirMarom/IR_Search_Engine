class ConfigClass:
    def __init__(self):
        self.corpusPath = 'C:\\Users\\Ben Rozilio\\Desktop\\SemA\\engine\\Data\\Data'
        self.savedFileMainFolder = ''
        self.saveFilesWithStem = self.savedFileMainFolder + "/WithStem"
        self.saveFilesWithoutStem = self.savedFileMainFolder + "/WithoutStem"
        self.toStem = False

    def get__corpusPath(self):
        return self.corpusPath

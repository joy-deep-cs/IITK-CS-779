import os

class Utility:


    @staticmethod
    # create dir if not exist
    def ensureDir(dirPath):
        dir_ = os.path.dirname(dirPath)
        # print(dirPath)
        # print(dir_)
        if not os.path.exists(dir_):
            print(dir_ +" doesn't exist, so creating it.")
            os.makedirs(dir_)

    ###########

    @staticmethod
    # get all Dir as a dictionary of dirs
    def getAllDir():
        dirDict = {}
        cwd = os.getcwd()
        parentDir = "/".join(cwd.split("/"))
        dirDict["parent"] = parentDir
        dirDict["data"] = parentDir+"/data/"
        dirDict["output"] = parentDir+"/output/"
        dirDict["resources"] = parentDir+"/resources/"
        dirDict["src"] = parentDir+"/src/"
        dirDict["scripts"] = parentDir+"/scripts/"
        dirDict["temp"] = parentDir+"/temp/"

        return dirDict
    ###########
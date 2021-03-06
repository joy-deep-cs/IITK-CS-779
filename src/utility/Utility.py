import os
from ..utility.Constants import Constants

class Utility:


    @staticmethod
    # create dir if not exist
    def ensureDir(dirPath):
        # dir_ = os.path.(dirPath)
        print(dirPath)
        # print(dir_)
        if not os.path.exists(dirPath):
            print(dirPath +" doesn't exist, so creating it.")
            os.makedirs(dirPath)

    ###########

    @staticmethod
    # get all Dir as a dictionary of dirs
    def getAllDir():
        dirDict = {}
        cwd = os.getcwd()
        parentDir = "/".join(cwd.split("/"))
        dirDict[Constants.getParentDirName()] = parentDir
        dirDict[Constants.getDataDirName()] = parentDir+"/"+Constants.getDataDirName()
        dirDict[Constants.getOutputDirName()] = parentDir+"/"+Constants.getOutputDirName()
        dirDict[Constants.getResourcesDirName()] = parentDir+"/"+Constants.getResourcesDirName()
        dirDict[Constants.getSrcDirName()] = parentDir+"/"+Constants.getSrcDirName()
        dirDict[Constants.getScriptsDirName()] = parentDir+"/"+Constants.getScriptsDirName()
        dirDict[Constants.getTempDirName()] = parentDir+"/"+Constants.getTempDirName()
        dirDict[Constants.getModelDirName()] = parentDir+"/"+Constants.getModelDirName()

        return dirDict
    ###########
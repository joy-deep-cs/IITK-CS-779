from ..utility.Utility import Utility
from ..utility.Constants import Constants

allDirs = Utility.getAllDir()
dataDir = allDirs[Constants.getDataDirName()]
import glob
import pandas as pd
import json

allDirs = Utility.getAllDir()
dataDir = allDirs[Constants.getDataDirName()]
trainDataDir = dataDir+"/train/"
annotatedDataDir = trainDataDir+"tsv/"
rawDataDir = trainDataDir+"text/"
resourceDir = allDirs[Constants.getResourcesDirName()]
outputDir = allDirs[Constants.getOutputDirName()]+"/"

from grobid_quantities.quantities import QuantitiesClient
server_url = "http://localhost:8060/service"
client = QuantitiesClient(apiBase=server_url)
from os import listdir
from os.path import isfile, join
annotatedFiles = [f for f in listdir(annotatedDataDir) if isfile(join(annotatedDataDir, f))]
for annotatedFile in annotatedFiles:
    rawFile = annotatedFile[:-3]+"txt"
    rawText = open(rawDataDir+rawFile,"r").readlines() 
    outputFileName = annotatedFile[:-3]+"json"
    response = client.process_text(rawText)
    with open(outputDir+outputFileName, 'w') as outfile:
        json.dump(response, outfile)
    
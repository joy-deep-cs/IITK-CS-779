import json
import pandas as pd

from ..utility.Utility import Utility
from ..utility.Constants import Constants

allDirs = Utility.getAllDir()
dataDir = allDirs[Constants.getDataDirName()]
trainDataDir = dataDir+"/train/"
annotatedDataDir = trainDataDir+"tsv/"
rawDataDir = trainDataDir+"text/"
# resourceDir = allDirs[Constants.getResourcesDirName()]
outputDir = allDirs[Constants.getOutputDirName()]+"/"

from os import listdir
from os.path import isfile, join
outputFiles = [f for f in listdir(outputDir) if isfile(join(outputDir, f))]

def accuracyMetrics(yPred, yTrue):
    metric = {}
    metric["TP"] = 0.0
    metric["FP"] = 0.0
    metric["TN"] = 0.0
    metric["FN"] = 0.0

    for i in range(len(yPred)): 
        if yTrue[i]==yPred[i]==1:
           metric["TP"]+= 1.0
        if yPred[i]==1 and yTrue[i]!=yPred[i]:
           metric["FP"]+= 1.0
        if yTrue[i]==yPred[i]==0:
            metric["TN"]+= 1.0
        if yPred[i]==0 and yTrue[i]!=yPred[i]:
           metric["FN"]+= 1.0

    if(metric["TP"]+metric["FP"] != 0.0):
        metric["precision"] = metric["TP"]/(metric["TP"]+metric["FP"])
    else:
         metric["precision"] = 0.0
    if(metric["TP"]+metric["FN"] != 0.0):
        metric["recall"] = metric["TP"]/(metric["TP"]+metric["FN"])
    else:
        metric["recall"] = 0.0
    if(metric["TP"]+metric["TN"]+metric["FP"]+metric["FN"]!=0.0):
        metric["accuracy"] = (metric["TP"]+metric["TN"])/(metric["TP"]+metric["TN"]+metric["FP"]+metric["FN"])
    else:
        metric["accuracy"] = 0.0
    if(metric["precision"] + metric["recall"]!=0.0):
      metric["F1 score"] = (2*metric["precision"] * metric["recall"])/(metric["precision"] + metric["recall"])
    else:
        metric["F1 score"] =0.0

    return metric



def nested_dict(dataStr, outputDf, docId):
    if type(dataStr) is dict:
        keyList = dataStr.keys()

        startOffSet = Constants.getOffSetString()+Constants.getStartString()
        endOffset = Constants.getOffSetString()+Constants.getEndString()
        if(startOffSet in keyList):
            outputDf["docId"].append((docId))
            # outputDf["text"].append(dataStr["rawValue"])
            outputDf["startOffset"].append(int(dataStr[startOffSet]) -2)
            outputDf["endOffset"].append(int(dataStr[endOffset])-2)
        for key in keyList:
           outputDf =  nested_dict(dataStr[key], outputDf, docId)
    if type(dataStr) is list:
        for item in dataStr:
            outputDf = nested_dict(item, outputDf, docId)
    return outputDf
        

outputDf = {}
outputDf["docId"] = []
# outputDf["text"] = []
outputDf["startOffset"] = []
outputDf["endOffset"] = []

trainOutputDf = {}
trainOutputDf["docId"] = []
# outputDf["text"] = []
trainOutputDf["startOffset"] = []
trainOutputDf["endOffset"] = []
for outputFile in outputFiles:
    # print(outputFile)
    if(".json" in outputFile):
        with open(outputDir+outputFile) as f:
            data = json.load(f)
            # print(data)
            fileName= outputFile[:-5]
            trainOutputFile = annotatedDataDir+fileName+".tsv"
            tempDf = pd.read_csv(trainOutputFile, sep="\t", header = 0)
            tempDf = tempDf[tempDf["annotType"] == "Quantity"]
            trainOutputDf["docId"].extend(tempDf["docId"])
            trainOutputDf["startOffset"].extend(tempDf["startOffset"])
            trainOutputDf["endOffset"].extend(tempDf["endOffset"])
            docId = fileName
            outputDf = nested_dict(data[1], outputDf, docId)
            # print(outputDf)

validDataFrame = pd.DataFrame(outputDf)
validDataFrame.to_csv(outputDir+"grobid_valid.csv", index = False)

trainDataFrame = pd.DataFrame(trainOutputDf)
trainDataFrame.to_csv(outputDir+"grobid_train.csv", index = False)

docIds = set(trainDataFrame["docId"])
metrics = []
validSpans = []
trainSpans = []
intersectionSpans = []
unionSpans = []
for docId in docIds:
    # validSpan = []
    rawFile = docId+".txt"
    rawText = open(rawDataDir+rawFile,"r").readlines()
    rawText = ".".join(rawText)
    # print(rawText)
    rawTextLen = len(rawText)
    # print("rawTextLen: "+str(rawTextLen))

    trainSpan = []
    validSpan = []
    for i in range(0,rawTextLen):
        trainSpan.append(0)
        validSpan.append(0)

    tempValidDf = validDataFrame[validDataFrame["docId"] == docId]
    for start, end in zip(tempValidDf["startOffset"],tempValidDf["endOffset"]):
        for i in range(start, end):
            # print("start: "+str(start))
            # print("end: "+str(end))

            validSpan[i] = 1
    # sorted(validSpans)
    # validSpan = set(validSpan)

    # trainSpan = []
    tempTrainDf = trainDataFrame[trainDataFrame["docId"] == docId]
    for start, end in zip(tempTrainDf["startOffset"],tempTrainDf["endOffset"]):
        for i in range(start, end):
            trainSpan[i] = 1
    # sorted(trainSpans)
    # trainSpan = set(trainSpan)

    print(docId)
    metric =  accuracyMetrics(validSpan,trainSpan)
    metrics.append((docId, metric))

print(metrics)

accuracy = 0.0
f1Score = 0.0
precision =0.0
recall = 0.0
for id,metric in metrics:
    accuracy +=metric["accuracy"]
    f1Score+=metric["F1 score"]
    precision+=metric["precision"]
    recall+=metric["recall"]

accuracy/=float(len(docIds))

precision/=float(len(docIds))
recall/=float(len(docIds))
f1Score= (2*precision*recall)/(precision+recall)

print("Accuracy: "+str(accuracy))
print("F1 Score: "+str(f1Score))
print("precision: "+str(precision))
print("recall: "+str(recall))
print(len(docIds))


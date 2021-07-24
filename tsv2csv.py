import sys
import csv
import os

strInputPath = "" #file or folder path for input
strOutFile = "" #output file
boolRemoveDupHeaderValue = True # Use when processing many files. Removes first line in every file except the first line from the very first file
strMoveFolder = "" #move files here when processed

def convertTSV(tsvPathIn, tsvPathOut, boolRemoveHeader): #https://gist.github.com/dansimau/7600667
    with open(tsvPathIn, 'r') as tsvHandle:
        
        tsvin = csv.reader(tsvHandle, dialect=csv.excel_tab)
        with open(tsvPathOut, 'a',newline='') as csvfile:
            csvout = csv.writer(csvfile, dialect=csv.excel)

            for row in tsvin:
                #print(row)
                if boolRemoveHeader== False:
                  # Force all fields to be string-based (Excel specific)
                  for i, val in enumerate(row):
                      row[i] = val
                  
                  csvout.writerow(row)
                else:
                  boolRemoveHeader=False
    
boolHeaderRemoved = False
#walk directory for files
if os.path.isdir(strInputPath):  
    for (dirpath, dirnames, filenames) in os.walk(strInputPath):
      print(dirpath + "\n")
      for file in filenames:
          scanPath = os.path.join(dirpath, file)
          print(scanPath + "\n")
          if boolHeaderRemoved == True:
              boolHeaderRemoved = boolRemoveDupHeaderValue

          convertTSV(scanPath, strOutFile, boolHeaderRemoved)
          print(boolHeaderRemoved)
          if strMoveFolder != "":
              os.replace(scanPath, os.path.join(strMoveFolder, file))
          boolHeaderRemoved = True
#open a single file
elif os.path.isfile(strInputPath):  
    convertTSV(strInputPath, strOutFile, False)
    if strMoveFolder != "":
        os.replace(scanPath, os.path.join(strMoveFolder, file))

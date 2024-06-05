
import sys
import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonDict = dict()
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonDict[row['id_aluno']] = row
            
    #convert python jsonDict to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps({'alunos':jsonDict}, indent=4)
        jsonf.write(jsonString)
        
if __name__ == "__main__":
    csvFilePath = sys.argv[1]
    jsonFilePath = r'db.json'
    csv_to_json(csvFilePath, jsonFilePath)
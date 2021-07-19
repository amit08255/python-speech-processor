from fuzzywuzzy import fuzz
import json

def detectPercentage(results):
    matches = 0
    for ratio in results:
        if ratio >= 70:
            matches += 1
    return (matches / len(results)) * 100


def clearText(text):
    finalText = []
    fin = open("stopwords.txt", "r")
    datas = fin.read()
    wordlist = json.loads(datas)
    fin.close()

    textWords = text.lower().split()
    
    for x in textWords:
        if x not in wordlist:
            finalText.append(x)
    
    return " ".join(finalText)
        

def match(text, dataset, requiredPercent = 80):
    results = []
    textData = clearText(text)

    for data in dataset:
        results.append(fuzz.partial_ratio(textData, data))
    
    percent = detectPercentage(results)
    
    if percent >= requiredPercent:
        return True

    return False
import text_detection as text
import json


def detect(expression):
    query = expression.lower()
    fin = open("expressions.txt")
    data = fin.read()
    dataset = json.loads(data)
    
    for expression in dataset:
        if text.match(query, dataset[expression]):
            return expression
    return None
    

def response(expression):
    defaultResponse = "Sorry I cannot understand. Please try again."
    
    if not expression:
        return defaultResponse
    
    query = expression.lower()
    fin = open("responses.txt")
    data = fin.read()
    dataset = json.loads(data)

    if query not in dataset:
        return defaultResponse
    return dataset[query]
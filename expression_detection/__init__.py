from . import text_detection as text
import json
import os


def detect(expression):
    query = expression.lower()
    fin = open(os.path.join(os.path.dirname(__file__), 'expressions.txt'), "r")
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
    fin = open(os.path.join(os.path.dirname(__file__), 'responses.txt'), "r")
    data = fin.read()
    dataset = json.loads(data)

    if query not in dataset:
        return defaultResponse
    return dataset[query]
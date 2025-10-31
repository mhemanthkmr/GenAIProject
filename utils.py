import json

def extractJSON(response):
    start_ind = response.find('{') #6
    end_ind = response.rfind('}') #20
    return json.loads(response[start_ind : end_ind + 1])

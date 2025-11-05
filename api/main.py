from aiService import call_llm, intent_classifer
from kb_service.similarity_search import similarity_search
from flask import Flask, request
from flask_cors import CORS
from contants import set_system_instruction
from utils import extractJSON

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return {
        "status" : "Works!"
    }, 200


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if  "message" in data.keys():
        message = data.get("message")
        if message != None and message != "":
            intent_response = intent_classifer(message)
            if intent_response.get('intent') == "general":
                llm_response = call_llm(message)
                return {
                    "message" : f"{llm_response}",
                    "status" : 200
                }, 200
            else:
                try:
                    datas = similarity_search(message)
                    context = ""
                    for data in datas:
                        context += data[0]
                        context += ".  \n"
                        system_instruction = set_system_instruction(context, message)
                        llm_response = call_llm(message, system_instruction)
                        responseJSON = extractJSON(llm_response)
                        summary = responseJSON.get("summary")
                        return {
                            "message" : summary,
                            "status" : 200
                        }, 200
                except Exception as err:
                    return {
                            "message" : "Something Went Wrong",
                            "error" : str(err),
                            "status" : 500
                        }, 500
        else:
            return {
                "message" : "No Message Found in the Payload",
                "status" : 200
            }, 200
    else:
        return {
            "message" : "BAD Request",
            "status" : 400
        }, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
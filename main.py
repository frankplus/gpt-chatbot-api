from flask import Flask, request
import gpt2
from conversation import Conversation
import secrets, string

app = Flask(__name__)

enabled_api_keys = ["f24eded9-fcd1-4392-b214-01bad08fa69f"]

gpt = gpt2.GPT2(model_name="117M")
contexts = dict()

def get_instance(id):
    global contexts
    if id not in contexts:
        contexts[id] = Conversation(gpt)
    return contexts[id]

def generate_context_id():
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(64))

@app.route('/')
def hello_world():
   return "Hello, world"

@app.route('/getreply',methods = ['GET'])
def getreply():
    key = request.args.get('key')
    if not key or key not in enabled_api_keys:
        return {
            "status": "401",
            "error": "Missing or invalid API key"
            }, 401

    context_id = request.args.get('context')
    if not context_id:
        context_id = generate_context_id()
    conversation = get_instance(context_id)

    text = request.args.get('input')
    if text:
        print(f"Input: {text}")
        conversation.add_human(text)
    answer = conversation.get_answer()
    print(f"Answer: {answer}")
    conversation.add_computer(answer)

    return {
            "context": context_id,
            "output": answer
        }



if __name__ == '__main__':
   app.run("localhost", "2834", debug=True)
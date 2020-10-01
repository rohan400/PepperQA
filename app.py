'''import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin
import rs


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'

# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):

    #sessionID=req.get('responseId')
    result = req.get("queryResult")
    #user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    contexttemp=parameters.get("context")
    questiontemp = parameters.get("question")
    context = str(contexttemp)
    question = str(questiontemp)
    
	 
    intent = result.get("intent").get('displayName')
    
    if (intent=='QA - yes'):
        #answer = 'Done'
        answer = rs.predict(context, question)
       
        fulfillmentText= str(answer)
        #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": 'Please wait.....'
        }
    #else:
    #    log.write_log(sessionID, "Bot Says: " + result.fulfillmentText)'''

# import flask dependencies
app = flask.Flask(__name__)


@app.route('/')
def index():

    print('Hello Wolrd')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

'''@app.route('/')
def index():

    if request.args:

        context = request.args["context"]
        question = request.args["question"]

        answer = model.predict(context, question)
        print(answer["answer"])

        return flask.render_template('index.html', question=question, answer=answer["answer"])
    else:
        return flask.render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))'''


#if __name__ == '__main__':
#    port = int(os.getenv('PORT', 5000))
#    print("Starting app on port %d" % port)
#    app.run(debug=False, port=port, host='0.0.0.0')

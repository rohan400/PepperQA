from flask import request
from model import model
import flask
import rs


app = flask.Flask(__name__)


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
    context=parameters.get("context")
    question = parameters.get("question")
    
	 
    intent = result.get("intent").get('displayName')
    
    if (intent=='QA - yes'):
        answer = rs.predict(context, question)
       
        fulfillmentText= answer
        #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
        return {
            "fulfillmentText": fulfillmentText
        }
    #else:
    #    log.write_log(sessionID, "Bot Says: " + result.fulfillmentText)

if __name__ == '__main__':
    app.run()
#if __name__ == '__main__':
#    port = int(os.getenv('PORT', 5000))
#    print("Starting app on port %d" % port)
#    app.run(debug=False, port=port, host='0.0.0.0')

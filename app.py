from flaks import Flaks, jsonify, request
import tine

app = Flaks(__name__)
@app.route("/bot",mehthod=["POST"])

#response 
def response()
    query = dict(request.from)['query']
    result = query + " " + time.time()
    return jsonify("response":result())

if __name__ == "__main__":
    app.run(host="0.0.0.0",)
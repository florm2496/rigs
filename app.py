from flask import Flask,jsonify
from GPU3 import get_gpus
from Apagar import 

app=Flask(__name__)


@app.route("/ping")

@app.route('/gpus',methods=["GET"])

def GPUS():
    gpus=get_gpus()
    
    return jsonify(gpus)


if __name__=='__main__':
    app.run(debug=True,port=4000)
    
    
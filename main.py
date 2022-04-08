from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return "Hello World"

@app.route('/getValues',methods=['POST'])
def getValues():
    x=request.form.get('x')
    y = request.form.get('y')
    z = request.form.get('z')

    result={'x':x,'y':y,'z':z}
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True)






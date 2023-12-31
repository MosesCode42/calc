## Create a simple flask application

from flask import Flask, request

## create the flask app

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation == 'add':
        result = int(number1) + int(number1)
    elif operation == 'multiply':
        result = int(number1)*int(number2)
    elif operation == 'division':
        result = int(number1) / int(number2)
    else:
        result = int(number1) - int(number2)
    return  "The operation is {} and reslut is {}".format(operation,result)



print(__name__)

if __name__=='__main__':
   app.run(port=8000)
    
    

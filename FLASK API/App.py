from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__) #creating the Flask class object   


@app.route('/empty/temp=<name>,hum=<bs>')
def hello_world(name,bs):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return '{}.Hello {}, we are on:  {}!'.format(bs,name,formatted_now)

@app.route('/')
def index():
    return render_template('results1.html')

def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  

@app.route('/user/<uname>')  
def message(uname):  
      return render_template('message.html',name=uname) 

if __name__ == '__main__':
    app.run(debug = True)
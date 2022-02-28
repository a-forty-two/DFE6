from flask import Flask

app = Flask("myapp")

@app.route('/')
def helloworld():
    return "bye bye world"

@app.route('/home')
def homefunction():
    filedata = open('home.html','rt').read()
    return filedata

@app.route('/sum/<n>/<m>')
def sumfunc(n, m):
    # num1,num2-> strings
    n1 = int(n)
    n2 = int(m)
    return str(n1+n2)

# 2 options for host-> if you leave this blank, app runs on LOCALHOST (only inside the machine)
# host=0.0.0.0 -> app runs outside the machine 
app.run(host="0.0.0.0")


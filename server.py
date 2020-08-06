from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def generate():
    return render_template('index.html')


@app.route('/answer')
def answer():
    x = request.args.get('x', '')
    num = request.args.get('num', '')
    answ = request.args.get('answ', '')
    xAnsw = 0
    if x != '' and num != '' and answ != '':
        if (int(x) != 0):
            xAnsw = (int(answ) - int(num)) / int(x)
        else:
            if(int(num)==int(answ)):
                return render_template('answer.html', x=x, num=num, answ=answ, xAnsw='лююбое число')
            else:
                return render_template('index.html')
        return render_template('answer.html', x=x, num=num, answ=answ, xAnsw=xAnsw)
    else:
        return render_template('index.html')


app.run(debug=True)

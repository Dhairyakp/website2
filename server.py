from flask import Flask,render_template , request , redirect

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/work.html")
def work():
    return render_template('work.html')

@app.route("/works.html")
def works():
    return render_template('works.html')

@app.route("/components.html")
def components():
    return render_template('components.html')

@app.route("/work2.html")
def work2():
    return render_template('work2.html')

@app.route("/work3.html")
def work3():
    return render_template('work3.html')

@app.route('/submit.html', methods=['POST', 'GET'])
def submitform():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/submit.html')
    else:
        return 'Something went wrong'
    




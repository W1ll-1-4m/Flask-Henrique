from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
    # templates/home.html
    tasks = take_tasks()
    print('Log1', tasks)
    return render_template('home.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    task = {'name': name, 'finished': False}
    write_task(task)
    tasks = take_tasks()
    return render_template('home.html', tasks=tasks)

@app.route("/bye")
def bye():
    return 'Bye!'

def take_tasks():
    
    file_in = open('tasks.json', 'rt' )
    conteudo = file_in.read()
    conteudo = json.loads(conteudo)
    file_in.close()

    return conteudo

def write_task(task):

    conteudo = take_tasks()

    print('LOG1', conteudo)

    file_out = open('tasks.json', 'wt' )
    add = conteudo.append(task)
    print('LOG2', add)
    file_out.write(add)
    file_out.close()

app.run(debug = True)

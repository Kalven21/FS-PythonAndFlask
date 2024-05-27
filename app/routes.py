from flask import (
    Flask,
    render_template,
    request as flask_req,
    redirect,
    url_for
)
import requests

app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1:5000/tasks"

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/tasks")
def tasks_list():
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks")
        return render_template("list.html", tasks=task_list)
    return (
        render_template("error.html", err_code=response.status_code),
        response.status_code
    )
    
@app.get("/tasks/<int:pk>")
def task_detail(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        single_task = response.json().get("task")
        return render_template("detail.html", task=single_task)
    return (
        render_template("error.html", err_code=response.status_code),
        response.status_code
    )
    
@app.get("/tasks/<int:pk>/edit")
def edit_task(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    response = requests.get(url)
    if response.status_code == 200:
        single_task = response.json().get("task")
        return render_template("edit.html", task=single_task)    
    return (
        render_template("error.html", err_code=response.status_code),
        response.status_code
    )
        
@app.post("/tasks/<int:pk>/edit")
def edit_task_request(pk):
    url = "%s/%s" % (BACKEND_URL, pk)
    task_data = flask_req.form
    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        return render_template("success.html", msg="Task updated successfully")
    return (
        render_template("error.html", err_code=response.status_code),
        response.status_code
    )
    
@app.get("/new")
def create_task():
    return render_template("new.html")

@app.post("/new")
def create_task_request():
    task_data = flask_req.form.to_dict()
    response = requests.post(BACKEND_URL, json=task_data)
    if response.status_code == 201:
        return redirect(url_for("success", msg="Task created successfully"))
    return (
        render_template("error.html", err_code=response.status_code),
        response.status_code
    )

@app.get("/error")
def error():
    return render_template("error.html")

@app.get("/success")
def success():
    return render_template("success.html")
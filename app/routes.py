from flask import Flask     # From the flask module import Flask class

app = Flask(__name__)       # Create an instance of Flask (now an object)

@app.get("/")               # Flask decorator that allow us to define routes
def index():                # View function
    me = {                  # Python dictionary (key-value pairs)
        "first_name": "Kevin",
        "last_name": "Zamora",
        "hobbies": "Video games",
        "is_online": True
    }
    return me               # Returning a dictionary in flask converts it to JSON!

# idempotent
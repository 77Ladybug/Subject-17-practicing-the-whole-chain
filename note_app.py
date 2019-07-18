#FLASK
import flask
app = flask.Flask("note_app")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def add(user_note):
    user_note = flask.request.form["Add a note"]
    file = open("note","a")
    file.write(user_note + "\n")
    file.close()

    
@app.route ("/")
def homepage():
    return get_html("index")
    





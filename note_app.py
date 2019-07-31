#FLASK
import flask
app = flask.Flask("note_app")
#Function to read a html page (take page name and concatenate with .html)
def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content
#Function to read the text file with all the notes
def get_notes():
    notesdb = open("note")
    content = notesdb.read()
    notesdb.close()
    notes = content.split("\n")
    return notes

# Opening the homepage 
@app.route ("/")
def homepage():
    return get_html("index")
# Adding a note and returning a page with a message to the user
@app.route ("/add")
def route_add():
    html_page = get_html("add")
    user_note= flask.request.args.get("note")
    file = open("note","a")
    file.write(user_note + "\n")
    file.close()
    return html_page
# Creating a page with all the notes that the user input
@app.route ("/all notes")
def all_notes():
    html_page = get_html("note")
    text = get_notes()
    actual_values = ""
    for notes in text:
        actual_values +="<p>" + notes + "</p>"
    return html_page.replace("$$NOTES$$",actual_values)

@app.route ("/search")
def search():
    html_page = get_html("note")
    query = flask.request.args.get("query")
    text = get_notes()
    result = ""
    for notes in text:
        if notes.lower().find(query.lower()) != -1:
            result+="<p>" + notes + "</p>"
    if result == "":
        result = "<p>No result found</p>"
    return html_page.replace("$$NOTES$$",result)
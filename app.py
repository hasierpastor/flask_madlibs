from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import fire_story, chill_story
from story_templates import TEMPLATES


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def generate_homepage():
    """ Display a list of stories for the user to choose from"""

    list_of_templates = TEMPLATES
    return render_template("homepage.html",
    templates = list_of_templates)

@app.route('/form')
def generate_form():
    """ Takes placeholders, defined by the user's story and generates a form of questions for the user to answer"""
    
    templates_key = request.args['template']
    
    list_words = TEMPLATES[templates_key].words

    return render_template("form.html",
    words = list_words, story_id = templates_key)


@app.route('/story/<story_id>')
def generate_story(story):
    """Takes the answers from the /form page, and generates a new story that will be displayed on the story page"""

    # answers = {k.strip("form_: v for k, v in request.args if k in story.words}
    answers = request.args

    new_story = TEMPLATES[story_id].generate(answers)

    return render_template("story.html",
    story=new_story)


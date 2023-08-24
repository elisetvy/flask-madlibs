from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
# descriptive verb noun
def index():
    prompts = silly_story.prompts
    # unnecessary
    template = silly_story.template
    return render_template("questions.html",
                           prompts=prompts,
                           template=template
                           )


@app.get('/results')
# descriptive
def handle_results():
    story = silly_story.get_result_text(request.args)
    return render_template('results.html', text=story)

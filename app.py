from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route("/")
def index():
    # Dynamically get the list of prompts from the story instance
    prompts = story.prompts
    return render_template("index.html", prompts=prompts)

@app.route("/story", methods=["POST"])
def show_story():
    # Collect answers for each prompt from the submitted form
    answers = {key: request.form[key] for key in story.prompts}
    # Generate the story using the answers
    generated_story = story.generate(answers)
    return render_template("story.html", story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
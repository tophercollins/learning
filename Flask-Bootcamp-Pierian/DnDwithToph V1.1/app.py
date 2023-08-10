from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/adventures')
def adventures():
    return render_template('adventures.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/trialclass')
def trialclass():
    return render_template('trialclass.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

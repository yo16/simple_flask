from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('default.html')

if __name__=='__main__':
    app.config.from_object('config')
    app.run(debug=app.config['DEBUG'])

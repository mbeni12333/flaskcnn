from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  return render_template('/index.html')


@app.route('/predict', methods=['POST'])
def predict():
    return 'khra'
if __name__ == "__main__":
    app.run()

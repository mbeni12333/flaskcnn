from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  return render_template('/index.html')


@app.route('/predict', methods=['POST'])
def predict():
    return 'khra'
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, request
from algo import recipe_tranlate

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/', methods=['POST'])
def translate():
    return recipe_tranlate(request.data.decode("utf-8"))

if __name__ == '__main__':
  app.run(debug=True)

# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Estudiante: Andres Murillo. Esta es mi versión esqueleto del proyecto!'

if __name__ == '__main__':
    app.run(debug=True)

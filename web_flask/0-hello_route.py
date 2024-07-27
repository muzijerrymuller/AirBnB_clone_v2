#!/usr/bin/python3

"""
installs a flask programme
ensures that its listening on 0.0.0.0 and on port 5000
displays 'Hello HBNB'
"""

from flast import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def first():
    """
    routing
    """
    return 'Hello HBNB!'

if __name__ = '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request
from flask_cors import CORS
from utils import search_engine

app = Flask(__name__)
CORS(app)
@app.route('/api', methods=['GET'])
def search_api():
    query_param = request.args.get('query')
    if query_param is None:
        return 'Error: No string parameter provided', 400
    return search_engine(query_param)

if __name__ == '__main__':
    app.run(debug=True)
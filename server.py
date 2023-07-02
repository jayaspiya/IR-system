from flask import Flask, request
from utils import search_engine

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def search_api():
    query_param = request.args.get('query')
    if query_param is None:
        return 'Error: No string parameter provided', 400
    results = search_engine(query_param)
    return results

if __name__ == '__main__':
    app.run(debug=False)
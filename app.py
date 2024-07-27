from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model import perform_summarization  # Import the correct function

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    article_text = data.get('article')
    if not article_text:
        return jsonify({'error': 'No article text provided'}), 400
    
    # Call your TextRank summarization function
    summary = perform_summarization(article_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)

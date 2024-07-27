from flask import Flask, request, jsonify
from flask_cors import CORS
# Import your TextRank summarization function here
# from summarizer import summarize_article

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    article_text = data.get('article')
    if not article_text:
        return jsonify({'error': 'No article text provided'}), 400
    
    # Call your TextRank summarization function
    summary = summarize_article(article_text)
    return jsonify({'summary': summary})

def summarize_article(article):
    # Dummy summary function for demonstration
    # Replace this with your actual TextRank summarization logic
    return "This is a summary of the article."

if __name__ == '__main__':
    app.run(debug=True)

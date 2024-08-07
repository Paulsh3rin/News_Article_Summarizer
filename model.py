import nltk
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

# Uncomment these lines to download NLTK resources if not already done
#nltk.download('punkt')
#nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    processed_sentences = []
    
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        words = [word for word in words if word.isalnum() and word not in stop_words]
        processed_sentences.append(' '.join(words))
    
    return sentences, processed_sentences

def build_similarity_matrix(sentences):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def rank_sentences(similarity_matrix):
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)
    return scores

def summarize_text(text, num_sentences=3):
    original_sentences, processed_sentences = preprocess_text(text)
    similarity_matrix = build_similarity_matrix(processed_sentences)
    scores = rank_sentences(similarity_matrix)
    
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(original_sentences)), reverse=True)
    
    summary = ' '.join([sentence for score, sentence in ranked_sentences[:num_sentences]])
    return summary

def extract_keywords_tfidf(text, num_keywords=4):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Use TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(words)])
    feature_array = tfidf_vectorizer.get_feature_names_out()
    
    # Get the sorted indices of the top keywords
    sorted_indices = tfidf_matrix.toarray().argsort(axis=1)[0][::-1]

    # Select the top keywords
    top_keywords = [feature_array[i] for i in sorted_indices[:num_keywords]]
    hashtags = ['#' + keyword for keyword in top_keywords]

    return hashtags

def perform_summarization(text):
    summary = summarize_text(text)
    keywords = extract_keywords_tfidf(text)
    return summary, keywords

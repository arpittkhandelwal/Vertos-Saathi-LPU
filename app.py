"""
Vertos Saathi - Flask Backend Application
An intelligent multi-mode chatbot for LPU students
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# ============= LOAD TRAINED MODELS =============
print("Loading trained models...")

try:
    # Load ML model
    with open('models/chatbot_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✓ Model loaded")
    
    # Load TF-IDF vectorizer
    with open('models/tfidf_vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    print("✓ TF-IDF Vectorizer loaded")
    
    # Load label encoder
    with open('models/label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    print("✓ Label Encoder loaded")
    
    # Load dataset
    with open('models/dataset.pkl', 'rb') as f:
        df = pickle.load(f)
    print("✓ Dataset loaded")
    
    print("\n✅ All models loaded successfully!")
    print(f"📊 Dataset size: {len(df)} Q&A pairs")
    print(f"🎯 Modes available: {', '.join(label_encoder.classes_)}")
    
except Exception as e:
    print(f"\n❌ Error loading models: {e}")
    print("Please run 'python train_model.py' first to train the model.")
    exit(1)

# Download NLTK data if not already downloaded
try:
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)
except:
    pass

# ============= HELPER FUNCTIONS =============

def preprocess_text(text):
    """
    Preprocess user input text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 2]
    
    # Join tokens back
    return ' '.join(tokens)

def detect_mode(question):
    """
    Detect the mode/intent from user question using ML model
    Returns: (mode_name, confidence_score)
    """
    # Preprocess the question
    processed_question = preprocess_text(question)
    
    # Transform using TF-IDF
    question_vector = tfidf.transform([processed_question])
    
    # Predict mode
    prediction = model.predict(question_vector)[0]
    
    # Get probability scores
    probabilities = model.predict_proba(question_vector)[0]
    confidence = max(probabilities)
    
    # Decode label to mode name
    mode_name = label_encoder.inverse_transform([prediction])[0]
    
    return mode_name, confidence

def get_best_answer(question, mode=None):
    """
    Get the best matching answer for the question
    If mode is specified, search only within that mode
    Otherwise, auto-detect mode first
    """
    # Auto-detect mode if not specified
    if mode is None or mode == 'auto':
        detected_mode, confidence = detect_mode(question)
        mode = detected_mode
    else:
        confidence = 1.0  # User selected mode manually
    
    # Filter dataset by mode
    mode_df = df[df['Mode'] == mode]
    
    if len(mode_df) == 0:
        return "Sorry, I don't have information about that mode.", mode, 0.0
    
    # Preprocess user question
    processed_question = preprocess_text(question)
    
    # Preprocess all questions in the mode
    mode_questions = mode_df['processed_question'].tolist()
    
    # Create TF-IDF vectors
    all_questions = [processed_question] + mode_questions
    vectors = tfidf.transform(all_questions)
    
    # Calculate cosine similarity
    user_vector = vectors[0]
    question_vectors = vectors[1:]
    similarities = cosine_similarity(user_vector, question_vectors)[0]
    
    # Get best match
    best_idx = np.argmax(similarities)
    best_similarity = similarities[best_idx]
    
    # Threshold for similarity
    if best_similarity < 0.1:
        return f"Sorry, I don't have enough information about that in {mode} mode. Please try rephrasing your question or contact the university for specific details.", mode, best_similarity
    
    # Get the answer
    answer = mode_df.iloc[best_idx]['Answer']
    
    return answer, mode, best_similarity

# ============= ROUTES =============

@app.route('/')
def home():
    """
    Serve the main chatbot UI
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests from frontend
    Expects JSON: {"message": "user question", "mode": "optional mode"}
    Returns JSON: {"response": "answer", "mode": "detected/used mode", "confidence": score}
    """
    try:
        # Get user message and mode
        data = request.get_json()
        user_message = data.get('message', '').strip()
        selected_mode = data.get('mode', 'auto')
        
        # Validate input
        if not user_message:
            return jsonify({
                'response': 'Please enter a question.',
                'mode': 'error',
                'confidence': 0.0
            })
        
        # Get answer
        answer, mode, confidence = get_best_answer(user_message, selected_mode)
        
        # Return response
        return jsonify({
            'response': answer,
            'mode': mode,
            'confidence': float(confidence)
        })
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({
            'response': 'Sorry, I encountered an error processing your request. Please try again.',
            'mode': 'error',
            'confidence': 0.0
        }), 500

@app.route('/modes', methods=['GET'])
def get_modes():
    """
    Get list of available modes
    """
    modes = label_encoder.classes_.tolist()
    return jsonify({'modes': modes})

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'model_loaded': True,
        'total_qa_pairs': len(df),
        'modes': len(label_encoder.classes_)
    })

# ============= MAIN =============

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting Vertos Saathi Chatbot Server")
    print("="*60)
    print("📍 Server running at: http://localhost:5000")
    print("📝 Open browser and navigate to the URL above")
    print("💬 Try asking questions about LPU!")
    print("="*60 + "\n")
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

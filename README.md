# Vertos Saathi - LPU Intelligent Chatbot

**An AI-powered multi-mode chatbot for Lovely Professional University students**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)
![ML](https://img.shields.io/badge/ML-Naive%20Bayes-orange.svg)
![License](https://img.shields.io/badge/License-Academic-yellow.svg)

---

## 📖 Overview

Vertos Saathi is an intelligent chatbot system designed to help LPU students quickly find answers to college-related queries. The chatbot covers 5 distinct modes:

1. **📚 Academic Mode** - Courses, exams, attendance, CGPA
2. **📝 Admissions & Administration** - Fees, scholarships, documents  
3. **🏛️ Campus Life** - Hostels, mess, clubs, facilities
4. **💼 Placements & Career** - Companies, internships, preparation
5. **🛡️ Rules & Safety** - Discipline, grievance, safety measures

---

## ✨ Features

- 🤖 **Automatic Mode Detection** using ML (Naive Bayes)
- 🎯 **Manual Mode Selection** for specific queries
- 💬 **Natural Language Understanding** with NLP preprocessing
- ⚡ **Instant Responses** (<1 second)
- 📱 **Responsive UI** (works on mobile, tablet, desktop)
- 🎨 **Modern Design** with gradients and animations
- 🔒 **Privacy-Focused** (no external API calls)
- 📊 **High Accuracy** (85-95% on test set)

---

## 🛠️ Technology Stack

**Backend:**
- Python 3.8+
- Flask 2.3.0
- scikit-learn 1.3.0 (ML)
- NLTK 3.8.1 (NLP)
- pandas 2.0.0

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive design (no frameworks)

**ML Pipeline:**
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier
- Cosine Similarity for answer matching

---

## 📂 Project Structure

```
vertos-saathi/
├── academic_documentation/
│   └── PROJECT_REPORT.md          # Complete academic documentation (15 sections)
├── data/
│   └── dataset.csv                # 150+ Q&A pairs across 5 modes
├── models/                        # (Generated after training)
│   ├── chatbot_model.pkl          # Trained Naive Bayes model
│   ├── tfidf_vectorizer.pkl       # TF-IDF feature extractor
│   ├── label_encoder.pkl          # Mode encoder
│   └── dataset.pkl                # Dataset for answer retrieval
├── static/
│   ├── css/
│   │   └── style.css              # UI styling
│   └── js/
│       └── script.js              # Frontend logic
├── templates/
│   └── index.html                 # Main chatbot interface
├── train_model.py                 # ML model training script
├── app.py                         # Flask backend server
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone/Download the Project

```bash
cd /path/to/vertos-saathi
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train the ML Model

```bash
python train_model.py
```

**Expected Output:**
```
Downloading NLTK data...
============================================================
STEP 1: Loading Dataset
============================================================
✓ Dataset loaded successfully
  Total samples: 150
  Modes: ['Academic' 'Admissions and Administration' 'Campus Life' 
          'Placements and Career' 'Rules Safety and Grievance']
...
✓ Training Accuracy: 96.67%
✓ Testing Accuracy: 90.00%
✅ MODEL TRAINING COMPLETED SUCCESSFULLY!
```

### Step 4: Run the Flask Application

```bash
python app.py
```

**Expected Output:**
```
Loading trained models...
✓ Model loaded
✓ TF-IDF Vectorizer loaded
✓ Label Encoder loaded
✓ Dataset loaded

✅ All models loaded successfully!
============================================================
🚀 Starting Vertos Saathi Chatbot Server
============================================================
📍 Server running at: http://localhost:5000
```

### Step 5: Open in Browser

Navigate to **http://localhost:5000** in your web browser

---

## 💬 Usage

1. **Select a Mode** (or keep "Auto Detect" for automatic mode detection)
2. **Type your question** in the input box
3. **Press Enter** or click the **Send button**
4. **Receive instant answer** with mode badge

### Sample Queries

**Academic:**
- "What is the grading system?"
- "How can I check my attendance?"
- "What is CGPA calculation?"

**Admissions:**
- "What documents are required for admission?"
- "How do I apply for scholarships?"
- "What is the fee structure?"

**Campus Life:**
- "What are the hostel facilities?"
- "What are the mess timings?"
- "What clubs can I join?"

**Placements:**
- "Which companies visit for placements?"
- "What is the placement process?"
- "How to build a good resume?"

**Rules & Safety:**
- "What is the dress code?"
- "How to file a grievance?"
- "What are anti-ragging measures?"

---

## 📊 Model Performance

- **Algorithm:** Multinomial Naive Bayes
- **Features:** TF-IDF (500 features, unigrams + bigrams)
- **Training Accuracy:** 95-98%
- **Testing Accuracy:** 88-93%
- **Dataset Size:** 150 Q&A pairs
- **Modes:** 5 (balanced distribution)

---

## 🎓 Academic Documentation

Complete project report available at:  
**`academic_documentation/PROJECT_REPORT.md`**

Includes all 15 required sections:
1. Abstract
2. Problem Statement
3. Objectives
4. System Architecture
5. Workflow
6. Technology Stack
7. ML Algorithm Explanation
8. Dataset Creation & Preprocessing
9. Model Training & Evaluation
10. User Interface Description
11. Use Case Scenarios
12. Advantages
13. Limitations
14. Future Scope
15. Conclusion

---

## 🧪 Testing

### Automated Testing

Run the training script to see model evaluation:
```bash
python train_model.py
```

View classification report, confusion matrix, and accuracy scores.

### Manual Testing

Start the server and test queries for all 5 modes to verify accurate responses.

---

## 🔧 Customization

### Adding New Q&A Pairs

1. Open `data/dataset.csv`
2. Add new rows with format: `mode,question,answer`
3. Retrain the model: `python train_model.py`
4. Restart the server: `python app.py`

### Changing UI Colors/Styling

Edit `static/css/style.css` to customize colors, fonts, and layout.

### Modifying Modes

To add/remove modes:
1. Update `dataset.csv` with new mode names
2. Retrain model
3. Update mode buttons in `templates/index.html`

---

## 🚨 Troubleshooting

### Issue: "FileNotFoundError: models/chatbot_model.pkl"
**Solution:** Run `python train_model.py` first to train and save models

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Install dependencies: `pip install -r requirements.txt`

### Issue: NLTK data not found
**Solution:** The script auto-downloads NLTK data, but if issues persist:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### Issue: Port 5000 already in use
**Solution:** Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## 📈 Future Enhancements

- [ ] Integration with LPU UMS/ERP systems
- [ ] Multilingual support (Hindi, Punjabi)
- [ ] Voice input/output
- [ ] Mobile app (Android/iOS)
- [ ] Deep learning models (LSTM, BERT)
- [ ] Conversation memory and context
- [ ] Admin dashboard for analytics
- [ ] Database migration (SQLite/PostgreSQL)

See **Section 14 (Future Scope)** in PROJECT_REPORT.md for detailed roadmap.

---

## 📝 License

This is an academic project developed for educational purposes. All information is sourced from publicly available LPU resources. Not for commercial use.

---

## 👥 Contributors

Developed as Final Year Engineering Project  
**Lovely Professional University**

---

## 📧 Contact

For official LPU information, visit: **https://www.lpu.in**

---

## ⭐ Acknowledgments

- LPU for providing the problem context
- Scikit-learn and NLTK communities
- Flask framework developers
- Open-source contributors

---

**Built with ❤️ for LPU Students**

---

## 📸 Screenshots

(UI screenshots can be added here after running the application)

---

**Happy Querying! 🚀**

/**
 * Vertos Saathi - Clean & Fixed JavaScript
 */

// Global variables
let currentMode = 'auto';
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const modeBtns = document.querySelectorAll('.mode-btn');
const suggestionPills = document.querySelectorAll('.suggestion-pill');
const themeToggle = document.getElementById('themeToggle');
const quickActionBtns = document.querySelectorAll('.quick-action-btn');

// ===== MODE SELECTION =====
modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        modeBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentMode = btn.dataset.mode;
        console.log('Mode selected:', currentMode);
    });
});

// ===== SEND MESSAGE =====
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Display user message
    appendMessage(message, 'user');
    userInput.value = '';

    // Show typing indicator
    showTypingIndicator();

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message, mode: currentMode })
        });

        const data = await response.json();
        removeTypingIndicator();
        appendMessage(data.response, 'bot', data.mode);

    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        appendMessage('Sorry, I encountered an error. Please try again.', 'bot', 'error');
    }
}

// ===== MESSAGE DISPLAY =====
function appendMessage(text, sender, mode = null) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', `${sender}-message`);

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');

    // Mode badge
    if (sender === 'bot' && mode && mode !== 'auto' && mode !== 'error') {
        const badge = document.createElement('div');
        badge.classList.add('mode-badge');
        badge.textContent = `📍 ${mode}`;
        contentDiv.appendChild(badge);
    }

    // Message text
    const textSpan = document.createElement('span');
    textSpan.innerHTML = formatMessage(text);
    contentDiv.appendChild(textSpan);

    // Copy button for bot messages
    if (sender === 'bot' && mode !== 'error') {
        const copyBtn = document.createElement('button');
        copyBtn.classList.add('copy-btn');
        copyBtn.textContent = '📋 Copy';
        copyBtn.onclick = () => copyToClipboard(text, copyBtn);
        contentDiv.appendChild(copyBtn);
    }

    // Feedback buttons for bot messages
    if (sender === 'bot' && mode !== 'error') {
        const messageId = Date.now().toString();
        const feedbackDiv = addFeedbackButtons(messageId);
        contentDiv.appendChild(feedbackDiv);
    }

    // Timestamp
    const timestamp = document.createElement('span');
    timestamp.classList.add('message-time');
    timestamp.textContent = getCurrentTime();
    contentDiv.appendChild(timestamp);

    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);

    // Show related questions
    if (sender === 'bot' && mode && mode !== 'auto' && mode !== 'error') {
        showRelatedQuestions(mode);
    }

    scrollToBottom();
}

function formatMessage(text) {
    return text.replace(/\n/g, '<br>');
}

// ===== FEEDBACK SYSTEM =====
let feedbackData = JSON.parse(localStorage.getItem('feedbackData')) || {};

function addFeedbackButtons(messageId) {
    const feedbackDiv = document.createElement('div');
    feedbackDiv.classList.add('feedback-buttons');

    const thumbsUp = document.createElement('button');
    thumbsUp.classList.add('feedback-btn', 'thumbs-up');
    thumbsUp.innerHTML = '👍 Helpful';
    thumbsUp.onclick = () => giveFeedback(messageId, 'positive', thumbsUp, feedbackDiv);

    const thumbsDown = document.createElement('button');
    thumbsDown.classList.add('feedback-btn', 'thumbs-down');
    thumbsDown.innerHTML = '👎 Not Helpful';
    thumbsDown.onclick = () => giveFeedback(messageId, 'negative', thumbsDown, feedbackDiv);

    feedbackDiv.appendChild(thumbsUp);
    feedbackDiv.appendChild(thumbsDown);

    if (feedbackData[messageId]) {
        const votedBtn = feedbackData[messageId] === 'positive' ? thumbsUp : thumbsDown;
        votedBtn.classList.add('active');
        thumbsUp.disabled = true;
        thumbsDown.disabled = true;
    }

    return feedbackDiv;
}

function giveFeedback(messageId, type, button, container) {
    button.classList.add('active');
    const allBtns = container.querySelectorAll('.feedback-btn');
    allBtns.forEach(btn => btn.disabled = true);

    feedbackData[messageId] = type;
    localStorage.setItem('feedbackData', JSON.stringify(feedbackData));

    button.innerHTML = type === 'positive' ? '✓ Thank you!' : '✓ Noted';
}

// ===== RELATED QUESTIONS =====
const relatedQuestionsData = {
    'Academic': [
        'How to apply for re-evaluation?',
        'What is the credit system?',
        'When are semester exams?'
    ],
    'Admissions and Administration': [
        'What is admission eligibility?',
        'What documents are required?',
        'What are scholarship criteria?'
    ],
    'Campus Life': [
        'What are mess timings?',
        'What clubs can I join?',
        'What sports facilities are available?'
    ],
    'Placements and Career': [
        'What is average package?',
        'How to prepare for placements?',
        'What is placement process?'
    ],
    'Rules Safety and Grievance': [
        'What is the dress code?',
        'What are anti-ragging measures?',
        'How to file a grievance?'
    ]
};

function showRelatedQuestions(mode) {
    const container = document.getElementById('relatedQuestions');
    const list = document.getElementById('relatedQuestionsList');

    list.innerHTML = '';

    const questions = relatedQuestionsData[mode] || [];

    if (questions.length > 0) {
        const selectedQuestions = questions.sort(() => 0.5 - Math.random()).slice(0, 3);

        selectedQuestions.forEach(question => {
            const item = document.createElement('div');
            item.classList.add('related-question-item');
            item.textContent = question;
            item.onclick = () => {
                userInput.value = question;
                userInput.focus();
                container.style.display = 'none';
                sendMessage();
            };
            list.appendChild(item);
        });

        container.style.display = 'block';
        setTimeout(() => container.style.display = 'none', 30000);
    } else {
        container.style.display = 'none';
    }
}

// ===== TYPING INDICATOR =====
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.classList.add('message', 'bot-message');
    typingDiv.id = 'typingIndicator';

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content', 'typing-indicator');

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.classList.add('typing-dot');
        contentDiv.appendChild(dot);
    }

    typingDiv.appendChild(contentDiv);
    chatMessages.appendChild(typingDiv);
    scrollToBottom();
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) indicator.remove();
}

// ===== UTILITY FUNCTIONS =====
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    });
}

function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(() => {
        const original = button.textContent;
        button.textContent = '✅ Copied!';
        button.style.background = '#10b981';
        button.style.color = 'white';

        setTimeout(() => {
            button.textContent = original;
            button.style.background = '';
            button.style.color = '';
        }, 2000);
    }).catch(() => {
        button.textContent = '❌ Failed';
        setTimeout(() => button.textContent = '📋 Copy', 2000);
    });
}

// ===== DARK MODE =====
const savedTheme = localStorage.getItem('theme') || 'light';
if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    document.querySelector('.theme-icon').textContent = '☀️';
}

themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    const icon = document.querySelector('.theme-icon');

    icon.textContent = isDark ? '☀️' : '🌙';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

// ===== QUICK ACTIONS =====
quickActionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        userInput.value = btn.dataset.action;
        userInput.focus();
        sendMessage();
    });
});

// ===== EVENT LISTENERS =====
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

suggestionPills.forEach(pill => {
    pill.addEventListener('click', () => {
        userInput.value = pill.textContent;
        userInput.focus();
    });
});

// ===== INITIALIZATION =====
window.addEventListener('load', () => {
    userInput.focus();
    scrollToBottom();
    console.log('✅ Vertos Saathi initialized successfully!');
});

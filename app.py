from flask import Flask, render_template, request, jsonify
import random
import json
from datetime import datetime

app = Flask(__name__)

class AivaChatbot:
    def __init__(self):
        self.name = "Aiva"
        self.responses = {
            "greeting": [
                "Hello! I'm Aiva, your virtual assistant. How can I help you today?",
                "Hi there! I'm Aiva. What can I do for you?",
                "Greetings! I'm Aiva, ready to assist you. What's on your mind?"
            ],
            "farewell": [
                "Goodbye! It was nice chatting with you. Have a great day!",
                "See you later! Feel free to come back anytime.",
                "Bye! Take care and don't hesitate to return if you need help."
            ],
            "thanks": [
                "You're welcome! I'm always here to help.",
                "My pleasure! Is there anything else I can assist you with?",
                "Happy to help! What else would you like to know?"
            ],
            "how_are_you": [
                "I'm doing great, thanks for asking! I'm always ready to help you.",
                "I'm functioning perfectly! Ready to assist you with whatever you need.",
                "I'm excellent! Always here and ready to chat."
            ],
            "default": [
                "That's interesting! Tell me more about that.",
                "I see. Could you elaborate on that?",
                "Hmm, let me think about that. Can you provide more details?",
                "That's a good question! Let me help you with that.",
                "I understand. How can I assist you further with this?"
            ]
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Greeting patterns
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(self.responses["greeting"])
        
        # Farewell patterns
        elif any(word in user_input for word in ['bye', 'goodbye', 'see you', 'farewell']):
            return random.choice(self.responses["farewell"])
        
        # Thanks patterns
        elif any(word in user_input for word in ['thank', 'thanks', 'appreciate']):
            return random.choice(self.responses["thanks"])
        
        # How are you patterns
        elif any(word in user_input for word in ['how are you', 'how do you do', 'how are you doing']):
            return random.choice(self.responses["how_are you"])
        
        # Name inquiry
        elif any(word in user_input for word in ['what is your name', 'who are you', 'your name']):
            return f"I'm {self.name}, your friendly chatbot assistant!"
        
        # Time inquiry
        elif any(word in user_input for word in ['time', 'current time']):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}."
        
        # Date inquiry
        elif any(word in user_input for word in ['date', 'today', "what's today", 'current date']):
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today's date is {current_date}."
        
        # Help inquiry
        elif any(word in user_input for word in ['help', 'what can you do', 'abilities']):
            return "I can chat with you, answer basic questions, tell you the time and date, and provide general assistance. I'm continuously learning to better serve you!"
        
        # Default response
        else:
            return random.choice(self.responses["default"])

# Initialize chatbot
chatbot = AivaChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        bot_response = chatbot.get_response(user_message)
        
        response_data = {
            'message': bot_response,
            'timestamp': datetime.now().strftime("%I:%M %p")
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({'error': 'An error occurred processing your request'}), 500

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'chatbot': 'Aiva'})

if __name__ == '__main__':
    print("Starting Aiva Chatbot Server...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

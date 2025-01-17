from flask import Flask, request, jsonify, render_template, session
from flask_mysqldb import MySQL  # Update this import
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # This is needed for session to work

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'bankdb'

mysql = MySQL(app)

# Load chatbot logic
from chatbot_logic import chatbot_response

@app.route('/')
def home():
    return render_template('bank.html')  # Your frontend template

@app.route('/set_account', methods=['POST'])
def set_account():
    account_number = request.json.get('account_number')
    session['account_number'] = account_number
    return jsonify({"message": "Account number found successfully."})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    account_number = session.get('account_number', None)

    if account_number is None:
        return jsonify({"response": "Please provide your account number first."})

    response = chatbot_response(user_message, mysql, account_number)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import ai as aistory
from ai import start_ai_program
import os
from datetime import datetime

app = Flask(__name__)

LOGS_FOLDER = "logs"
LOG_FILE_NAME = "session_logs.txt"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_ai_program', methods=['GET'])
def start_ai_program_route():
    result = start_ai_program()
    return result

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']

    
    log_data(user_input)

    res = aistory.getNewAIMessage(user_input)

    
    log_data(res)

    return res

def log_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(LOGS_FOLDER, LOG_FILE_NAME)

    os.makedirs(LOGS_FOLDER, exist_ok=True)

    with open(log_file_path, 'a') as file:
        file.write(f"{timestamp}: {data}\n")

if __name__ == '__main__':
    app.run(debug=True)

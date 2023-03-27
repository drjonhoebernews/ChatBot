from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
CORS(app)

chatbot = ChatBot('Türkçe Chatbot')
trainer = ChatterBotCorpusTrainer(chatbot)
current_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_directory, "chatterbot_corpus", "data", "turkish")
trainer.train(data_directory)


@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.json['user_input']
    response = chatbot.get_response(user_input)
    return jsonify(str(response))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import rlcard
from rlcard.agents import CFRAgent

app = Flask(__name__)

env = None
ai_agent = None
game_over = False

@app.route('/new_game', methods=['POST'])
def new_game():
    global env, ai_agent, game_over

    env = rlcard.make('leduc-holdem')
    ai_agent = CFRAgent(env)
    ai_agent.load()

    game_over = False

    return jsonify({
        'status': 0,
        'message': 'new game created'
    })

@app.route('/step', methods=['POST'])
def step():
    data = request.json

    return jsonify({
        'status': 0,
        'message': 'step received',
        'received_data': data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
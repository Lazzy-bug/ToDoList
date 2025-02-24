from flask import Flask, request, jsonify, render_template
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

todos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    app.logger.debug("Fetching todos")
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    try:
        todo = request.json.get('todo')
        time = request.json.get('time')
        if not todo or not time:
            raise ValueError("Todo or time not provided")
        timestamp = datetime.strptime(time, '%Y-%m-%dT%H:%M')
        todos.append({'task': todo, 'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S')})
        app.logger.debug(f"Added todo: {todo} at {timestamp}")
        return jsonify({'message': 'Todo added successfully'}), 201
    except Exception as e:
        app.logger.error(f"Error adding todo: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        if 0 <= todo_id < len(todos):
            removed_todo = todos.pop(todo_id)
            app.logger.debug(f"Deleted todo: {removed_todo}")
            return jsonify({'message': 'Todo deleted successfully'})
        return jsonify({'message': 'Todo not found'}), 404
    except Exception as e:
        app.logger.error(f"Error deleting todo: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

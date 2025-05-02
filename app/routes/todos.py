from flask import Blueprint, request, jsonify
from app.models import Todo
from app.extensions import db

todos_bp = Blueprint('todos',__name__)

@todos_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{
        'id': todo.id, 
        'content': todo.content, 
        'completed': todo.completed
        } for todo in todos])

@todos_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = Todo(content=data['content'])
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'id': todo.id, 
        'content': todo.content, 
        'completed': todo.completed
        }), 201

@todos_bp.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({
        'message': 'Todo deleted'
        }), 200

@todos_bp.route('/todos/<int:id>/toggle-completed', methods=['PUT'])
def toggle_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return jsonify({
        'id': todo.id, 
        'content': todo.content, 
        'completed': todo.completed,
        'message': 'Todo completion status updated'
        }), 200
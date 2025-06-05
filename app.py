from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from sudoku_solver import SudokuSolver

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.get_json()
        board = data.get('board')

        if not board or len(board) != 9 or any(len(row) != 9 for row in board):
            return jsonify({'error': 'Invalid board format'}), 400

        solver = SudokuSolver(board)
        solution = solver.get_solution()

        if solution:
            return jsonify({'solution': solution})
        else:
            return jsonify({'error': 'No solution exists for this puzzle'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

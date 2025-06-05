// Create the Sudoku grid
function createGrid() {
    const grid = document.getElementById('sudokuGrid');
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            const input = document.createElement('input');
            input.type = 'text';
            input.maxLength = 1;
            input.dataset.row = i;
            input.dataset.col = j;
            
            // Only allow numbers 1-9
            input.addEventListener('input', function(e) {
                const value = e.target.value;
                if (value && (!/^[1-9]$/.test(value))) {
                    e.target.value = '';
                }
            });
            
            cell.appendChild(input);
            grid.appendChild(cell);
        }
    }
}

// Get the current board state
function getBoard() {
    const board = Array(9).fill().map(() => Array(9).fill(0));
    const inputs = document.querySelectorAll('.cell input');
    
    inputs.forEach(input => {
        const row = parseInt(input.dataset.row);
        const col = parseInt(input.dataset.col);
        const value = input.value;
        board[row][col] = value ? parseInt(value) : 0;
    });
    
    return board;
}

// Update the grid with the solution
function updateGrid(solution) {
    const inputs = document.querySelectorAll('.cell input');
    inputs.forEach(input => {
        const row = parseInt(input.dataset.row);
        const col = parseInt(input.dataset.col);
        input.value = solution[row][col];
    });
}

// Solve the Sudoku puzzle
async function solveSudoku() {
    const board = getBoard();
    const messageDiv = document.getElementById('message');
    
    try {
        const response = await fetch('/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ board: board })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            updateGrid(data.solution);
            messageDiv.textContent = '';
        } else {
            messageDiv.textContent = data.error || 'An error occurred';
        }
    } catch (error) {
        messageDiv.textContent = 'Failed to connect to the server';
    }
}

// Clear the grid
function clearGrid() {
    const inputs = document.querySelectorAll('.cell input');
    inputs.forEach(input => {
        input.value = '';
    });
    document.getElementById('message').textContent = '';
}

// Initialize the grid when the page loads
document.addEventListener('DOMContentLoaded', createGrid); 
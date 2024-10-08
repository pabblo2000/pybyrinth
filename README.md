
# Maze Solver Library

A Python library for creating, solving, and visualizing mazes using Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Reading a Maze](#reading-a-maze)
  - [Solving a Maze](#solving-a-maze)
  - [Printing the Maze](#printing-the-maze)
  - [Generating an Image](#generating-an-image)
- [API Reference](#api-reference)
  - [Classes](#classes)
    - [Maze](#maze)
    - [Node](#node)
    - [StackFrontier](#stackfrontier)
    - [QueueFrontier](#queuefrontier)
  - [Functions](#functions)
    - [`read(filepath)`](#readfilepath)
- [Example](#example)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **Read Mazes from Text Files**: Easily load mazes defined in simple text formats.
- **Solve Mazes**: Utilize DFS or BFS algorithms to find solutions.
- **Visualize Mazes**: Generate image representations of mazes, including solution paths and explored nodes.
- **Immutable Original Maze**: Solving a maze returns a new instance, keeping the original maze unaltered.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tu-usuario/maze-solver.git
   cd maze-solver
   ```

2. **Install Dependencies**

   Ensure you have Python 3.6 or later installed. Install the required Python packages using `pip`:

   ```bash
   pip install Pillow
   ```

   *Note: The library uses the `Pillow` library for image generation.*

3. **Add to Your Project**

   You can copy the `maze.py` file into your project directory or install it as a package if you plan to distribute it.

## Usage

### Reading a Maze

Load a maze from a text file using the `read` function.

```python
import maze as mz

# Replace 'ruta/maze.txt' with the path to your maze file
maze = mz.read('ruta/maze.txt')
```

### Solving a Maze

Solve the maze using either Depth-First Search (DFS) or Breadth-First Search (BFS).

```python
# Solve using Depth-First Search
maze_solved_DFS = maze.solve(method='DFS')

# Solve using Breadth-First Search
maze_solved_BFS = maze.solve(method='BFS')
```

### Printing the Maze

Print the maze to the console. The original maze remains unsolved.

```python
print("Laberinto Original:")
print(maze)

print("
Laberinto Resuelto con DFS:")
print(maze_solved_DFS)
```

### Generating an Image

Generate an image of the maze, highlighting the solution path and explored cells.

```python
# Generate image for the solved maze with explored cells
maze_solved_DFS.output_image('maze_solution_DFS.png', show_explored=True)

# Generate image without showing explored cells
maze_solved_BFS.output_image('maze_solution_BFS.png', show_explored=False)
```

## API Reference

### Classes

#### `Maze`

Represents a maze loaded from a text file.

- **Initialization**

  ```python
  maze = Maze(filename)
  ```

  - `filename` (str): Path to the maze text file.

- **Methods**

  - `solve(method="DFS")`  
    Solves the maze using the specified method.
    
    - `method` (str): `'DFS'` for Depth-First Search or `'BFS'` for Breadth-First Search.
    - **Returns**: A new `Maze` instance with the solution.

  - `output_image(filename, show_solution=True, show_explored=False)`  
    Generates an image of the maze.
    
    - `filename` (str): Output image file name (e.g., `'maze.png'`).
    - `show_solution` (bool): Whether to display the solution path.
    - `show_explored` (bool): Whether to display the explored cells.

  - `__str__()`  
    Returns a string representation of the maze, suitable for printing.

#### `Node`

Represents a node in the search tree.

- **Initialization**

  ```python
  node = Node(state, parent, action)
  ```

  - `state` (tuple): The current position in the maze (row, column).
  - `parent` (`Node` or `None`): The parent node.
  - `action` (str): The action taken to reach this node (e.g., `'up'`, `'down'`).

#### `StackFrontier`

Implements a stack-based frontier for DFS.

- **Methods**

  - `add(node)`  
    Adds a node to the frontier.
  
  - `contains_state(state)`  
    Checks if a state is already in the frontier.
  
  - `empty()`  
    Checks if the frontier is empty.
  
  - `remove()`  
    Removes and returns the last node added.

#### `QueueFrontier`

Inherits from `StackFrontier` and implements a queue-based frontier for BFS.

- **Methods**

  - `remove()`  
    Removes and returns the first node added.

### Functions

#### `read(filepath)`

Reads a maze from a file and returns a `Maze` instance.

```python
maze = read(filepath)
```

- `filepath` (str): Path to the maze text file.
- **Returns**: `Maze` instance.

## Example

Here's a complete example demonstrating how to use the library:

```python
import maze as mz

# Leer el laberinto desde un archivo
maze = mz.read("mazes/maze2.txt")

# Resolver el laberinto usando DFS
maze_solved_DFS = maze.solve(method='DFS')

# Resolver el laberinto usando BFS
maze_solved_BFS = maze.solve(method='BFS')

# Imprimir el laberinto original
print("Laberinto Original:")
print(maze)

# Imprimir el laberinto resuelto con DFS
print("
Laberinto Resuelto con DFS:")
print(maze_solved_DFS)

# Imprimir el laberinto resuelto con BFS
print("
Laberinto Resuelto con BFS:")
print(maze_solved_BFS)

# Generar una imagen del laberinto resuelto mostrando las celdas exploradas
maze_solved_DFS.output_image('maze_solution_DFS.png', show_explored=True)
maze_solved_BFS.output_image('maze_solution_BFS.png', show_explored=True)
```

**Expected Output:**

- **Console Output**:
  - Original maze without any solution.
  - Maze with the DFS solution path.
  - Maze with the BFS solution path.

- **Generated Images**:
  - `maze_solution_DFS.png`: Visual representation of the maze solved using DFS, highlighting the solution path and explored cells.
  - `maze_solution_BFS.png`: Visual representation of the maze solved using BFS, highlighting the solution path and explored cells.

## Dependencies


- **Python 3.6 or later**
- **Pillow**: For image generation.

  Install via pip:

  ```bash
  pip install Pillow
  ```

## License

This project is licensed under the [MIT License](LICENSE).


## Contact

For any questions or suggestions, feel free to open an issue or contact [palvaroh2000@gmail.com](mailto:palvaroh2000@gmail.com).

---

*¡Gracias por usar el Maze Solver Library! Esperamos que te sea de gran utilidad para tus proyectos de resolución de laberintos.*

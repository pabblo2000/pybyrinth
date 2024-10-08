# maze.py

import copy  # Importamos el módulo copy para hacer copias profundas

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return not self.frontier

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            return self.frontier.pop()


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            return self.frontier.pop(0)


class Maze:
    def __init__(self, filename):
        # Leer el archivo y configurar el laberinto
        with open(filename) as f:
            contents = f.read()

        # Validar punto de inicio y objetivo
        if contents.count("A") != 1:
            raise Exception("El laberinto debe tener exactamente un punto de inicio 'A'")
        if contents.count("B") != 1:
            raise Exception("El laberinto debe tener exactamente un punto objetivo 'B'")

        # Determinar altura y anchura
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Crear la cuadrícula de paredes
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def __str__(self):
        output = []
        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            line = ""
            for j, col in enumerate(row):
                if col:
                    line += "█"
                elif (i, j) == self.start:
                    line += "A"
                elif (i, j) == self.goal:
                    line += "B"
                elif solution and (i, j) in solution:
                    line += "*"
                else:
                    line += " "
            output.append(line)
        return "\n".join(output)

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        result = []
        for action, (r, c) in candidates:
            if (
                0 <= r < self.height
                and 0 <= c < self.width
                and not self.walls[r][c]
            ):
                result.append((action, (r, c)))
        return result

    def solve(self, method="DFS"):
        """Encuentra una solución al laberinto usando el método especificado ('DFS' o 'BFS')."""
        # Hacer una copia profunda de la instancia actual
        copy_maze = copy.deepcopy(self)

        # Inicializar contadores y conjuntos
        copy_maze.num_explored = 0
        copy_maze.explored = set()

        # Inicializar frontera
        start_node = Node(state=copy_maze.start, parent=None, action=None)
        if method == "DFS":
            frontier = StackFrontier()
        elif method == "BFS":
            frontier = QueueFrontier()
        else:
            raise ValueError("El método debe ser 'DFS' o 'BFS'")
        frontier.add(start_node)

        while True:
            if frontier.empty():
                raise Exception("No hay solución para este laberinto")

            node = frontier.remove()
            copy_maze.num_explored += 1

            if node.state == copy_maze.goal:
                # Se encontró la solución
                actions = []
                cells = []
                while node.parent:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                copy_maze.solution = (actions, cells)
                return copy_maze  # Devolvemos la copia resuelta

            copy_maze.explored.add(node.state)

            for action, state in copy_maze.neighbors(node.state):
                if not frontier.contains_state(state) and state not in copy_maze.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw

        cell_size = 50
        cell_border = 2
        img = Image.new(
            "RGBA", (self.width * cell_size, self.height * cell_size), "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                elif show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    [
                        (
                            j * cell_size + cell_border,
                            i * cell_size + cell_border,
                        ),
                        (
                            (j + 1) * cell_size - cell_border,
                            (i + 1) * cell_size - cell_border,
                        ),
                    ],
                    fill=fill,
                )

        img.save(filename)


def read(filepath):
    return Maze(filepath)

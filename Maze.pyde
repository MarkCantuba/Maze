WINDOW_HEIGHT = 200
WINDOW_WIDTH = 200
CELL_SIZE = 50
nodes = []
node_stack = []
not_visited = []

def setup():
    global nodes, not_visited, node_stack
    size(WINDOW_WIDTH, WINDOW_HEIGHT)
    background(255)

    for x in range(WINDOW_WIDTH // CELL_SIZE):
        nodes.append([0 for _ in range(WINDOW_WIDTH // CELL_SIZE)])
        for y in range(WINDOW_HEIGHT // CELL_SIZE):
            nodes[x][y] = Node(x, y)
            not_visited.append(nodes[x][y])
            
    current_node = not_visited.pop()
    current_node.visited = True
    
    while len(not_visited) != 0:
        
        neighbors = current_node.get_neighbors()

        if len(neighbors) != 0:
            
            chosen_node = neighbors[int(random(len(neighbors)))]
            node_stack.append(current_node)
            
            if chosen_node.x == current_node.x - 1:
                print()
            if chosen_node.x == current_node.x - 1:
                print()
            if chosen_node.x == current_node.x - 1:
                print()
            if chosen_node.x == current_node.x - 1:
                print()  
            
            current_node = chosen_node
            not_visited.remove(current_node)
            chosen_node.visited = True
        
        elif len(node_stack) != 0:
            current_node = node_stack.pop()
            
        
    
def draw():
    background(255)
    for x in range(WINDOW_WIDTH // CELL_SIZE):
        for y in range(WINDOW_HEIGHT // CELL_SIZE):
            textSize(10)
            fill(0)
            text(str(x) + "," + str(y), x*CELL_SIZE, y*CELL_SIZE+CELL_SIZE)
            
            node = nodes[x][y]
            
            if node.walls[0]:
                line(x*CELL_SIZE,y*CELL_SIZE,x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE)
            if node.walls[1]:
                line(x*CELL_SIZE,y*CELL_SIZE,x*CELL_SIZE, y*CELL_SIZE+CELL_SIZE)
            if node.walls[2]:
                line(x*CELL_SIZE,y*CELL_SIZE+CELL_SIZE,x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE)
            if node.walls[3]:
                line(x*CELL_SIZE+CELL_SIZE,y*CELL_SIZE,x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE)
                

class Node(object):
    def __init__(self, x, y):
        self.walls = [True, True, True, True]
        self.x = x
        self.y = y
        self.visited = False
        
    def get_neighbors(self):
        neighbors = []
        if self.x+1 < WINDOW_WIDTH // CELL_SIZE and not nodes[self.x+1][self.y].visited:
            neighbors.append(nodes[self.x+1][self.y])
        if self.x-1 >= 0 and not nodes[self.x-1][self.y].visited:
            neighbors.append(nodes[self.x-1][self.y])
        if self.y+1 < WINDOW_HEIGHT // CELL_SIZE and not nodes[self.x][self.y+1].visited:
            neighbors.append(nodes[self.x][self.y+1])
        if self.y-1 >= 0 and not nodes[self.x][self.y-1].visited:
            neighbors.append(nodes[self.x][self.y-1])
        return neighbors
    
    def __str__(self):
        return str(self.x) + "," + str(self.y) 

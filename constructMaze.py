from matplotlib import pyplot
from matplotlib import colors #this HURTS me
import globalConstants


def colour_path(maze, path) -> None:
    
    for (x,y) in path:
        maze.board[x][y] = globalConstants.RED

    if len(path):
        maze.board[path[0][0], path[0][1]] = globalConstants.BLUE
        maze.board[path[-1][0], path[-1][1]] = globalConstants.BLUE

        
def draw_maze(maze, path=None, figSize=(20, 10), file_path=None) -> None:
    
    if path is None:
        path = []

    pyplot.figure(figsize=figsize)
    color_path(maze, path)

    cmap = colors.ListedColormap(["black","white","red","blue"])
    bounds = [0,1,2,3,4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    pyplot.imshow(maze.board, interpolation="neareast", cmap=cmap, norm=norm)
    pylot.xticks([])
    pyplot.yticks([])

    if file_path is not None:
        pyplot.savefig(file_path + ".png")
        maze.write_to_file(file_path + ".txt")
    else:
        pyplot.show()
        

def draw_ascii(maze) -> str:
    
    grid = ""
    
    for i in range(maze.nrows):
        
        for j in range(maze.ncolumns):
            
            if maze.is_wall(i, j):
                grid += "X"
            else:
                grid += " "
                
        grid += "\n"
        
    return grid

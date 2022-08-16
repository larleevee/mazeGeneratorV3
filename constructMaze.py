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

from Stack import Stack


def solveMaze(maze, startX, startY):
    stack = Stack()
    stack.push([startX, startY])

    step = 1
    maze[startX][startY] = step

    while not stack.isEmpty():
        current = stack.peek()
        x, y = current[0], current[1]

        # North
        if x > 0 and maze[x - 1][y] in (' ', 'G'):
            nextX, nextY = x - 1, y

        # West
        elif y > 0 and maze[x][y - 1] in (' ', 'G'):
            nextX, nextY = x, y - 1

        # South
        elif x + 1 < len(maze) and maze[x + 1][y] in (' ', 'G'):
            nextX, nextY = x + 1, y

        # East
        elif y + 1 < len(maze[0]) and maze[x][y + 1] in (' ', 'G'):
            nextX, nextY = x, y + 1

        # Dead end: backtrack
        else:
            stack.pop()
            continue

        # Move into the selected position
        stack.push([nextX, nextY])

        if maze[nextX][nextY] == 'G':
            return True

        step += 1
        maze[nextX][nextY] = step

    return False
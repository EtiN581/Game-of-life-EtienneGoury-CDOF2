import tkinter as tk
import random

# Configuration
width = 50
height = 50
cell_size = 10  # Size of each cell in pixels
prob = 0.5  # Probability for a new cell to appear
delay = 100  # Delay in ms

# Initialize space
space = [[True if random.random() < prob else False for _ in range(height)] for _ in range(width)]

# Tkinter setup
root = tk.Tk()
root.title("Conway's Game of Life")
canvas = tk.Canvas(root, width=width * cell_size, height=height * cell_size)
canvas.pack()

def count_neighbors(x, y):
    k = 0
    for i in range(max(0, x-1), min(x+2, width)):
        for j in range(max(0, y-1), min(y+2, height)):
            if (i, j) != (x, y) and space[i][j]:
                k += 1
    return k

def update_cell(x, y, new_space):
    k = count_neighbors(x, y)
    if (not space[x][y] and k == 3) or (space[x][y] and k in [2, 3]):
        new_space[x][y] = True

def draw_space():
    canvas.delete("all")
    for x in range(width):
        for y in range(height):
            color = 'black' if space[x][y] else 'white'
            canvas.create_rectangle(x * cell_size, y * cell_size, (x+1) * cell_size, (y+1) * cell_size, fill=color, outline="")

def toggle_cell(event):
    x, y = event.x // cell_size, event.y // cell_size
    if 0 <= x < width and 0 <= y < height:
        space[x][y] = not space[x][y]
        draw_space()

def update_space():
    global space
    new_space = [[False for _ in range(height)] for _ in range(width)]
    for x in range(width):
        for y in range(height):
            update_cell(x, y, new_space)
    space = new_space
    draw_space()
    if running:
        root.after(delay, update_space)

def start():
    global running
    running = True
    update_space()

def stop():
    global running
    running = False

def reset():
    global space
    space = [[False for _ in range(height)] for _ in range(width)]
    draw_space()

running = False
canvas.bind("<Button-1>", toggle_cell)

# Control buttons
frame = tk.Frame(root)
frame.pack()
start_button = tk.Button(frame, text="Start", command=start)
start_button.pack(side=tk.LEFT)
stop_button = tk.Button(frame, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT)
reset_button = tk.Button(frame, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT)

# Initial drawing of the space
draw_space()

root.mainloop()

from tkinter import *
# матрицы для отрисовки клеток
cell = [[0 for row in range(61)] for col in range(81)]
live = [[0 for row in range(61)] for col in range(81)]
new_generation = [[0 for row in range(61)] for col in range(81)]

def load_from_file():

    f = open('map', 'r')
    for y in range(60):
        line = f.readline()
        line =line.strip()
        for x in range(80):
              live[x][y] = int(line[x])
              new_generation[x][y] = 0
              cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray", fill="black")
    f.close()

def statystic():
    return live == new_generation

def process():
    for y in range(0,60):
        for x in range(0,80):
            lives = live_neighbors(x,y)

            if live[x][y] == 1 and (lives < 2 or lives > 3): new_generation[x][y] = 0
            if live[x][y] == 1 and (lives == 2 or lives == 3): new_generation[x][y] = 1
            if live[x][y] == 0 and lives == 3: new_generation[x][y] = 1

    if statystic(): exit()
    for y in range(60):
        for x in range(80):
            live[x][y] = new_generation[x][y]


def live_neighbors(a,b):
    lives = 0
    for i in range(-1,2):
        for j in range(-1,2):
           if a+i > -1 and a+i < 80 and b+i > -1 and b+i < 60:

             if  i==0 and j==0:
                 pass

             elif live[a+i][b+j] == 1: lives += 1
    return lives


def draw():
    for y in range(60):
        for x in range(80):
            if live[x][y]==0:
                canvas.itemconfig(cell[x][y], fill="black")
            if live[x][y]==1:
                canvas.itemconfig(cell[x][y], fill="green")

def step():
    process()
    draw()
    root.after(10, step)

root = Tk()
root.title("Conway's Game of Life")
canvas = Canvas(root, width=800, height=600, highlightthickness=0, bd=10, bg='black')
canvas.pack() # отображаем его на экране
load_from_file()
step()
root.mainloop()


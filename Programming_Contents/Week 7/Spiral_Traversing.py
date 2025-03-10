import numpy as np
import turtle
import random

turtle.bgcolor("black")
turtwig = turtle.Turtle()

width = 5
height = 5
dot_distance = 25
turtwig.setpos(-300,300)
color_list = ["white","yellow","brown","red","blue","green","orange","pink","violet","grey"]
turtwig.penup()

order = int(input("Enter the size/order: "))
matrix = np.array([i for i in range(1, order**2+1)]).reshape(order, order)
n = order
#print(matrix)

def print_element(arr):
    global dot_distance
    for element in arr:
        #print(element)
        turtwig.color(random.choice(color_list))
        turtwig.dot()
        turtwig.forward(dot_distance)

def spiral(matrix):
    global n, dot_distance
    row_visited = []
    column_visited = []
    round = 0

    while True:
        if round in row_visited:    break
        print_element(matrix[round,round:n-round])
        row_visited.append(round)
        turtwig.right(90)
        if n-round-1 in column_visited:    break
        print_element(matrix[round+1:n-round,n-round-1])
        column_visited.append(round-1)
        turtwig.right(90)
        if n-round-1 in row_visited:    break
        print_element(np.flip(matrix[n-round-1, round:n-round-1]))
        row_visited.append(n-round-1)
        turtwig.right(90)
        if round in column_visited:    break
        print_element(np.flip(matrix[round+1:n-round-1,round]))
        column_visited.append(round)
        turtwig.right(90)

        round += 1

spiral(matrix)
turtle.done()
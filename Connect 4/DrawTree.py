import tkinter as tk
from tkinter import ttk
from tkinter import *
from INode import *


def createTree(nextGen, ans):
    if len(nextGen) == 0:
        return ans
    ans.append([])
    nextStep = []
    for i in nextGen:
        ans[len(ans) - 1].append(i)
        for j in i.children:
            nextStep.append(j)
    return createTree(nextStep, ans)


def createNode(arr):
    ans = ""
    for i in range(len(arr)):
        for char in arr[i]:
            if char == '0':
                ans += "E"
            if char == '1':
                ans += "C"
            if char == '2':
                ans += "P"
        ans += '\n'
    return ans


def drawTree(parent, nextGen, n):
    root = tk.Tk()
    scrollbar = ttk.Scrollbar(root, orient=HORIZONTAL)
    scrollbar.pack(side=BOTTOM, fill=X)
    scrollbar2 = ttk.Scrollbar(root, orient=VERTICAL)
    scrollbar2.pack(side=RIGHT, fill=Y)
    canvas = Canvas(root, width=1500, height=700, xscrollcommand=scrollbar.set, yscrollcommand=scrollbar2.set)
    allFrames = tk.Frame(canvas)
    canvas.create_window((0, 0), window=allFrames, anchor='nw')

    tree = [[parent]]
    tree = createTree(nextGen, tree)

    layers = [] * n
    for i in range(n):
        # for each level create a frame
        layers.append(tk.Frame(allFrames, padx=10, pady=20))
        layers[i].grid(row=i)

        # for each frame add all its nodes
        for j in range(len(tree[i])):
            layers[i].columnconfigure(j, weight=1)
            x = (tk.Label(layers[i], text=createNode(tree[i][j].board), font="20", background='#ff0000', padx=10,
                          highlightbackground="green", borderwidth=10, highlightthickness=5))
            x.grid(row=i, column=j)

    canvas.pack()
    scrollbar.config(command=canvas.xview)
    scrollbar2.config(command=canvas.yview)
    root.mainloop()

# def drawTree():
#     root = tk.Tk()
#     scrollbar = ttk.Scrollbar(root, orient=HORIZONTAL)
#     scrollbar.pack(side=BOTTOM, fill=X)
#     scrollbar2 = ttk.Scrollbar(root, orient=VERTICAL)
#     scrollbar2.pack(side=RIGHT, fill=Y)
#     canvas = Canvas(root, width=1400, height=500, xscrollcommand=scrollbar.set, yscrollcommand=scrollbar2.set)
#
#     allframs = tk.Frame(canvas)
#     canvas.create_window((0, 0), window=allframs, anchor='nw')


#     n = 3
#     frames = [] * n
#     arrofarr = [] * n
#
#     arr = [[0, 0, 0, 1, 2, 0, 0], [0, 0, 0, 1, 2, 0, 0], [0, 0, 0, 1, 2, 0, 0], [0, 0, 0, 1, 2, 0, 0],
#            [0, 0, 0, 1, 2, 0, 0], [0, 0, 0, 1, 2, 0, 0]]
#
#     for i in range(n):
#         frames.append(tk.Frame(allframs, padx=10, pady=20))
#         frames[i].grid(row=i)
#         arrofarr.append([] * 7 ** i)
#         for j in range(7 ** i):
#             frames[i].columnconfigure(j, weight=1)
#             arrofarr[i].append(tk.Label(frames[i], text=createNode(arr), font="20", background='#ff0000', padx=10,
#                                         highlightbackground="green", borderwidth=10, highlightthickness=5))
#             arrofarr[i][j].grid(row=i, column=j)
#
#     # Draw lines connecting parent node to its children
#     canvas.pack()
#     # side="left", fill="both", expand=True
#     # root.update()
#     # for i in range(n):
#     #     for j in range(7 ** i):
#     #         if i > 0:
#     #             parent_node_index = j // 7
#     #             parent_node = arrofarr[i - 1][parent_node_index]
#     #             parent_node_center_x = parent_node.winfo_rootx() + parent_node.winfo_width() / 2
#     #             parent_node_center_y = parent_node.winfo_rooty() + parent_node.winfo_height() / 2
#     #             print(parent_node.winfo_rootx())
#     #             current_node_center_x = arrofarr[i][j].winfo_rootx() + arrofarr[i][j].winfo_width() / 2
#     #             current_node_center_y = arrofarr[i][j].winfo_rooty() + arrofarr[i][j].winfo_height() / 2
#     #
#     #             canvas.create_line(parent_node_center_x, parent_node_center_y, current_node_center_x,
#     #                                current_node_center_y)
#
#     scrollbar.config(command=canvas.xview)
#     scrollbar2.config(command=canvas.yview)
#     root.mainloop()

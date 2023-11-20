import tkinter as tk

YELLOW = "#ffff00"
RED = "#ff0000"


def createNode(node, ab):
    ans = ""
    for i in range(len(node.board)):
        for char in node.board[i]:
            if char == '0':
                ans += "E"
            if char == '1':
                ans += "C"
            if char == '2':
                ans += "P"
        ans += '\n'
    ans += "Heuristic = " + str(node.score)
    if ab:
        ans += '\n'
        ans += "Alpha = " + str(node.alpha)
        ans += "  Beta = " + str(node.beta)
    return ans


def center_window(window, width_percentage, height_percentage):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate window width and height based on percentages
    window_width = int(screen_width * width_percentage)
    window_height = int(screen_height * height_percentage)

    # Calculate x and y coordinates to center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 50

    # Set the geometry of the window
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def drawTree(source, sourceTurn, root, ab):
    if root is not None and source is not None and len(source.children) > 0:
        root.destroy()
    if source is not None and len(source.children) > 0:
        if sourceTurn == 1:
            parentColor = RED
            childColor = YELLOW
        else:
            parentColor = YELLOW
            childColor = RED
        root = tk.Tk()
        root.title("Minimax Tree")
        width_percentage = 0.75
        height_percentage = 0.8
        center_window(root, width_percentage, height_percentage)
        frame1 = tk.Frame(root)
        parentLabel = tk.Label(frame1, text=createNode(source, ab), font="25", background=parentColor, padx=10,
                               borderwidth=10, highlightthickness=5, pady=10)
        parentLabel.grid(row=0, column=0)
        frame1.pack()
        frame2 = tk.Frame(root)
        for i in range(len(source.children)):
            frame2.columnconfigure(i, weight=1)
            x = tk.Label(frame2, text=createNode(source.children[i], ab), font="25", background=childColor, padx=10
                         , borderwidth=10, highlightthickness=5, pady=10)
            x.grid(row=0, column=i)
        frame2.pack()
        frame3 = tk.Frame(root)
        for i in range(len(source.children)):
            button_command = lambda i=i: drawTree(source.children[i], 1 - sourceTurn, root, ab)
            x = ((tk.Button(frame3, text="Next", font="25", background='#339966', padx=35, borderwidth=10,
                            highlightthickness=5, pady=10, command=button_command)))
            x.grid(row=0, column=i)
        frame3.pack()
        frame4 = tk.Frame(root)
        backButton = tk.Button(frame4, text="Back", font="25", background='#339966', padx=10,
                               borderwidth=10, highlightthickness=5, pady=10, command=lambda: drawTree(source.parent,
                                                                                                       1 - sourceTurn,
                                                                                                       root, ab))
        backButton.grid(row=0, column=0)
        frame4.pack()
        frame5 = tk.Frame(root)
        guidAgent = tk.Label(frame5, text="MAX", font="25", background=YELLOW, padx=10, borderwidth=10,
                             highlightthickness=5, pady=10)
        guidAgent.grid(row=0, column=0)
        guidHuman = tk.Label(frame5, text="MIN", font="25", background=RED, padx=10, borderwidth=10,
                             highlightthickness=5, pady=10)
        guidHuman.grid(row=0, column=1)
        frame5.pack()
        root.mainloop()

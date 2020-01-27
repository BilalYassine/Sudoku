import tkinter as tk

# Create instance of tkinter
win = tk.Tk()

win.title("Sudoku Solver")

titleLabel = tk.Label(win, text="Sudoku")
titleLabel.pack()

testButton = tk.Button(win, text="Button")
testButton.pack()

win.mainloop()


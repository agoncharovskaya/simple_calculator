import tkinter as tk
from tkinter import ttk


# window
window = tk.Tk()
window.title('Python Calculator')
window.geometry('300x400')

# grid
window.columnconfigure((0, 1, 2, 3), weight=1)
window.rowconfigure((0, 1, 2, 3, 4), weight=1)

# data
calc_str = tk.StringVar(value='000')

# widgets
num_0 = ttk.Button(window, text='0')
num_1 = ttk.Button(window, text='1')
num_2 = ttk.Button(window, text='2')
num_3 = ttk.Button(window, text='3')
num_4 = ttk.Button(window, text='4')
num_5 = ttk.Button(window, text='5')
num_6 = ttk.Button(window, text='6')
num_7 = ttk.Button(window, text='7')
num_8 = ttk.Button(window, text='8')
num_9 = ttk.Button(window, text='9')

num_plus = ttk.Button(window, text='+')
num_minus = ttk.Button(window, text='-')
num_enter = ttk.Button(window, text='=')
num_clear = ttk.Button(window, text='C', command=lambda: calc_str.set(''))

label = ttk.Label(window, textvariable=calc_str)

# layout
label.grid(column=0, row=0, columnspan=4, sticky='nswe')
num_1.grid(column=0, row=3, sticky='nswe')
num_2.grid(column=1, row=3, sticky='nswe')
num_3.grid(column=2, row=3, sticky='nswe')
num_4.grid(column=0, row=2, sticky='nswe')
num_5.grid(column=1, row=2, sticky='nswe')
num_6.grid(column=2, row=2, sticky='nswe')
num_7.grid(column=0, row=1, sticky='nswe')
num_8.grid(column=1, row=1, sticky='nswe')
num_9.grid(column=2, row=1, sticky='nswe')
num_0.grid(column=0, row=4, sticky='nswe')

num_clear.grid(column=3, row=1, sticky='nswe')
num_enter.grid(column=1, row=4, columnspan=2, sticky='nswe')
num_plus.grid(column=3, row=3, rowspan=2, sticky='nswe')
num_minus.grid(column=3, row=2, sticky='nswe')

# run
window.mainloop()

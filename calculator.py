import tkinter as tk
 
# Create app window
win = tk.Tk()
 
# Specify screen size of the window
win.geometry("312x324")
 
# Disable resizing the app window
win.resizable(0, 0)
 
# Specify app name
win.title("Calculator")
 
input_value = ""
 
# Intialize StringVar
display_text = tk.StringVar()
 
# Function to continuously updates input field whenever you click a button
def click_button(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)
 
# Function to clear the display
def clear_button(): 
    global input_value 
    input_value = "" 
    display_text.set("")
 
# Function to calculate input values 
def equal_button():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""
     
# Create a frame 
input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
  
input_frame.pack(side = tk.TOP)
 
# Create an input field inside the frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable = display_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
  
input_field.grid(row=0, column=0)
  
input_field.pack(ipady=10) 
 
  
buttons_frame = tk.Frame(win, width=312, height=272.5, bg="grey")
  
buttons_frame.pack()
 
# 1st row
clear_button = tk.Button(buttons_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clear_button()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
  
divide_button = tk.Button(buttons_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# 2nd row
button_7 = tk.Button(buttons_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
  
button_8 = tk.Button(buttons_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
  
button_9 = tk.Button(buttons_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
  
multiply_button = tk.Button(buttons_frame, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# 3rd row
button_4 = tk.Button(buttons_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
  
button_5 = tk.Button(buttons_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
  
button_6 = tk.Button(buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
  
minus_button = tk.Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# 4th row
  
button_1 = tk.Button(buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
  
button_2 = tk.Button(buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
  
button_3 = tk.Button(buttons_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
  
plus_button = tk.Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# 5th row
  
button_0 = tk.Button(buttons_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click_button(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
  
point_button = tk.Button(buttons_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click_button(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
  
equals_button = tk.Button(buttons_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: equal_button()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
# Run main loop
win.mainloop()
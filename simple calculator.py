import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        self.expression = ""
        
        # Input field for displaying expressions and results
        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        
        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=14, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()
        
        # Button layout
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        row_val = 0
        col_val = 0
        
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def create_button(self, value, row, column):
        button = tk.Button(self.buttons_frame, text=value, font=('arial', 18, 'bold'), fg='black', width=4, height=2, bd=1, bg='white')
        button.grid(row=row, column=column, padx=1, pady=1)
        
        if value == "=":
            button.bind('<Button-1>', self.calculate)
        elif value == "C":
            button.bind('<Button-1>', self.clear)
        else:
            button.bind('<Button-1>', self.add_to_expression)
    
    def add_to_expression(self, event):
        self.expression += str(event.widget.cget("text"))
        self.input_text.set(self.expression)
    
    def clear(self, event):
        self.expression = ""
        self.input_text.set(self.expression)
    
    def calculate(self, event):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

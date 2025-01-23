import tkinter as tk


def click_button(value):
    
    current = entry.get()
    
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)
def calcular():
    try:
       
        result = eval(entry.get())  
        entry.delete(0, tk.END)  
        entry.insert(tk.END, result)  
    except Exception as e:
        
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")
def limpar():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Calculadora Simples")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]
for (text, row, col) in buttons:
    if text == '=':
        # Para o botão de "=" vamos associar a função de cálculo
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=calcular)
    else:
        # Para os outros botões, associamos a função de adicionar ao visor
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=limpar)
button_clear.grid(row=4, column=3)

root.mainloop()


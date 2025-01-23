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
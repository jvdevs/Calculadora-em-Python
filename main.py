import tkinter as tk


def click_button(value):
    
    current = entry.get()
    
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)
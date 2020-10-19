#!/usr/bin/python3
from tkinter import *
from tkinter.ttk import Scrollbar as ttk_scrollbar

root = Tk() 
root.geometry("350x250") 
root.title("Sticky Note") 
root.minsize(height=250, width=350) 
root.maxsize(height=250, width=350) 

# scrollbar = Scrollbar(root)
scrollbar = ttk_scrollbar(root) 
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.pack_forget()
text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)
with open(".notepad_txt") as f:
    text_info.insert(END, f.read(), "colour") 

def save(event):
    mode = "a" if event else "w"
    with open(".notepad_txt", mode) as f:
        f.write(text_info.get("1.0", "end-1c"))

def on_closing():
    save(None)
    root.destroy()

def select_all(event):
    text_info.tag_add(SEL, "1.0", END)
    text_info.mark_set(INSERT, "1.0")
    text_info.see(INSERT)
    return 'break'

def colour(event):
    if event.char:
        text_info.tag_add("colour",  "1.0", 'end')

scrollbar.config(command=text_info.yview) 
text_info.configure(bg='#2e2e2e', insertbackground="white")
text_info.tag_config('colour', foreground="yellow")
text_info.bind("<FocusOut>", save)
text_info.bind("<Key>", colour)
text_info.bind("<Control-Key-a>", select_all)
root.call('wm', 'attributes', '.', '-topmost', '1')
root.configure(bg='#2e2e2e')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop() 

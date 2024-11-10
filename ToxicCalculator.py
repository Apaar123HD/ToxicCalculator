import tkinter as tk
import requests

#initializes tkinter
root = tk.Tk()
root.title("ToxicCalculator")

#insult api stuff
insultAPI = requests.get("https://insult.mattbas.org/api/insult")
insult = insultAPI.text

text_inserting = str()

intro = tk.Label(root, text="Welcome to ToxicCalculator, where we do really just hate you.")
intro.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def enter_click():
    entering.destroy()
    intro.destroy()
    text_field.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=5)
    button_1.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
    button_2.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
    button_3.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")
    button_mul.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")
    button_4.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
    button_5.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")
    button_6.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")
    button_add.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")
    button_7.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
    button_8.grid(row=7, column=1, padx=10, pady=10, sticky="nsew")
    button_9.grid(row=7, column=2, padx=10, pady=10, sticky="nsew")
    button_div.grid(row=7, column=3, padx=10, pady=10, sticky="nsew")
    button_clear.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")
    button_0.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")
    button_sub.grid(row=8, column=2, padx=10, pady=10, sticky="nsew")
    button_equal.grid(row=8, column=3, padx=10, pady=10, sticky="nsew")


entering = tk.Button(root, text="> Enter The Dungeon <", command=enter_click)
entering.grid(column=0, row=1, padx=10, pady=10, sticky="nsew", columnspan=2)

text_field = tk.Entry(root)
text_field.config()

def clicking1():
    old_text = text_field.get()
    new_text = old_text + "1"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking2():
    old_text = text_field.get()
    new_text = old_text + "2"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking3():
    old_text = text_field.get()
    new_text = old_text + "3"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking4():
    old_text = text_field.get()
    new_text = old_text + "4"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking5():
    old_text = text_field.get()
    new_text = old_text + "5"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking6():
    old_text = text_field.get()
    new_text = old_text + "6"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking7():
    old_text = text_field.get()
    new_text = old_text + "7"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking8():
    old_text = text_field.get()
    new_text = old_text + "8"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking9():
    old_text = text_field.get()
    new_text = old_text + "9"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking0():
    old_text = text_field.get()
    new_text = old_text + "0"
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking_mul():
    old_text = text_field.get()
    new_text = old_text + " * "
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking_div():
    old_text = text_field.get()
    new_text = old_text + " / "
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking_add():
    old_text = text_field.get()
    new_text = old_text + " + "
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking_clear():
    text_field.delete(0, tk.END)

def clicking_sub():
    old_text = text_field.get()
    new_text = old_text + " - "
    text_field.delete(0, tk.END)
    text_field.insert(0, new_text)

def clicking_equal():
    the_input = text_field.get()
    #seperated = [i for i in the_input.split()]
    ans = eval(the_input)
    output = f"{insult} \n anyways the answer is: {ans}"
    text_field.delete(0, tk.END)
    answer = tk.Label(root, text=output)
    answer.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")
    text_field.destroy()
    button_1.destroy()
    button_2.destroy()
    button_3.destroy()
    button_4.destroy()
    button_5.destroy()
    button_6.destroy()
    button_7.destroy()
    button_8.destroy()
    button_9.destroy()
    button_0.destroy()
    button_add.destroy()
    button_clear.destroy()
    button_sub.destroy()
    button_equal.destroy()
    button_mul.destroy()
    button_div.destroy()

button_1 = tk.Button(root, text=1, command=clicking1)
button_2 = tk.Button(root, text=2, command=clicking2)
button_3 = tk.Button(root, text=3, command=clicking3)
button_mul = tk.Button(root, text="*", command=clicking_mul)
button_4 = tk.Button(root, text=4, command=clicking4)
button_5 = tk.Button(root, text=5, command=clicking5)
button_6 = tk.Button(root, text=6, command=clicking6)
button_div = tk.Button(root, text="/", command=clicking_div)
button_7 = tk.Button(root, text=7, command=clicking7)
button_8 = tk.Button(root, text=8, command=clicking8)
button_9 = tk.Button(root, text=9, command=clicking9)
button_add = tk.Button(root, text="+", command=clicking_add)
button_clear = tk.Button(root, text="AC", command=clicking_clear)
button_0 = tk.Button(root, text=0, command=clicking0)
button_sub = tk.Button(root, text="-", command=clicking_sub)
button_equal = tk.Button(root, text="=", command=clicking_equal)

#keeps tkinter open
root.mainloop()
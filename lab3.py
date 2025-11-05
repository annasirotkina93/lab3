import tkinter as tk
import random
import string


def weight(c): #весовой коэф
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 1
    elif '0' <= c <= '9':
        return ord(c) - ord('0') + 27
    return 0


def generate_ogr(min_sum, max_sum): #работа с блоком XXXX
    block = []
    cur_sum = 0
    while cur_sum < min_sum or cur_sum > max_sum:
        block = random.choices(string.ascii_uppercase + string.digits, k=4)
        cur_sum = sum(weight(c) for c in block)
    return ''.join(block)


def generate_password(min_sum=30, max_sum=35): #работа с блоками XXXX-XXXX-XXXX
    blocks = [generate_ogr(min_sum, max_sum) for _ in range(3)]
    return '-'.join(blocks)


def update_password():
    password = generate_password()
    Text_gen.delete(0, tk.END)
    Text_gen.insert(0, password)


window = tk.Tk()
window.geometry('700x700')
window.resizable(width=False, height=False)


try:
    bg_img = tk.PhotoImage(file='stranger_things.png')
    lbl_bg = tk.Label(window, image=bg_img, width=100, height=50)
    lbl_bg.place(x=0, y=0)
except:
    lbl_bg = tk.Label(window, bg='gray', width=100, height=50)
    lbl_bg.place(x=0, y=0)



frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')


lbl_gen = tk.Label(frame, text='Generation', font=('Arial', 20), fg='black')
lbl_gen.grid(column=0, row=0, padx=10, pady=10)
Text_gen = tk.Entry(frame, width=50)
Text_gen.insert(0, 'XXXX-XXXX-XXXX')
Text_gen.grid(column=0, row=1, padx=10, pady=10)


btn_gen = tk.Button(frame, text='*тык*', command=update_password)
btn_gen.grid(column=0, row=5, padx=10, pady=10)



window.mainloop()

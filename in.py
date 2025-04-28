import tkinter as tk
import random

def play(user_choice):
    options = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        result = "Ты победил!"
    else:
        result = "Ты проиграл!"

    result_label.config(text=f"Компьютер выбрал: {computer_choice}\n{result}")

# Создание окна
root = tk.Tk()
root.title("Камень-Ножницы-Бумага")

# Загрузка изображений
rock_img = tk.PhotoImage(file="rock.png")
scissors_img = tk.PhotoImage(file="scissors.png")
paper_img = tk.PhotoImage(file="paper.png")

# Кнопки с картинками
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play("камень"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play("ножницы"))
scissors_button.grid(row=0, column=1, padx=5, pady=5)

paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play("бумага"))
paper_button.grid(row=0, column=2, padx=5, pady=5)

# Результат
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()

import tkinter as tk
import random

def play(user_choice):
    options = ["камень", "ножницы", "бумага", "шоколад", "лимонад", "отвёртка", "огонь"]
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "камень" and computer_choice == "огонь") or \
         (user_choice == "камень" and computer_choice == "шоколад") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень") or \
         (user_choice == "шоколад" and computer_choice == "бумага") or \
         (user_choice == "ножницы" and computer_choice == "лимонад") or \
         (user_choice == "лимонад" and computer_choice == "отвёртка") or \
         (user_choice == "лимонад" and computer_choice == "камень") or \
         (user_choice == "отвёртка" and computer_choice == "огонь") or \
         (user_choice == "огонь" and computer_choice == "бумага") or \
         (user_choice == "огонь" and computer_choice == "шоколад"):
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
chocolate_img = tk.PhotoImage(file="chocolate.png")
lemonad_img = tk.PhotoImage(file="lemonad.png")
otvertka_img = tk.PhotoImage(file="otvertka.png")
fire_img = tk.PhotoImage(file="fire.png")



# Кнопки с картинками
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play("камень"))
rock_button.grid(row=0, column=0, padx=5, pady=5)

scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play("ножницы"))
scissors_button.grid(row=0, column=1, padx=5, pady=5)

paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play("бумага"))
paper_button.grid(row=0, column=2, padx=5, pady=5)

chocolate_button = tk.Button(button_frame, image=chocolate_img, command=lambda: play("шоколад"))
chocolate_button.grid(row=0, column=3, padx=5, pady=5)

lemonad_button = tk.Button(button_frame, image=lemonad_img, command=lambda: play("лимонад"))
lemonad_button.grid(row=0, column=4, padx=5, pady=5)

otvertka_button = tk.Button(button_frame, image=otvertka_img, command=lambda: play("отвёртка"))
otvertka_button.grid(row=0, column=5, padx=5, pady=5)

fire_button = tk.Button(button_frame, image=fire_img, command=lambda: play("огонь"))
fire_button.grid(row=0, column=6, padx=5, pady=5)

# Результат
result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack(pady=10)

root.mainloop()
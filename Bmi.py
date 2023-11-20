import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

    #yorumlar

    if bmi < 18.5:
        advice_label.config(text="Durum: Zayıf")
    elif 18.5 <= bmi < 24.9:
        advice_label.config(text="Durum: Normal")
    elif 25 <= bmi < 29.9:
        advice_label.config(text="Durum: Fazla Kilolu")
    else:
        advice_label.config(text="Durum: Obez")

# Main

root = tk.Tk()
root.title("BMI Hesaplayıcı")

# Kullanıcı giriş 
weight_label = ttk.Label(root, text="Kilo (kg):")
weight_label.pack(pady=10)
weight_entry = ttk.Entry(root)
weight_entry.pack(pady=10)

height_label = ttk.Label(root, text="Boy (metre):")
height_label.pack(pady=10)
height_entry = ttk.Entry(root)
height_entry.pack(pady=10)

# Hesapla Button
calculate_button = ttk.Button(root, text="BMI Hesapla", command=calculate_bmi)
calculate_button.pack(pady=20)

# Sonuç
result_label = ttk.Label(root, text="BMI:")
result_label.pack()

advice_label = ttk.Label(root, text="Durum:")
advice_label.pack()


root.mainloop()

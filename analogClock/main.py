import tkinter as tk
import math
from datetime import datetime
import pygame
import threading

pygame.mixer.init()

def play_pop():
    try:
        sound = pygame.mixer.Sound("pop.wav")
        sound.play()
    except Exception as e:
        print("Error al reproducir sonido:", e)

roman_numerals = {
    1: "I", 2: "II", 3: "III", 4: "IIII", 5: "V", 6: "VI",
    7: "VII", 8: "VIII", 9: "VIIII", 10: "X", 11: "XI", 12: "XII"
}

root = tk.Tk()
root.title("Relojinn")
root.configure(bg="#1e1e1e")

canvas = tk.Canvas(root, width=400, height=400, bg="#2e2e2e", highlightthickness=0)
canvas.pack(pady=10)

digital_label = tk.Label(root, font=("Orbitron", 24), fg="gold", bg="#1e1e1e")
digital_label.pack(pady=5)
digital_label.pack_forget()  

def toggle_digital():
    if digital_label.winfo_ismapped():
        digital_label.pack_forget()
    else:
        digital_label.pack()

button = tk.Button(root, text="¿No sabes leer un reloj analógico? Click aquí.",
                   command=toggle_digital, font=("Courier", 10, "italic"),
                   fg="white", bg="#444", activebackground="#666", relief="flat")
button.pack(pady=10)

def update_clock():
    canvas.delete("hands")
    
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    center_x = 200
    center_y = 200
    radius = 150
    border_radius = 160 

    canvas.create_oval(center_x - border_radius, center_y - border_radius,
                       center_x + border_radius, center_y + border_radius,
                       outline="#888", width=10, tags="hands")

    for h in range(1, 13):
        angle = math.pi / 6 * (h - 3)
        x = center_x + radius * 0.75 * math.cos(angle)
        y = center_y + radius * 0.75 * math.sin(angle)
        canvas.create_text(x, y, text=roman_numerals[h],
                           fill="gold", font=("Times New Roman", 18, "bold"))

    second_angle = math.pi / 30 * second - math.pi / 2
    minute_angle = math.pi / 30 * minute - math.pi / 2
    hour_angle = math.pi / 6 * hour + math.pi / 360 * minute - math.pi / 2

    second_x = center_x + radius * 0.9 * math.cos(second_angle)
    second_y = center_y + radius * 0.9 * math.sin(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=1, tags="hands")

    minute_x = center_x + radius * 0.75 * math.cos(minute_angle)
    minute_y = center_y + radius * 0.75 * math.sin(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, fill="white", width=3, tags="hands")

    hour_x = center_x + radius * 0.5 * math.cos(hour_angle)
    hour_y = center_y + radius * 0.5 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill="white", width=5, tags="hands")

    canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5,
                       fill="gold", outline="", tags="hands")

    digital_label.config(text=now.strftime("%H:%M:%S"))

    threading.Thread(target=play_pop, daemon=True).start()

    root.after(1000, update_clock)

update_clock()
root.mainloop()

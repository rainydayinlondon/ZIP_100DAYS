import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class HabitTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Habit Tracker")

        self.habits = []
        self.num_habits = 1

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Lütfen alışkanlıklarınızı girin:")
        self.label.pack()

        for i in range(self.num_habits):
            habit_label = tk.Label(self.master, text=f"{i+1}. alışkanlık:")
            habit_label.pack()
            habit_entry = tk.Entry(self.master)
            habit_entry.pack()
            self.habits.append(habit_entry)

        self.record_button = tk.Button(self.master, text="Kaydet", command=self.record_progress)
        self.record_button.pack()

        self.quit_button = tk.Button(self.master, text="Çıkış", command=self.master.quit)
        self.quit_button.pack()

    def record_progress(self):
        date_today = datetime.now().strftime("%Y-%m-%d")
        for habit_entry in self.habits:
            habit = habit_entry.get()
            if habit:
                self.write_to_file(date_today, habit)
                self.reset_entry(habit_entry)

    def write_to_file(self, date, habit):
        file_name = "habit_tracker.txt"
        with open(file_name, "a") as file:
            file.write(f"{date},{habit}\n")
        messagebox.showinfo("Bilgi", f"{date} tarihinde '{habit}' alışkanlığı kaydedildi.")

    def reset_entry(self, entry):
        entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

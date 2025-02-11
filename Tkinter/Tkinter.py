import tkinter as tk
from tkinter import Listbox, Entry, Button

class FilterableListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Szűrhető Lista (Tkinter)")
        self.root.geometry("300x400")

        # Alap listaelemek
        self.items = ["Számla 001", "Számla 002", "Számla 003", "Számla 004", 
                      "Vásárló 1", "Vásárló 2", "Termék A", "Termék B"]

        # Szűrő mező
        self.filter_entry = Entry(root, width=30)
        self.filter_entry.pack(pady=10)

        # Szűrés gomb
        self.filter_button = Button(root, text="Szűrés", command=self.filter_list)
        self.filter_button.pack(pady=5)

        # Lista widget
        self.listbox = Listbox(root, width=40, height=15)
        self.listbox.pack(pady=10)

        # Lista feltöltése
        self.update_list(self.items)

    def update_list(self, items):
        """Frissíti a listát a megadott elemekkel."""
        self.listbox.delete(0, tk.END)  # Töröljük a jelenlegi elemeket
        for item in items:
            self.listbox.insert(tk.END, item)  # Új elemek hozzáadása

    def filter_list(self):
        """Szűrési logika a beírt szöveg alapján."""
        filter_text = self.filter_entry.get().lower()
        filtered_items = [item for item in self.items if filter_text in item.lower()]
        self.update_list(filtered_items)

if __name__ == "__main__":
    root = tk.Tk()
    app = FilterableListApp(root)
    root.mainloop()

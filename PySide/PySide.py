from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class FilterableList(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Szűrhető Lista (PySide6)")
        self.setGeometry(100, 100, 300, 400)

        # Alap listaelemek
        self.items = ["Számla 001", "Számla 002", "Számla 003", "Számla 004", "Vásárló 1", "Vásárló 2", "Termék A", "Termék B"]

        # Fő elrendezés
        layout = QVBoxLayout()

        # Szűrő mező
        self.filter_input = QLineEdit(self)
        self.filter_input.setPlaceholderText("Írd be a keresett kifejezést...")
        layout.addWidget(self.filter_input)

        # Szűrés gomb
        self.filter_button = QPushButton("Szűrés", self)
        self.filter_button.clicked.connect(self.filter_list)
        layout.addWidget(self.filter_button)

        # Lista widget
        self.list_widget = QListWidget(self)
        self.list_widget.addItems(self.items)
        layout.addWidget(self.list_widget)

        # Beállítjuk az elrendezést
        self.setLayout(layout)

    def filter_list(self):
        """Szűrési logika a megadott szöveg alapján"""
        filter_text = self.filter_input.text().lower()
        self.list_widget.clear()

        # Csak azokat az elemeket adjuk hozzá, amelyek tartalmazzák a keresett kifejezést
        filtered_items = [item for item in self.items if filter_text in item.lower()]
        self.list_widget.addItems(filtered_items)

if __name__ == "__main__":
    app = QApplication([])
    window = FilterableList()
    window.show()
    app.exec()


import customtkinter
from ui.main_window import MainWindow


if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")  # Modes: System (default), Light, Dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = MainWindow()
    app.mainloop()

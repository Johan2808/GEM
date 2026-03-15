import customtkinter as ctk
from tkinter import filedialog
import os
import platform
import subprocess


class PDFViewer(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.current_file = None

        self.label = ctk.CTkLabel(self, text="PDF Viewer", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)

        self.open_btn = ctk.CTkButton(self, text="Choisir un PDF", command=self.open_pdf)
        self.open_btn.pack(pady=8)

        self.open_ext_btn = ctk.CTkButton(self, text="Ouvrir dans l'application par défaut", command=self.open_in_default, state="disabled")
        self.open_ext_btn.pack(pady=8)

        self.file_label = ctk.CTkLabel(self, text="Aucun fichier sélectionné.")
        self.file_label.pack(pady=10)

    def open_pdf(self):
        """Sélectionne un fichier PDF et prépare l’ouverture dans l’application par défaut."""
        path = filedialog.askopenfilename(title="Sélectionner un fichier PDF", filetypes=[("Fichiers PDF", "*.pdf")])
        if path:
            self.current_file = path
            self.file_label.configure(text=f"Fichier sélectionné : {path}")
            self.open_ext_btn.configure(state="normal")
        else:
            self.current_file = None
            self.file_label.configure(text="Aucun fichier sélectionné.")
            self.open_ext_btn.configure(state="disabled")

    def open_in_default(self):
        """Ouvre le PDF sélectionné dans l’application système par défaut."""
        if not self.current_file:
            return

        if platform.system() == "Windows":
            os.startfile(self.current_file)
        elif platform.system() == "Darwin":
            subprocess.call(["open", self.current_file])
        else:
            subprocess.call(["xdg-open", self.current_file])


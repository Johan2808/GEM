import customtkinter as ctk
from tkinter import filedialog
import vlc


class MP4Player(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.player = None
        self.current_file = None

        self.label = ctk.CTkLabel(self, text="MP4 Player", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)

        self.open_btn = ctk.CTkButton(self, text="Ouvrir un MP4", command=self.open_mp4)
        self.open_btn.pack(pady=8)

        self.status_label = ctk.CTkLabel(self, text="Aucun fichier sélectionné.")
        self.status_label.pack(pady=8)

        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(pady=8)

        self.play_btn = ctk.CTkButton(self.control_frame, text="Play", command=self.play)
        self.play_btn.grid(row=0, column=0, padx=6)

        self.pause_btn = ctk.CTkButton(self.control_frame, text="Pause", command=self.pause)
        self.pause_btn.grid(row=0, column=1, padx=6)

        self.stop_btn = ctk.CTkButton(self.control_frame, text="Stop", command=self.stop)
        self.stop_btn.grid(row=0, column=2, padx=6)

    def _create_player(self):
        """Crée l’instance de player VLC si nécessaire."""
        if self.player is None:
            self.player = vlc.MediaPlayer()

    def open_mp4(self):
        """Ouvre un fichier MP4 et prépare la lecture."""
        path = filedialog.askopenfilename(title="Sélectionner un fichier MP4", filetypes=[("Fichiers MP4", "*.mp4")])
        if path:
            self.current_file = path
            self.status_label.configure(text=f"Fichier sélectionné : {path}")
            self._create_player()
            media = vlc.Media(self.current_file)
            self.player.set_media(media)
        else:
            self.status_label.configure(text="Aucun fichier sélectionné.")
            self.current_file = None

    def play(self):
        """Démarre ou reprend la lecture du MP4 sélectionné."""
        if self.current_file:
            self._create_player()
            if self.player.get_media() is None:
                media = vlc.Media(self.current_file)
                self.player.set_media(media)
            self.player.play()
            self.status_label.configure(text=f"Lecture : {self.current_file}")
        else:
            self.status_label.configure(text="Pas de fichier à lire.")

    def pause(self):
        """Met la lecture en pause."""
        if self.player:
            self.player.pause()
            self.status_label.configure(text="Lecture en pause")

    def stop(self):
        """Arrête la lecture et remet à zéro."""
        if self.player:
            self.player.stop()
            self.status_label.configure(text="Lecture arrêtée")

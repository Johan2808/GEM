from gestures.swipe import SwipeGesture
from config.settings import SWIPE_THRESHOLD

class SwipeLeftGesture(SwipeGesture):
    
    def __init__(self):
        self.start_x = None      # position X au début du mouvement
   # timestamp du début du mouvement

    @property
    def name(self):
        return "SWIPE_LEFT"

    def detect(self, hand_landmarks):
        """Détecte un swipe vers la gauche :
        main en position swipe + déplacement rapide vers la gauche
        """
        
        # Vérifie d'abord la position swipe (hérité de SwipeGesture)
        if not self.is_swipe_position(hand_landmarks):
            # Reset si main plus en position swipe
            self.start_x = None
            return None

        # Position X actuelle du poignet (landmark 0)
        current_x = hand_landmarks[0].x

        # Initialise le point de départ
        if self.start_x is None:
            self.start_x = current_x
            return None

        # Calcule le déplacement et le temps écoulé
        delta_x = self.start_x - current_x  # positif = mouvement gauche
 

        # Swipe gauche validé si déplacement suffisant dans le temps imparti
        if delta_x > SWIPE_THRESHOLD:
            self.start_x = current_x
            return "SWIPE_LEFT"

        return None
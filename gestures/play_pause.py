from config.settings import FINGER_TIP_IDS
from gestures.base_gesture import BaseGesture


class PlayPauseGesture(BaseGesture):
    
    def __init__(self):
        self.prev_state = None  # mémorise l'état précédent pour éviter les signaux répétés

    @property
    def name(self):
        return "PLAY_PAUSE"
    
    def detect(self, hand_landmarks):
        """Retourne 'PAUSE', 'PLAY' ou None selon changement d'état"""
        
        # Vérifie si les doigts sont repliés
        fingers_folded = 0
        for i in range(1, 5):  # Index à auriculaire (pouce exclu)
            tip = hand_landmarks[FINGER_TIP_IDS[i]]       # bout du doigt
            pip = hand_landmarks[FINGER_TIP_IDS[i] - 2]  # articulation milieu
            if tip.y > pip.y:  # bout plus bas = doigt replié
                fingers_folded += 1
        
        # Détermine l'état actuel
        is_fist = fingers_folded >= 4
        current = "PAUSE" if is_fist else "PLAY"

        # N'envoie le signal qu'au changement d'état
        if current != self.prev_state:
            self.prev_state = current
            return current

        return None  # aucun changement, pas de signal
from config.settings import FINGER_TIP_IDS
from gestures.base_gesture import BaseGesture


class PlayPauseGesture(BaseGesture):
    
    def __init__(self):
        self.prev_state = None

    @property
    def name(self):
        return "PLAY_PAUSE"
    
    def detect(self, hand_landmarks):
        """Retourne 'PAUSE', 'PLAY' ou None selon changement d'état"""
        
        # Vérifie si les doigts sont repliés
        fingers_folded = 0
        for i in range(1, 5):
            tip = hand_landmarks[FINGER_TIP_IDS[i]]
            pip = hand_landmarks[FINGER_TIP_IDS[i] - 2]
            if tip.y > pip.y:
                fingers_folded += 1

        # Vérifie si les doigts sont levés
        fingers_up = 0
        for i in range(1, 5):
            tip = hand_landmarks[FINGER_TIP_IDS[i]]
            pip = hand_landmarks[FINGER_TIP_IDS[i] - 2]
            if tip.y < pip.y:
                fingers_up += 1

        # Poing strict = 4 doigts repliés
        is_fist = fingers_folded >= 4

        # Main ouverte stricte = 4 doigts levés
        is_open = fingers_up >= 4

        if is_fist:
            current = "PAUSE"
        elif is_open:
            current = "PLAY"
        else:
            return None  # geste ambigu, on ignore

        if current != self.prev_state:
            self.prev_state = current
            return current

        return None
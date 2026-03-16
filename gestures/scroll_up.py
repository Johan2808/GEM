from gestures.scroll import ScrollGesture
from config.settings import SCROLL_THRESHOLD

class ScrollUpGesture(ScrollGesture):

    def __init__(self):
        self.prev_y = None  # position Y précédente de l'index

    @property
    def name(self):
        return "SCROLL_UP"

    def detect(self, hand_landmarks):
        """Index seul levé + mouvement vers le haut → SCROLL_UP"""

        # Vérifie position index seul strict
        if not self.is_index_pointer(hand_landmarks):
            self.prev_y = None
            return None

        current_y = hand_landmarks[8].y  # bout de l'index

        if self.prev_y is None:
            self.prev_y = current_y
            return None

        # Mouvement vers haut = Y diminue
        if self.prev_y - current_y > SCROLL_THRESHOLD:
            self.prev_y = current_y
            return "SCROLL_UP"

        self.prev_y = current_y
        return None
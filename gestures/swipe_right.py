from gestures.swipe import SwipeGesture
from config.settings import SWIPE_SPEED

class SwipeRightGesture(SwipeGesture):
    
    def __init__(self):
        super().__init__()
        self.prev_x = None

    @property
    def name(self):
        return "SWIPE_RIGHT"

    def detect(self, hand_landmarks):
        if not self.is_swipe_position(hand_landmarks):
            self.prev_x = None
            return None

        current_x = hand_landmarks[0].x

        if self.prev_x is None:
            self.prev_x = current_x
            return None

        delta = current_x - self.prev_x  # positif = mouvement droite
        self.prev_x = current_x

        if delta > SWIPE_SPEED:
            return "SWIPE_RIGHT"

        return None
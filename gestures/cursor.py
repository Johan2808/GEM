from config.settings import PINCH_THRESHOLD, FINGER_TIP_IDS
from gestures.base_gesture import BaseGesture
from gestures.mouse_move import MouseMove
import math

class CursorGesture(BaseGesture):
    def __init__(self):
        self.mover = MouseMove()

    @property
    def name(self):
        return "CURSOR"

    def detect(self, raw_landmarks, pixel_landmarks):
        # Coordonnées pouce et index
        thumb = raw_landmarks[4]
        index = raw_landmarks[12]

        # Distance euclidienne normalisée
        dist = math.sqrt((thumb.x - index.x)**2 + (thumb.y - index.y)**2) * 1000

        #Main ouverte → déplace la souris
        if dist >= PINCH_THRESHOLD:
            _, cx, cy = pixel_landmarks[12]
            self.mover.move(cx, cy)
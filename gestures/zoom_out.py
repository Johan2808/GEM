from gestures.base_gesture import BaseGesture
from config.settings import ZOOM_THRESHOLD
import math

class ZoomOutGesture(BaseGesture):

    def __init__(self):
        self.prev_dist = None  # distance précédente entre pouce et index

    @property
    def name(self):
        return "ZOOM_OUT"

    def _all_fingers(self, hand_landmarks):
        """Vérifie que tous les doigts sont levés"""
        index_up = hand_landmarks[8].y < hand_landmarks[6].y
        middle_up = hand_landmarks[12].y < hand_landmarks[10].y
        ring_up = hand_landmarks[16].y < hand_landmarks[14].y
        pinky_up = hand_landmarks[20].y < hand_landmarks[18].y
        return index_up and middle_up and ring_up and pinky_up

    def detect(self, hand_landmarks):
        """Détecte un rapprochement pouce-index avec tous les doigts levés → ZOOM_OUT"""

        # Vérifie la position zoom out
        if not self._all_fingers(hand_landmarks):
            self.prev_dist = None
            return None

        # Calcule distance euclidienne entre pouce (4) et index (8)
        thumb = hand_landmarks[4]
        index = hand_landmarks[8]
        dist = math.sqrt((thumb.x - index.x)**2 + (thumb.y - index.y)**2)

        # Initialise la distance de référence
        if self.prev_dist is None:
            self.prev_dist = dist
            return None

        # Si distance diminue au delà du seuil → zoom out
        if self.prev_dist - dist > ZOOM_THRESHOLD:
            self.prev_dist = dist
            return "ZOOM_OUT"

        self.prev_dist = dist
        return None
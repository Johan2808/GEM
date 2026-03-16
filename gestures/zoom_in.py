from gestures.base_gesture import BaseGesture
from config.settings import ZOOM_THRESHOLD

import math

class ZoomInGesture(BaseGesture):

    def __init__(self):
        self.prev_dist = None  # distance précédente entre pouce et index

    @property
    def name(self):
        return "ZOOM_IN"

    def _two_fingers_only(self, hand_landmarks):
        """Vérifie que seuls pouce et index sont levés, autres repliés"""
        
        # Index levé : bout (8) plus haut que articulation (6)
        index_up = hand_landmarks[8].y < hand_landmarks[6].y
        
        # Majeur replié : bout (12) plus bas que articulation (10)
        middle_down = hand_landmarks[12].y > hand_landmarks[10].y
        
        # Annulaire replié : bout (16) plus bas que articulation (14)
        ring_down = hand_landmarks[16].y > hand_landmarks[14].y
        
        # Auriculaire replié : bout (20) plus bas que articulation (18)
        pinky_down = hand_landmarks[20].y > hand_landmarks[18].y

        # Pouce levé : bout (4) éloigné du poignet (0) horizontalement
        thumb_up = hand_landmarks[4].x < hand_landmarks[3].x

        return index_up and middle_down and ring_down and pinky_down and thumb_up

    def detect(self, hand_landmarks):
        """Détecte un écartement pouce-index avec autres doigts repliés → ZOOM_IN"""

        # Vérifie la position zoom in
        if not self._two_fingers_only(hand_landmarks):
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

        # Si distance augmente au delà du seuil → zoom in
        if dist - self.prev_dist > ZOOM_THRESHOLD:
            self.prev_dist = dist
            return "ZOOM_IN"

        self.prev_dist = dist
        return None
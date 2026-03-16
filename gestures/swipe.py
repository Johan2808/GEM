from gestures.base_gesture import BaseGesture

class SwipeGesture(BaseGesture):
    
    def __init__(self):
        self.stable_count = 0
        self.STABLE_FRAMES = 3  # frames consécutives requises pour valider la position

    @property
    def name(self):
        return "SWIPE"

    def is_swipe_position(self, hand_landmarks):
        """Vérifie si la main est en position swipe :
        index (8) et majeur (12) levés, autres doigts repliés.
        """
        
        # Index levé : bout (8) plus haut que articulation (6)
        index_up = hand_landmarks[8].y < hand_landmarks[6].y
        
        # Majeur levé : bout (12) plus haut que articulation (10)
        middle_up = hand_landmarks[12].y < hand_landmarks[10].y
        
        # Annulaire replié : bout (16) plus bas que articulation (14)
        ring_down = hand_landmarks[16].y > hand_landmarks[14].y
        
        # Auriculaire replié : bout (20) plus bas que articulation (18)
        pinky_down = hand_landmarks[20].y > hand_landmarks[18].y
        
        # Pouce replié horizontalement
        thumb_down = hand_landmarks[4].x > hand_landmarks[3].x

        result = index_up and middle_up and ring_down and pinky_down and thumb_down

        # Stabilisation : exige plusieurs frames consécutives
        if result:
            self.stable_count += 1
        else:
            self.stable_count = 0

        return self.stable_count >= self.STABLE_FRAMES

    def detect(self, hand_landmarks):
        """Retourne True si la main est en position swipe stable"""
        return self.is_swipe_position(hand_landmarks)
from gestures.base_gesture import BaseGesture

class VolumeGesture(BaseGesture):

    @property
    def name(self):
        return "VOLUME"

    def is_thumb_only(self, hand_landmarks):
        """Vérifie que seul le pouce est levé, tous les autres repliés"""

        # Index replié : bout (8) plus bas que articulation (6)
        index_down = hand_landmarks[8].y > hand_landmarks[6].y

        # Majeur replié : bout (12) plus bas que articulation (10)
        middle_down = hand_landmarks[12].y > hand_landmarks[10].y

        # Annulaire replié : bout (16) plus bas que articulation (14)
        ring_down = hand_landmarks[16].y > hand_landmarks[14].y

        # Auriculaire replié : bout (20) plus bas que articulation (18)
        pinky_down = hand_landmarks[20].y > hand_landmarks[18].y

        # Pouce écarté : bout (4) loin du bout index (8) horizontalement
        thumb_spread = abs(hand_landmarks[4].x - hand_landmarks[8].x) > 0.1

        return index_down and middle_down and ring_down and pinky_down and thumb_spread

    def detect(self, hand_landmarks):
        return self.is_thumb_only(hand_landmarks)
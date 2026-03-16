from gestures.base_gesture import BaseGesture

class ScrollGesture(BaseGesture):

    @property
    def name(self):
        return "SCROLL"

    def is_index_pointer(self, hand_landmarks):
        """Vérifie que seul l'index est levé strictement :
        index levé, majeur/annulaire/auriculaire repliés, pouce replié
        """

        # Index levé : bout (8) plus haut que articulation (6)
        index_up = hand_landmarks[8].y < hand_landmarks[6].y

        # Majeur replié strict
        middle_down = hand_landmarks[12].y > hand_landmarks[10].y

        # Annulaire replié strict
        ring_down = hand_landmarks[16].y > hand_landmarks[14].y

        # Auriculaire replié strict
        pinky_down = hand_landmarks[20].y > hand_landmarks[18].y

        return index_up and middle_down and ring_down and pinky_down

    def detect(self, hand_landmarks):
        return self.is_index_pointer(hand_landmarks)
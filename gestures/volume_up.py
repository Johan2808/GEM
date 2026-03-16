from gestures.volume import VolumeGesture

class VolumeUpGesture(VolumeGesture):

    @property
    def name(self):
        return "VOLUME_UP"

    def detect(self, hand_landmarks):
        """Pouce levé vers haut + autres repliés → VOLUME_UP"""

        if not self.is_thumb_only(hand_landmarks):
            return None

        # Pouce vers haut : bout (4) plus haut que articulation (3)
        if hand_landmarks[4].y < hand_landmarks[3].y:
            return "VOLUME_UP"

        return None
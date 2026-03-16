from gestures.volume import VolumeGesture

class VolumeDownGesture(VolumeGesture):

    @property
    def name(self):
        return "VOLUME_DOWN"

    def detect(self, hand_landmarks):
        """Pouce vers bas + autres repliés → VOLUME_DOWN"""

        if not self.is_thumb_only(hand_landmarks):
            return None

        # Pouce vers bas : bout (4) plus bas que articulation (3)
        if hand_landmarks[4].y > hand_landmarks[3].y:
            return "VOLUME_DOWN"

        return None
from config.settings import FINGER_TIP_IDS
from gestures.base_gesture import BaseGesture

#renomage class firstgesture -> freezeGesture
class FreezeGesture(BaseGesture):
    @property
    def name(self):
        return "FREEZE" #renomage return POING -> FREEZE
    
    def detect(self, hand_landmarks):
        """Détecte si la main est fermée (poing)"""
        # Récupère les bouts des doigts
        tips = []
        for tip_id in FINGER_TIP_IDS:
            tip = hand_landmarks[tip_id]
            tips.append(tip)
        
        # Vérifie si les doigts sont repliés
        # (les bouts sont plus bas que les articulations)
        fingers_folded = 0
        for i in range(1, 5):  # Index à auriculaire
            tip = hand_landmarks[FINGER_TIP_IDS[i]]
            pip = hand_landmarks[FINGER_TIP_IDS[i] - 2]  # Articulation
            if tip.y > pip.y:  # Le bout est plus bas que l'articulation
                fingers_folded += 1
        
        # C'est un poing si au moins 4 doigts sont repliés
        return fingers_folded >= 4
    
# DIKANLE FREEZE : geler curseur + quit
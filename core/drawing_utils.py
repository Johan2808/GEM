import cv2
from config.settings import COLORS

class DrawingUtils:
    
    # Connexions entre les landmarks (selon topologie MediaPipe 21 points)
    HAND_CONNECTIONS = [
        (0,1),(1,2),(2,3),(3,4),         # pouce
        (0,5),(5,6),(6,7),(7,8),         # index
        (0,9),(9,10),(10,11),(11,12),    # majeur
        (0,13),(13,14),(14,15),(15,16), # annulaire
        (0,17),(17,18),(18,19),(19,20), # auriculaire
        (5,9),(9,13),(13,17)             # paume
    ]

    def draw(self, img, raw_landmarks):
        """Dessine les landmarks et connexions sur le frame OpenCV"""
        
        if not raw_landmarks:
            return img
        
        h, w, _ = img.shape

        # Dessine les connexions (lignes)
        for start, end in self.HAND_CONNECTIONS:
            x1 = int(raw_landmarks[start].x * w)
            y1 = int(raw_landmarks[start].y * h)
            x2 = int(raw_landmarks[end].x * w)
            y2 = int(raw_landmarks[end].y * h)
            cv2.line(img, (x1, y1), (x2, y2), COLORS['HAND_CONNECTIONS'], 2)

        # Dessine les points landmarks (cercles)
        for lm in raw_landmarks:
            cx = int(lm.x * w)
            cy = int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, COLORS['HAND_LANDMARKS'], -1)

        return img
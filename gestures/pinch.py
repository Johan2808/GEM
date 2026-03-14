from config.settings import PINCH_THRESHOLD
from gestures.base_gesture import BaseGesture
import pyautogui
import math
import time

class PinchGesture(BaseGesture):
    def __init__(self):
        self.last_pinch_time = 0      # timestamp du dernier pincement
        self.pinching = False          # état actuel : est-ce qu'on pince ?
        self.DOUBLE_CLICK_DELAY = 0.4  # délai max entre 2 pincements pour double clic

    @property
    def name(self):
        return "PINCH"

    def detect(self, raw_landmarks):
        thumb = raw_landmarks[4]   # landmark pouce
        index = raw_landmarks[8]   # landmark bout index

        # Distance euclidienne normalisée entre pouce et index (×1000 pour lisibilité)
        dist = math.sqrt((thumb.x - index.x)**2 + (thumb.y - index.y)**2) * 1000

        if dist < PINCH_THRESHOLD:  # pincement détecté
            if not self.pinching:   # évite les clics répétés si on maintient le pincement
                self.pinching = True
                now = time.time()
                if now - self.last_pinch_time < self.DOUBLE_CLICK_DELAY:
                    # 2ème pincement rapide → double clic
                    pyautogui.doubleClick()
                else:
                    # 1er pincement ou trop lent → clic simple
                    pyautogui.click()
                self.last_pinch_time = now  # mémorise le moment du clic
        else:
            self.pinching = False  # main ouverte, réinitialise l'état

        return dist < PINCH_THRESHOLD  # True si pincement actif
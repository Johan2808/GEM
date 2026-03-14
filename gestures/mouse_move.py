from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, CAMERA_WIDTH, CAMERA_HEIGHT, CAM_MARGIN, SMOOTHING_FACTOR , SENSITIVITY
import pyautogui
import numpy as np

pyautogui.PAUSE = 0 # gain de temps par rapport au lag webcam
pyautogui.FAILSAFE = False #desactive le crash si le souris est au coin de l'ecran 

class MouseMove:
    def __init__(self):
        self.prev_x, self.prev_y = 0, 0

    def move(self, cx , cy):
        # Mapping caméra → écran
        x = np.interp(cx, [CAM_MARGIN, CAMERA_WIDTH - CAM_MARGIN], [0, SCREEN_WIDTH])
        y = np.interp(cy, [CAM_MARGIN, CAMERA_HEIGHT - CAM_MARGIN], [0, SCREEN_HEIGHT])

        #sensibilité de la souris 
        x = SCREEN_WIDTH/2 + (x - SCREEN_WIDTH/2) * SENSITIVITY
        y = SCREEN_HEIGHT/2 + (y - SCREEN_HEIGHT/2) * SENSITIVITY

        # Lissage / smooth / fluidité
        x = self.prev_x + (x - self.prev_x) / SMOOTHING_FACTOR
        y = self.prev_y + (y - self.prev_y) / SMOOTHING_FACTOR

        pyautogui.moveTo(int(x), int(y))
        self.prev_x, self.prev_y = x, y
import cv2
from core.hand_detector import HandDetector
from gestures.freeze import FreezeGesture
from gestures.cursor import CursorGesture
from gestures.pinch import PinchGesture

cap = cv2.VideoCapture(0)
detector = HandDetector() 
freeze = FreezeGesture()#variable freeze
cursor = CursorGesture()#variable cursor ---- curseur souris 
pinch = PinchGesture()#variable pinch ----- pincement


try:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        img = detector.find_hands(img)
        landmarks = detector.find_position(img)

        #si poing fermé -> affiche FREEZE dans le fenetre puis quitte le programme  
        raw = detector.get_raw_landmarks()
        if raw and freeze.detect(raw):
            import time
            end = time.time() + 0.5
            while time.time() < end:
                success, img = cap.read()
                img = cv2.flip(img, 1)
                cv2.putText(img, "FREEZE", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                cv2.imshow("Hand Detection", img)
                cv2.waitKey(1)
            break
        
        #si main ouverte on deplace la souris + pincement
        if raw:
            cursor.detect(raw, landmarks)#pour le curseur souris 
            pinch.detect(raw)#pour le pincement

        if landmarks:
            print(landmarks[8])  # position du bout de l'index
        
        cv2.imshow("Hand Detection", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
except KeyboardInterrupt:
    pass

finally : 
    cap.release()
    cv2.destroyAllWindows()

#try/exept dans le code pour plus de securité en keyboard interupt
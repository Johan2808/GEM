import cv2
from core.hand_detector import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector() 

try:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.find_hands(img)
        landmarks = detector.find_position(img)

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
import cv2
from core.hand_detector import HandDetector
from gestures.swipe_left import SwipeLeftGesture
from gestures.swipe_right import SwipeRightGesture
from gestures.play_pause import PlayPauseGesture

cap = cv2.VideoCapture(0)
detector = HandDetector() 
swipe_left = SwipeLeftGesture()
swipe_right = SwipeRightGesture()
play_pause = PlayPauseGesture()

gesture_text = ""

try:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.find_hands(img)
        landmarks = detector.find_position(img)
        raw = detector.get_raw_landmarks()

        if raw:
            #logique swipe
            result = swipe_left.detect(raw)
            if not result:
                result = swipe_right.detect(raw)
    
            if result:
                gesture_text = result
            
            #logique play pause
            pp_result = play_pause.detect(raw)
            if pp_result:
                gesture_text = pp_result

        if landmarks:
            print(landmarks[8])  # position du bout de l'index
        
        cv2.putText(img, gesture_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
        cv2.imshow("Hand Detection", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    pass

finally : 
    cap.release()
    cv2.destroyAllWindows()

#try/exept dans le code pour plus de securité en keyboard interupt
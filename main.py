import cv2
from core.hand_detector import HandDetector
from gestures.swipe_left import SwipeLeftGesture
from gestures.swipe_right import SwipeRightGesture
from gestures.play_pause import PlayPauseGesture
from gestures.zoom_in import ZoomInGesture
from gestures.zoom_out import ZoomOutGesture
from gestures.volume_up import VolumeUpGesture
from gestures.volume_down import VolumeDownGesture
from gestures.scroll_up import ScrollUpGesture
from gestures.scroll_down import ScrollDownGesture

cap = cv2.VideoCapture(0)
detector = HandDetector() 
swipe_left = SwipeLeftGesture()
swipe_right = SwipeRightGesture()
play_pause = PlayPauseGesture()
zoom_in = ZoomInGesture()
zoom_out = ZoomOutGesture()
volume_up = VolumeUpGesture()
volume_down = VolumeDownGesture()
scroll_up = ScrollUpGesture()
scroll_down = ScrollDownGesture()

gesture_text = ""

try:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.find_hands(img)
        landmarks = detector.find_position(img)
        raw = detector.get_raw_landmarks()

        if raw:
            # #logique swipe
            # result = swipe_left.detect(raw)
            # if not result:
            #     result = swipe_right.detect(raw)
            # if result:
            #     gesture_text = result
            # print("swipe_pos:", swipe_left.is_swipe_position(raw), "prev_x:", swipe_left.prev_x, "current_x:", raw[0].x)
            
            # #logique play pause
            # pp_result = play_pause.detect(raw)
            # if pp_result:
            #     gesture_text = pp_result

            # logique zoom in zoom out
            zoom_result = zoom_in.detect(raw)
            if not zoom_result:
                zoom_result = zoom_out.detect(raw)
            if zoom_result:
                gesture_text = zoom_result

            # #logique volume 
            # vol_result = volume_up.detect(raw)
            # if not vol_result:
            #     vol_result = volume_down.detect(raw)
            # if vol_result:
            #     gesture_text = vol_result


            # #logique scroll
            # scroll_result = scroll_up.detect(raw)
            # if not scroll_result:
            #     scroll_result = scroll_down.detect(raw)
            # if scroll_result:
            #     gesture_text = scroll_result

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
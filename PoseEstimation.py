import cv2
import time
from mediapipe.python.solutions.pose import Pose, POSE_CONNECTIONS
from mediapipe.python.solutions.drawing_utils import draw_landmarks


mypose = Pose(static_image_mode=False,
              model_complexity=1,
              smooth_landmarks=True,
              min_detection_confidence=0.5,
              min_tracking_confidence=0.5)
cap = cv2.VideoCapture('videos/4.mp4')
pTime = time.time()
scale = 0.6
while True:
    success, img = cap.read()
    if not success:
        break
    new_h, new_w = int(img.shape[0]*scale), int(img.shape[1]*scale)
    img = cv2.resize(img, (new_w, new_h))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = mypose.process(imgRGB).pose_landmarks
    if results:
        draw_landmarks(img, results, POSE_CONNECTIONS)
        for Id, lm in enumerate(results.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            # print(Id, lm.x, lm.y)
            cv2.circle(img, (cx, cy), 5,
                       (255, 0, 255), cv2.FILLED)

    # get frame rate :
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # show the frame rate
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    # show the image
    cv2.imshow("Image", img)
    cv2.waitKey(1)

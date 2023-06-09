from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2
from SOS import play_notification_sound

prototxt_path = r"C:\Users\marin\PycharmProjects\Final_qualifying_work\MobileNetSSD_deploy.prototxt.txt"
model_path = r"C:\Users\marin\PycharmProjects\Final_qualifying_work\MobileNetSSD_deploy.caffemodel"

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

loitering_time = {}
loitering_threshold = 70


print("[INFO] starting video stream...")

#video_source = 0
video_source = r"1_loitering.avi"

vs = cv2.VideoCapture(video_source)
time.sleep(2.0)
fps = FPS().start()


while True:
    ret, frame = vs.read()

    frame = imutils.resize(frame, width=400)

    (h, w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for person_id in list(loitering_time.keys()):
        if person_id not in person_ids:
            del loitering_time[person_id]

    person_ids = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            if CLASSES[class_id] == "person":
                person_id = int(detections[0, 0, i, 3])
                person_ids.append(person_id)

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[class_id], 2)
                label = f"Person {person_id}"
                cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[class_id], 2)

                if person_id in loitering_time:
                    loitering_time[person_id] += 1
                    if loitering_time[person_id] > loitering_threshold:
                        cv2.putText(frame, "Loitering!", (startX, startY - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        play_notification_sound()
                else:
                    loitering_time[person_id] = 1

    cv2.imshow("Loitering Detection", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    fps.update()

fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.release()

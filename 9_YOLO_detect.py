from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  9_YOLO_detect.py
from pprint import pprint

model = YOLO('best.pt')
cap = cv2.VideoCapture('1.mp4')
pprint(model.names)

while True:
    _, img = cap.read()


    results = model.predict(img)

    for r in results:

        annotator = Annotator(img)

        boxes = r.boxes
        for box in boxes:
            b = box.xyxy[0]
            c = box.cls

            annotator.box_label(b, model.names[int(c)])
            top, left, bottom, right = b.numpy().astype(int)
            # print(top, left, bottom, right)
            img[left:right, top:bottom, 0] = 255

    img = annotator.result()
    cv2.imshow('YOLO V8 Detection', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
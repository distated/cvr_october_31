from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='config.yaml', epochs=20, batch=16, imgsz=640)
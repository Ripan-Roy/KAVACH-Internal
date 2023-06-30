from ultralytics import YOLO
model = YOLO('yolo_custom.pt')

model.predict(source=0, show=True, conf=0.5)


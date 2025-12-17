from ultralytics import YOLO

model = YOLO("yolo11n.pt")  # pretrained

results = model(["../dataset/images/sample1.jpg"])

for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    obb = result.obb

    result.show()

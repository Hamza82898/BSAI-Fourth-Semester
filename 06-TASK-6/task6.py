from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
animal_Id = [15, 16, 17, 18, 19, 20, 21, 22]

def Show_Animal_Boxes(image_path):
    img=cv2.imread(image_path)
    results = model(img, classes=animal_Id)
    boxes = results[0].boxes

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

    animal_count = len(boxes)
    cv2.putText(img, f"Animals: {animal_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Animal Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = input("Enter image path: ") 
Show_Animal_Boxes(image)   

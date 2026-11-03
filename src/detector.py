from ultralytics import YOLO
import cv2

# Added 'r' string formatting to prevent escape sequence syntax warnings
detector_model_path = r"models\Detection_model.pt"
detector_model = YOLO(detector_model_path)

def detector(image):
    detected_class = set()
    outputs = []
    results = detector_model(image, verbose=False)
    
    for result in results:
        boxes = result.boxes

        for box in boxes:
            # Flatten indexing safely across all modern Ultralytics YOLO variations
            cls = int(box.cls)
            confidence = float(box.conf)
            x1, y1, x2, y2 = box.xyxy.tolist()[0]
            
            class_name = detector_model.names[cls]
            detected_class.add(class_name)
            
            output = {
                "class": cls,
                "confidence": confidence,
                "box": [x1, y1, x2, y2]
            }
            outputs.append(output)

    print("\n---Detected ---")
    for clean_class in detected_class:
        print(clean_class)
    print("------------------------------\n")
        
    annotated_image = results[0].plot()

    cv2.imshow("Waste Detection", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()        

    return outputs

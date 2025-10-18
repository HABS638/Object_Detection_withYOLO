from ultralytics import YOLO

def run_inference_yolov8(image_path: str):
    model = YOLO('yolov8n.pt')
    results = model(image_path, show=True)
    return results

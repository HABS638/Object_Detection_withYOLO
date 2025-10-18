import torch

def run_inference_yolov5(image_path: str):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    results = model(image_path)
    results.show()
    return results

# Détection d'objets avec YOLOv5 et YOLOv8

## 🎯 Objectif du projet

Le projet consiste à exploiter deux architectures de détection d’objets, YOLOv5 et YOLOv8, afin de comparer leurs capacités de généralisation. YOLOv5, pré-entraîné sur Microsoft COCO, est utilisé pour la détection sur des images de référence, tandis que YOLOv8 (Ultralytics) est appliqué à des images locales choisies par l’utilisateur, permettant de tester librement la détection d’objets sur n’importe quelle image personnelle.

## 🧩 Description
- **YOLOv5** : modèle pré-entraîné sur COCO.  
- **YOLOv8** : modèle Ultralytics appliqué à des images locales.

## 🧠 Technologies utilisées
- Python
- PyTorch  
- Ultralytics YOLO  
- OpenCV / PIL  
- Matplotlib

## 📂 Structure du projet
```
Object_Detection_withYOLO/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── YOLOv5_COCO.ipynb
│   └── YOLOv8_Local.ipynb
│
├── src/
│   ├── inference_yolov5.py
│   ├── inference_yolov8.py
│   ├── utils.py
│
├── images/
│   └── examples/
│       ├── input_example.jpg
│       └── output_detection.jpg
│
└── reports/
    └── results_summary.md
```


## 🚀 Exécution
Installez les dépendances :  
```bash
pip install -r requirements.txt
```

Lancez un script :  
```bash
python src/inference_yolov8.py
```

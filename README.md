# Détection d'objets avec YOLOv5 et YOLOv8

## 🎯 Objectif du projet
Ce projet compare la performance de deux modèles de détection d’objets — **YOLOv5** et **YOLOv8** — sur des images issues du dataset COCO et sur des images locales.  
L’objectif est de comprendre leurs différences en termes de rapidité, précision et simplicité d’utilisation.

## 🧩 Description
- **YOLOv5** : modèle pré-entraîné sur COCO.  
- **YOLOv8** : modèle Ultralytics appliqué à des images locales.

## 🧠 Technologies utilisées
- Python 3.x  
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

## 📊 Résultats comparatifs (exemple)
| Modèle  | Temps d’inférence | Observation |
|----------|------------------|--------------|
| YOLOv5s | ~25 ms | Bonne précision |
| YOLOv8n | ~20 ms | Résultats plus fins |

## 🚀 Exécution
Installez les dépendances :  
```bash
pip install -r requirements.txt
```

Lancez un script :  
```bash
python src/inference_yolov8.py
```

## 👩‍💻 Auteur
Projet réalisé par **Habsatou Laoualy Chaibou**  
Master Ingénierie Mathématique et Data Science  
Université de Haute-Alsace, France

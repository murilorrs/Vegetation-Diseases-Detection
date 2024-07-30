import cv2
import numpy as np
import torch

def detect_objects(image_path):
    # Carregar o modelo YOLOv5 pré-treinado
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    img = cv2.imread(image_path)

    # Realizar inferência
    results = model(img)

    # Extrair labels e coordenadas dos resultados
    labels, cords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    return labels, cords, img, model

def draw_boxes(labels, cords, img, model):
    n = len(labels)
    classes = model.names

    for i in range(n):
        row = cords[i]
        if row[4] >= 0.5:  # Se a confiança estiver acima do limiar
            x1, y1, x2, y2 = int(row[0] * img.shape[1]), int(row[1] * img.shape[0]), int(row[2] * img.shape[1]), int(row[3] * img.shape[0])
            label = classes[int(labels[i])]
            color = (0, 255, 0)  # Cor verde para a caixa delimitadora
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    return img

if __name__ == "__main__":
    image_path = "data/images/test.jpg"
    labels, cords, img, model = detect_objects(image_path)
    img = draw_boxes(labels, cords, img, model)

    output_image_path = "output/images/test_detected.jpg"
    cv2.imwrite(output_image_path, img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

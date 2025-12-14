import requests

API_KEY = "0ni1aLOl4URBmjk08gjY"
MODEL_URL = https://serverless.roboflow.com

image_path = "C:/Users/Tom/ImagesTest/fissure.jpg"

with open(image_path, "rb") as f:
    response = requests.post(
        MODEL_URL,
        files={"file": f},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )

print("Résultat JSON :", response.json())

Delete detect_fissure.py (cleanup)

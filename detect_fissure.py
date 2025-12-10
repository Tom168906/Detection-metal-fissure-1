import requests

API_KEY = "VOTRE_CLE_API"
MODEL_URL = "VOTRE_URL_MODELE"

image_path = "fissure1.jpg"

with open(image_path, "rb") as f:
    response = requests.post(
        MODEL_URL,
        files={"file": f},
        headers={"Authorization": f"Bearer {API_KEY}"}
    )

print("Résultat JSON :", response.json())

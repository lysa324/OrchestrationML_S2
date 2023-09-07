import requests
from io import BytesIO
from PIL import Image

url = "http://127.0.0.1:5000/predict"  # Remplacez par l'adresse de votre API

# Ouvrir et rogner l'image
image1 = Image.open(r"C:\Users\lysa.amroun\Desktop\MyTestImage.jpg")
image_rognee = image1.crop((20, 30, 50, 236))
image_vide = Image.new("RGB", (10, 10))  # Créer une image vide
images = [image1, image_rognee, image_vide]

for idx, image in enumerate(images):

        # Convertir l'image en octets
        image_bytes = BytesIO()
        image.save(image_bytes, format="JPEG")
        image_bytes.seek(0)
        files = {'file': ('image.jpg', image_bytes, 'image/jpeg')}
        response = requests.post(url, files=files)
        print("Test Image", idx+1)
        print("Réponse:", response.status_code, response.json())
        print("="*50)
    

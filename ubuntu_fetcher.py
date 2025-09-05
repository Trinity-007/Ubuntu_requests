import os
import requests

print("Ubuntu-Inspired Image Fetcher")
print('"I am because we are" 🫂\n')

url = input("Enter the URL of the image: ").strip()

# Create folder
folder = "Fetched_Images"
os.makedirs(folder, exist_ok=True)

try:
    # Pretend to be a browser
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # check for HTTP errors

    # Extract filename or set default
    filename = url.split("/")[-1]
    if not filename:  
        filename = "downloaded_image.jpg"

    filepath = os.path.join(folder, filename)

    # Save image
    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"✅ Image saved successfully as {filepath}")

except requests.exceptions.HTTPError as e:
    print(f"❌ HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"❌ Network Error: {e}")

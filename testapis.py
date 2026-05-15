import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1/models?key={key}"

print(f"Testing Key: {key[:5]}...{key[-5:]}")
res = requests.get(url)

if res.status_code == 200:
    models = res.json().get('models', [])
    if not models:
        print("❌ Your key works, but it is allowed to see ZERO models.")
    else:
        print("✅ Your key can see these models:")
        for m in models:
            print(f" - {m['name']}")
else:
    print(f"❌ API Request Failed: {res.status_code} - {res.text}")
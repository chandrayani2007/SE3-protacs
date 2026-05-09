import requests
import sys

url = "https://media.githubusercontent.com/media/drugparadigm/SE3-protacs/main/model/SE(3)-PROTACs.pt"
out_path = "model/SE3-PROTACs.pt"

print(f"Downloading actual model file from {url}...")
try:
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    
    with open(out_path, 'wb') as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    done = int(50 * downloaded / total_size)
                    sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {downloaded/1024/1024:.2f} MB")
                    sys.stdout.flush()
    print("\nDownload complete!")
except Exception as e:
    print(f"\nFailed to download: {e}")

import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 🔧 CONFIG — Replace these with your own repo info
GITHUB_USER = "ezmarie-p"
REPO_NAME = "bot-pics"
BRANCH = "main"
FOLDER = "srb-pics"

# GitHub API URL to list contents of a folder
api_url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FOLDER}?ref={BRANCH}"

# jsDelivr base URL format
cdn_base = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}@{BRANCH}/{FOLDER}/"

# Make request to GitHub API
response = requests.get(api_url)
if response.status_code != 200:
    print(f"❌ Failed to fetch file list: {response.status_code}")
    print(response.json())
    exit()

data = response.json()

# Extract file names and generate full CDN URLs
image_urls = []
for file in data:
    if file["name"].lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".jfif")):
        image_urls.append(cdn_base + file["name"])

# Save URLs to a file
with open("image_urls.txt", "w") as f:
    for url in image_urls:
        f.write(url + "\n")

print(f"✅ Found {len(image_urls)} image URLs. Saved to image_urls.txt.")

import requests

url = "https://api.ipify.org"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

get_response = requests.get(url,headers=headers)
content = get_response.text

# Change Path and Filename
with open("<Path><FileName>.txt", mode="a") as file:
    file.write("\n" + content)
    file.close

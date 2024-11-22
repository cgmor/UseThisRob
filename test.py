import requests

# Define the server URL (adjust the port if necessary)
url = "http://127.0.0.1:8000/check-proximity"

# Define the payload with the address
payload = {
    "address": {
      "address": {
        "city": "Ann Arbor",
        "state": "Michigan",
        "street": "619 East University Avenue",
        "zip": "48104"
      }
    }
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response from the server
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
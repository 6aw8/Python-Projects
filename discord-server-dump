# Discord server Dumper
import requests
import json
ServerInvite = input("Please enter the server invite (code only): ")
url = f'https://discord.com/api/v9/invites/{ServerInvite}?with_counts=true&with_expiration=true&with_permissions=true'

request = requests.get(url)
print(request.text)

if request.status_code == 200:
    data = request.json()
    formatted = json.dumps(data, indent=4)
    print(formatted)
else:
    print(f"Failed. Code: {request.status_code}, {request.text}")



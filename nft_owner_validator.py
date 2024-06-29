import requests

network = int(input("Blockchain network id: "))
contract_address = input("Smart contract address: ")
address = input("Address to be verified: ")
nft_id = int(input("NFT id: "))

url = 'https://api.vottun.tech/erc/v1/erc721/ownerOf'
headers = {
    "Authorization": "Bearer <api_key>",
    "x-application-vkn": "<app_id>", 
    "Content-Type": "application/json"
        }

data = {   
    "contractAddress": contract_address,
    "network": network,
    "nft_id": nft_id
    }

try:
    response = requests.post(url, headers=headers, json=data,timeout=10)
    
    if response.status_code == 404:
        response.raise_for_status()
    if response.status_code == 401:
        print("Http error 401, NOT AUTHORIZED (hint: check api_key and app_id)")
        print(response.json())
    if response.status_code == 400:
        print("Http error 400. BAD REQUEST (hint: check the data you entered)")
        print(response.json())
    if response.status_code == 403:
        print("Http error 403. Forbidden. This action is forbidden for the client")
        print(response.json())
    if response.status_code == 402:
        response.raise_for_status()
    if response.status_code > 404:
        response.raise_for_status()


except requests.exceptions.HTTPError as he:
    print('The following HTTP error occurred:', he)

except requests.exceptions.ConnectionError as ce:
    print('There was a connection error:', ce)

except requests.exceptions.Timeout as te:
    print('Sorry, the request timed out:', te)

except ValueError as ve:
    print('There was a JSON decoding error:', ve)

else:
    if response.ok:
        json_data = response.json()
        nft_owner = json_data["owner"]
        if address == nft_owner:
            print("YES. This is the owner of the NFT.")
        else:
            print("NO. This is not the owner of the NFT")
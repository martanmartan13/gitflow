import requests

server = input()
port, a, b = int(input()), int(input()), int(input())

resp = requests.get(f"{server}:{port}", params={'a': a, 'b': b})
print(*sorted(resp.json()['result']))
print(resp.json()['check'])




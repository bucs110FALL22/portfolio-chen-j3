import requests

def main():
  response = requests.get("https://uselessfacts.jsph.pl/random.json")
  data = response.json()
  print(data)

main()
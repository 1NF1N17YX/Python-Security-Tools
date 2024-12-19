import requests

URL = "http://62.182.86.140/main/0/766d57fc58fb6f1f28db48d47a2203f4/Benjamin%20Caballero%2C%20Lindsay%20Allen%2C%20Andrew%20Prentice%20-%20Encyclopedia%20of%20human%20nutrition-Elsevier%20Science%20%28E%29%20%282008%29.pdf"


r = requests.get(URL, allow_redirects=True, stream = True)

with open("Science.pdf", "wb") as pdf:
	for chunk in r.iter_content(chunk_size=1024):
		if chunk:
			pdf.write(chunk)



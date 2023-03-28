import json
import time
import cgi

form = cgi.FieldStorage()
try:
    with open("database.json", "r") as infile:
        messages = json.load(infile)
except:
    messages = []

messages.append({
    "author": form["author"].value,
    "message": form["message"].value,
    "time": time.strftime("%d/%m/%Y, %H:%M:%S")
})

with open("database.json", "w") as outfile:
    json.dump(messages, outfile, indent=2, ensure_ascii=False)

print("<html>")
print("<head>")
print("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
print()
print("<title>Comentários</title>")
print("</head>")
print("<body background=\"../background.png\">")
print("<h1 align='center' style=\"color: white; text-shadow: 0.1em 0.01em 0.05em #000000;\">Comentários</h1>")
print("<div style=\"color: white; font-size:22; text-shadow: 0.1em 0.01em 0.05em #000000;\">")
for message in messages:
    print("Autor: " + message["author"] + "<br>")
    print("Menssagem: " + message["message"] + "<br>")
    print("Enviado as: " + message["time"] + "<br><br><br>")
print("</div>")
print("</body></html>")
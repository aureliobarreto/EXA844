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
print("<title>Blog da Dama</title>")
print("</head>")
print("<body background=\"../background.png\">")
print("""<h1 align=\"center\"  style=\" color: white;font-size: 28;text-shadow: 0.1em 0.01em 0.05em #000000;\">Blog da Dama</h1>
    <hr />
    <br />
    <div align="center" style=\" color: white;font-size: 28;text-shadow: 0.1em 0.01em 0.05em #000000;\">
        A partida da vez se trata de um clássico entre os jogadores Tuca e José Carlos ocorrida no dia 19 de julho de 2022.
        Tuca leva vantagem em número de vitórias. Mas no recorte recente, o Zé Carlos leva ampla vantagem,
        a MAIOR RIVALIDADE de damas em território nacional.
        Transmissões: 
        <br/>
        <a href=\"https://youtu.be/u1g9hPvqWz8\">Cazé TV</a>
        <br/>
        <a href=\"https://youtu.be/INZR-Bbr1Vc\">Video Oficial: </a>

    </div>""")
print(""" <h2 align=\"center\"style=\" color: white;font-size: 28;text-shadow: 0.1em 0.01em 0.05em #000000;\"> Deixe seu comentário</h2>
    <form
      method=\"POST\"
      action=\"/cgi-bin/server.py"
      align=\"center\"
      style=\" color: white;\"
    >
      <h3 style=\"margin-top: 0; margin-bottom: 0;\">Autor: </h3><br />
      <input type=\"text\" size=\"64\" name=\"author\" /><br /><br />
      <h3 style=\"margin-top: 0; margin-bottom: 0;\">Mensagem </h3> <br />
      <textarea rows=\"3\" cols=\"64\" name=\"message\"></textarea><br /><br />
      <input type=\"submit\" value=\"Enviar\" />
      <input type=\"reset\" value=\"Limpar Campos\" />
    </form>""") 
print("<h1 style=\"color: white; text-shadow: 0.1em 0.01em 0.05em #000000;\">Comentários</h1>")
print("<div style=\"color: white; font-size:22; text-shadow: 0.1em 0.01em 0.05em #000000;\">")
for message in messages:
    print("Autor: " + message["author"] + "<br>")
    print("Menssagem: " + message["message"] + "<br>")
    print("Enviado as: " + message["time"] + "<br><br><br>")
print("</div>")
print("</body></html>")
# ChatConnect Pro: Seamless WhatsApp-ChatGPT Integration

"""Get ChatGPT to talk to itself."""

import requests

# Launch two instances of server.py
# python server.py --port 5001 --profile /tmp/chat1
# python server.py --port 5002 --profile /tmp/chat2

metaprompt = "Oh..i thought: Make it more exciting!"
chat1 = requests.get("http://localhost:5001/chat?q=%s" % "Tell me how persons communicate!")
while True:
    chat2 = requests.get("http://localhost:5002/chat?q=%s" % (chat1.text.replace(metaprompt, "") + " " + metaprompt))
    chat1 = requests.get("http://localhost:5001/chat?q=%s" % (chat2.text.replace(metaprompt, "") + " " + metaprompt))

    
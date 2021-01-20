import requests

def slash():
    url = "https://discord.com/api/v8/applications/770143431770505238/guilds/231851662761918464/commands"

    json = {
        "name": "test",
        "description": "Send a embed test",
        "options": []
    }

    headers = {
        "Authorization": "NzcwMTQzNDMxNzcwNTA1MjM4.X5ZR9g.9C_R182qfRJ3FMLUhWrOoS458ms"
    }
    # print("AAA")
    r = requests.post(url, headers=headers, json=json)

# url = "https://discord.com/api/v8/applications/770143431770505238/guilds/770143431770505238/commands/<command_id>"
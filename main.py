from mcstatus import MinecraftServer
from libs import *

hub_ip = "proxy.uplacraft.fr"

hubs = {
    "hub01": {
        "ip": f"{hub_ip}:25565",
        "players": 0,
        "latency": 0,
        "score": 0,
        "online": False
    },
    "hub02": {
        "ip": f"{hub_ip}:25566",
        "players": 0,
        "latency": 0,
        "score": 0,
        "online": False
    }
}

print(average_players(hubs), hubs)

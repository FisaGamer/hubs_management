def lookup(hubs):
    for hub in hubs:
        try:
            server = MinecraftServer.lookup(hubs[hub]["ip"])
            status = server.status()
            hubs[hub]["players"] = status.players.online
            hubs[hub]["latency"] = status.latency
            hubs[hub]["score"] = status.players.online * status.latency
            hubs[hub]["online"] = True
        except:
            continue

def newserver():
    pass

def average_players(hubs):
    lookup(hubs)
    average = []
    for hub in hubs:
        if hubs[hub]["online"] == True:
            average.append(hubs[hub]["players"])
    if len(average) != 0:
        return(sum(average)/len(average))
    else:
        return 0
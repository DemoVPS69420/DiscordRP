import os
from pypresence import Presence
import time

i = 0
i2 = 0

print("Running...")

while True:
    status1 = [
    "Demo123",
    "Demo456",
    ]

    status2 = [
    "Demo123",
    "Demo456",
    ]

    RPC = Presence(977208472909254666)
    RPC.connect()

    RPC.update(
            state=status1[i],
            details=status2[i],
            start=time.time(),
            large_image=("https://media.tenor.com/9c83g4VPctQAAAAi/shaking-eyes-eyes-shaking.gif"), 
            large_text="Watching!",
            small_image=("https://media.giphy.com/media/4UjV5LeD66EPruSG18/giphy.gif"),
            small_text="Spinning",
            buttons=[
                {"label": "Website", "url": "https://qtqt.cf"},
                {"label": "Server", "url": "https://discord.gg/JF3kg77"}],
            party_size=[1,69]
    )

    time.sleep(10)
    i = (i + 1) % len(status1)
    i2 = (i + 1) % len(status2)
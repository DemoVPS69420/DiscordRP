import os
from pypresence import Presence
import time

print("Running... (keera_nezuko.py)")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Keera Nezuko Kamado (SS Collab)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/A9-F0-E955-4627-45-FA-A363-6522-AA2-CE00-D.jpg"), 
            large_text="Keera Nezuko Kamado",
            small_image="https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/1110855395368509520.png",
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
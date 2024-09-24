import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Mganga Pháp sư mèo (S+)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/4714-C3-D3-A78-C-4-FEF-977-D-0113-A137-F03-E.png?token=GHSAT0AAAAAACX7AZQ47NKE2ZGOCWRLJQH4ZXS6AZA"), 
            large_text="Mganga Pháp sư mèo",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
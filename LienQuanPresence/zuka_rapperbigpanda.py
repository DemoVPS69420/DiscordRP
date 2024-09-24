import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Zuka Rapper Big Panda (S+ Hữu hạn)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/43-C92-EFB-0-F4-D-4-AA7-B3-E4-BC96-AF257199.png"), 
            large_text="Zuka Rapper Big Panda",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Violet Thứ Nguyên Vệ Thần (Dimension Breaker Hữu hạn)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/0610-DB27-B29-B-4-A18-8092-C6-D83-B0978-D7.png"), 
            large_text="Violet Thứ Nguyên Vệ Thần",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
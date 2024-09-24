import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Violet Tiệc bãi biển (SS Hữu hạn)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/33-DFD461-9-D3-D-4-C2-C-BB1-E-D5-EE76-F5-A4-BE.png?token=GHSAT0AAAAAACX7AZQ5OOA2YOBNIBCVLAS6ZXS57VQ"), 
            large_text="Violet Tiệc bãi biển",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
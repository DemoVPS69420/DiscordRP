import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Yorn Thế tử nguyệt tộc (SS)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/CDAB3813-B305-4258-9-A1-A-9-F3558-F68122.png?token=GHSAT0AAAAAACX7AZQ4HJELLKPQMTR5K7UOZXS6CSQ"), 
            large_text="Yorn Thế tử nguyệt tộc",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
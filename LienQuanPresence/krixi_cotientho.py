import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Krixi Cô tiên thỏ (S)",
            start=time.time(),
            large_image=("https://i.ibb.co/DVGC6QJ/FD25012-B-1-FB2-48-D0-8213-EE67-A5-B7653-C.png"), 
            large_text="Krixi Cô tiên thỏ",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
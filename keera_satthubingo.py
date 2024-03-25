import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Keera Sát thủ bí ngô (S+ Hữu hạn)",
            start=time.time(),
            large_image=("https://i.ibb.co/JzNwhhQ/C5-DF3-CBC-2765-4800-988-F-4-EE5-C48-B39-CE.png"), 
            large_text="Keera Sát thủ bí ngô",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
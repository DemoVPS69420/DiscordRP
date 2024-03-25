import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Violet Huyết ma thần (SS Hữu hạn)",
            start=time.time(),
            large_image=("https://i.ibb.co/6FY92Yr/040-F5-A0-F-BD45-40-A2-A70-E-2-D41-D8608-F4-F.png"), 
            large_text="Violet Huyết ma thần",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
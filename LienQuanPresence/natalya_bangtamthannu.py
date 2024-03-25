import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Natalya Băng tâm thần nữ (S+ Hữu hạn)",
            start=time.time(),
            large_image=("https://i.ibb.co/2gSZmxD/C64-BD421-96-B6-4-E77-8579-C033410-B7161.png"), 
            large_text="Natalya Băng tâm thần nữ",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
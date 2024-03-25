import os
from pypresence import Presence
import time

print("Running...")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Valhein Xạ thần Kagutsuchi (EVO Tiến hóa)",
            start=time.time(),
            large_image=("https://i.ibb.co/9Y8STFQ/FCF5-C58-B-BB12-41-ED-9-E9-F-68659592-C69-A.png"), 
            large_text="Valhein Xạ thần Kagutsuchi",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
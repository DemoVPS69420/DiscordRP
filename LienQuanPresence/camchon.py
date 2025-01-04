import os
from pypresence import Presence
import time

print("Running...(camchon.py)")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đang tiến hành cấm chọn",
            state="Đang patch dữ liệu",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/IMG-3966.png"), 
            large_text="Liên Quân Mobile",
            small_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
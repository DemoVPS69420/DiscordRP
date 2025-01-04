import os
from pypresence import Presence
import time

print("Running...(arthur_tonhovosong.py)")

RPC = Presence(1152566755357626388)
RPC.connect()

RPC.update(
            details="Đấu xếp hạng",
            state="Arthur Tôn Hổ Vô Song (Mythic)",
            start=time.time(),
            large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/Full_1669_EDIT_1736000056083.jpg"), 
            large_text="Arthur Tôn Hổ Vô Song",
            small_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
          )
time.sleep(999999)
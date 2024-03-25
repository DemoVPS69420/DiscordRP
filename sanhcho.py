
import os
from pypresence import Presence
import time

i = 0
i2 = 0

print("Running...")

while True:
    status1 = [
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    ]

    status2 = [
    "Rank Cao Thủ x22",
    "Miền Nam Hậu Giang thứ 46 Violet",
    "Chiến lực (Violet): 4918",
    "Số trận: 3592",
    "Tướng: 87, Trang phục: 210",
    "Độ hot: 1038",
    "Tỷ lệ thắng: 54.1%",
    "Dấu ấn truyền kì: VIII",
    ]

    RPC = Presence(1152566755357626388)
    RPC.connect()

    RPC.update(
            state=status2[i],
            details=status1[i],
            start=1697994000,
            large_image=("https://i.ibb.co/jk3tfMz/IMG-3966.png"), 
            large_text="Liên Quân Mobile",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}],
    )

    time.sleep(10)
    i = (i + 1) % len(status1)
    i2 = (i + 1) % len(status2)
else:
    print("error happened")

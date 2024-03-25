import os
import asyncio
from pypresence import Presence
import time

RPC = Presence(1152566755357626388)
RPC.connect()

i = 0

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

async def mainpresence():
    while True:
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
    await time.sleep(10)

async def run():
    await mainpresence

async.run(run())
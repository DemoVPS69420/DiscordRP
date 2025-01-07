import os
import time
from datetime import datetime, timedelta, timezone
from pypresence import Presence

print("Running... (sanhcho.py)")

status1 = [
    "Tên ingame: HachizuOrigami",
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
    "Rank Cao Thủ x10",
    "Chiến lực (Keera): 5278",
    "Chiến lực (Violet): 5384",
    "Chiến lực (Arthur): 3464",
    "Số trận: 4500",
    "Tướng: 107, Trang phục: 279",
    "Độ hot: 1601",
    "Tỷ lệ thắng: 54.1%",
    "Dấu ấn truyền kì: XI",
]

RPC = Presence(1152566755357626388)

def connect_rpc():
    try:
        RPC.connect()
    except Exception as e:
        print(f"Failed to connect to Discord RPC: {e}")
        time.sleep(10)
        connect_rpc()

def get_gmt7_timestamp():
    gmt7 = timezone(timedelta(hours=7))
    now = datetime.now(gmt7)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(start_of_day.timestamp())

connect_rpc()

while True:
    try:
        for i in range(min(len(status1), len(status2))):
            RPC.update(
                state=status2[i],
                details=status1[i],
                start=get_gmt7_timestamp(),
                large_image="https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/IMG-3966.png", 
                large_text="Liên Quân Mobile",
                small_image="https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/1110855395368509520.png",
                small_text="Cao Thủ",
                buttons=[
                    {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}
                ],
            )
            time.sleep(15)  # Adjust the sleep time as needed
    except Exception as e:
        print(f"Error updating Discord RPC: {e}")
        connect_rpc()

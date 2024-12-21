import os
import time
from datetime import datetime, timedelta, timezone
from pypresence import Presence

print("Running...")

status1 = [
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
    "Tên ingame: HachizuOrigami",
]

status2 = [
    "Rank Tinh Anh II 3x",
    "No data",
    "Chiến lực (Keera): 5278",
    "Số trận: 4461",
    "Tướng: 106, Trang phục: 274",
    "Độ hot: 1",
    "Tỷ lệ thắng: 54%",
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
    return int((datetime.now(timezone.utc) + timedelta(hours=7)).timestamp())

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
                small_image="https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/1110855409629139034.png",
                small_text="Tinh Anh",
                buttons=[
                    {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}
                ],
            )
            time.sleep(15)  # Adjust the sleep time as needed
    except Exception as e:
        print(f"Error updating Discord RPC: {e}")
        connect_rpc()

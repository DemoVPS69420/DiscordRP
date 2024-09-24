import os
import asyncio
from pypresence import Presence
import time

# Your Discord application's client ID (replace with your actual ID)
CLIENT_ID = 1152566755357626388

RPC = Presence(CLIENT_ID)  # Connect to Discord RPC

# Initialize i and i2 as global variables
i = 0
i2 = 0

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


async def main_presence():
    """Updates Discord Rich Presence with status information."""
    global i, i2  # Declare i and i2 as global variables within the function

    while True:
        RPC.update(
            state=status2[i2],
            details=status1[i],
            start=1697994000,  # Set a custom start timestamp (optional)
            large_image=("https://i.ibb.co/jk3tfMz/IMG-3966.png"),
            large_text="Liên Quân Mobile",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}
            ],
        )

        # Update i and i2 within the function
        i = (i + 1) % len(status1)
        i2 = (i2 + 1) % len(status2)

        await asyncio.sleep(10)  # Wait for 10 seconds before updating again


async def run():
    """Starts the asynchronous presence update loop."""
    await main_presence()


if __name__ == "__main__":
    # Connect to Discord RPC before running the loop
    RPC.connect()
    asyncio.run(run())  # Start the asynchronous task
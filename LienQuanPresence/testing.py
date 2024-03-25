import os
from pypresence import Presence
import time
import asyncio

# Danh sách trạng thái
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

# Hàm bất đồng bộ để cập nhật trạng thái Discord
async def update_presence(status1, status2):
    RPC = Presence(1152566755357626388)
    RPC.connect()

    i = 0
    j = 0
    while True:
        RPC.update(
            state=status2[j],
            details=status1[i],
            start=1697994000,
            large_image=("https://i.ibb.co/jk3tfMz/IMG-3966.png"), 
            large_text="Liên Quân Mobile",
            small_image=("https://i.ibb.co/fpD8NBH/1110855395368509520.png"),
            small_text="Cao Thủ",
            buttons=[
                {"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}],
        )
        await asyncio.sleep(10)  # Chờ 10 giây trước khi cập nhật trạng thái tiếp
        i = (i + 1) % len(status1)
        j = (i + 1) % len(status2)

# Khởi động event loop và chạy hàm
if __name__ == "__main__":
    print("Running...")
    loop = asyncio.get_event_loop()  # Tạo event loop
    try:
        loop.run_until_complete(update_presence(status1, status2))  # Bắt đầu chạy hàm asyncio
    except KeyboardInterrupt:
        # Cho phép dừng script bằng Ctrl+C 
        pass 
    finally:
        loop.close()
        await asyncio.sleep(10)  # Asynchronous wait
        i = (i + 1) % len(status1)
        i2 = (i + 1) % len(status2)

async def main():
    task = asyncio.create_task(update_presence())
    await task  # Wait for the update_presence task to run (likely indefinitely)

asyncio.run(main())                                                                                                                                                                                                                                                

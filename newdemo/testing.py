from pypresence import Presence, ActivityType
import time

client_id = '1320714112069664860'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

RPC.update(
    activity_type = ActivityType.LISTENING, # Set the activity to listening
    details="Liên Quân Mobile",
    state="Đấu xếp hạng",
    start=time.time(),
    end=int(input("The length of the song (in seconds): ")) + time.time(),
    large_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/IMG-3966.png"), 
    large_text="Đang lấy dữ liệu tướng",
    small_image=("https://raw.githubusercontent.com/DemoVPS69420/DiscordRP/refs/heads/main/lienquanimage/1110855395368509520.png"),
    small_text="Cao Thủ",
    buttons=[{"label": "Server Discord của Garena LQM", "url": "https://discord.gg/lqm"}]
    # At time of writing this, timestamps don't show for listening statuses!
    # ...so this field is pointless lol
) # Get the user's favorite song!

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
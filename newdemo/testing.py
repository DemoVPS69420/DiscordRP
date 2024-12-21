from pypresence import Presence
import time

print("Running...")

# Replace 'your_client_id' with your actual client ID
client_id = '977208472909254666'
RPC = Presence(client_id)
RPC.connect()

# List of statuses to cycle through
statuses = [
    {
        "state": "What are you looking for?",
        "details": "Looking for something?",
        "large_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",  
        "large_text": "WELL",         
        "small_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",  
        "small_text": "TOUCH GRASS"
    },
    {
        "state": "Testing stuff",
        "details": "For something else?",
        "large_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "large_text": "Match Time",
        "small_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "small_text": "In Game"
    },
    {
        "state": "Listening to music",
        "details": "in the dreams",
        "large_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "large_text": "Lobby",
        "small_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "small_text": "Waiting"
    },
    {
        "state": "For some practice",
        "details": "with my life",
        "large_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "large_text": "Training",
        "small_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "small_text": "Practice"
    },
    {
        "state": "Cooking?",
        "details": "Well, I don't know",
        "large_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "large_text": "Replay",
        "small_image": "https://raw.githubusercontent.com/DemoVPS69420/MyNewWebsite/refs/heads/main/touch_grass.png",
        "small_text": "Analyzing"
    }
]

index = 0

# Update the Rich Presence every 10 seconds
while True:
    status = statuses[index]
    RPC.update(
        state=status["state"],
        details=status["details"],
        large_image=status["large_image"],
        large_text=status["large_text"],
        small_image=status["small_image"],
        small_text=status["small_text"],
        start=time.time()
    )
    index = (index + 1) % len(statuses)
    time.sleep(10)
import asyncio
import os
from pypresence import Presence
import time 

i = 0
i2 = 0

print("Running...")

async def update_presence():
    global i, i2

    status1 = [  # ... Your status arrays 
    # ...
    ]
    status2 = [
    # ...
    ]

    RPC = Presence(1152566755357626388)
    RPC.connect()

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

        await asyncio.sleep(10)  # Asynchronous wait
        i = (i + 1) % len(status1)
        i2 = (i + 1) % len(status2)

async def main():
    task = asyncio.create_task(update_presence())
    await task  # Wait for the update_presence task to run (likely indefinitely)

asyncio.run(main())                                                                                                                               rror happened")
                                                                                                                                % len(status2)
                                                                                                                                else:
                                                                                                                                    print("error happened")
                                                                                                                                     % len(status2)
                                                                                                                                     else:
                                                                                                                                         print("error happened")
                                                                                                                                         Here's howith experstandiwhile True strucusre are:

                                                                                                                                         Blocking time.sleep(): This function pausre are:

                                                                                                                                         Blocking time.sleep(): This function pausre are:

                                                                                                                                         Blocking time.sleep(): This function pausre are:

                                                                                                                                         Blocking time.sleep(): This function pauses the eng. In at loynciLack of Asyncis would halt the entire event loop.
                                                                                                                                         Lack of Asyncis would halt the entire event loop.
                                                                                                                                         Lack of Asyncot havs native apure asyncio app
                                                                                                                                         Python
                                                                                                                                         import amport time 
                                                                                                                                         t os
                                                                                                                                         from pypresence import Presence
                                                                                                                                         import time 
                                                                                                                                         t os
                                                                                                                                         from pypresence import Presence
                                                                                                                                         import time 
                                                                                                                                         t os
                                                                                                                                         from pypresence import Presence
                                                                                                                                         import time 
                                                                                                                                         t os
                                                                                                                                         from pypresence import Presence
                                                                                                                                         import time 

                                                                                                                                         i = 0
                                                                                                                                         ince():
                                                                                                                                          s arrays 
                                                                                                                                              # ...
                                                                                                                                               status1 = [  # ... Your status arrays 
                                                                                                                                                   # ...
                                                                                                                                                    status1 = [  # ... Your status arrays 
                                                                                                                                                        # ...
                                                                                                                                                            ]
                                                                                                                                                              11525667      RP  detaies=status1[i],
                                                                                                                                                                          start=1697994000,
                                                                                                                                                                                      largi],
                                                                                                                                                                                                  start=1697994000,
                                                                                                                                                                                                              largi],
                                                                                                                                                                                                                          start=1697994000,
                                                                                                                                                                                                                                      largi],
                                                                                                                                                                                                                                                  start=1697994000,
                                                                                                                                                                                                                                                              large_image=(     large_text=s://i.ib  small_text="Cao Thủ",
                                                                                                                                                                                                                                                                          "),
                                                                                                                                                                                                                                                                                      small_text="Cao Thủ",
                                                                                                                                                                                                                                                                                                  "),
                                                                                                                                                                                                                                                                                                              small_text="Cao Thủ",
                                                                                                                                                                                                                                                                                                                          "),
                                                                                                                                                                                                                                                                                                                                      small_text="Cao Thủ",
                                                                                                                                                                                                                                                                                                                                                  buttons=rena LQM", "url"wait asy + 1) % len(status1)
                                                                                                                                                                                                                                                                                                                                                          i2 = (i + 1) % i = (i + 1) % len(status1)
                                                                                                                                                                                                                                                                                                                                                                  i2 = (i + 1) % i = (i + 1) % len(status1)
                                                                                                                                                                                                                                                                                                                                                                          i2 = (i + 1) % i = (i + 1) % len(status1)
                                                                                                                                                                                                                                                                                                                                                                                  i2 = (i + 1) % len(stattask(update_presence task to run (likely indefifor the update_presence task to run (likely indefifor the update_presence task to run (likely indefinitely)

                                                                                                                                                                                                                                                                                                                                                                                  asyncio.run(main())

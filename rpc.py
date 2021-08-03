from pypresence import Presence
import time, sys, psutil

start_time=time.time()

def no_button(client_id, state, large_image, small_image, large_text, small_text):
    ## Discord stuffs
    RPC = Presence(client_id, pipe=0)  # Initialize the client class
    RPC.connect()  # Start the handshake loop
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)  # Get CPU Usage
        mem = psutil.virtual_memory()  # RAM
        mem_per = round(psutil.virtual_memory().percent, 1)
        RPC.update(
            details=f"RAM: {str(mem_per)}% | CPU: {str(cpu_per)}%",
            state=state,
            large_image=large_image,
            large_text=large_text,
            small_image=small_image,
            small_text=small_text,
            start=start_time,
            instance=True
        )  # Set the presence
        time.sleep(15)  # Can only update rich presence every 15 seconds

def one_button(client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url):
    ## Discord stuffs
    RPC = Presence(client_id, pipe=0)  # Initialize the client class
    RPC.connect()  # Start the handshake loop
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)  # Get CPU Usage
        mem = psutil.virtual_memory()  # RAM
        mem_per = round(psutil.virtual_memory().percent, 1)
        RPC.update(
            details=f"RAM: {str(mem_per)}% | CPU: {str(cpu_per)}%",
            state=state,
            large_image=large_image,
            large_text=large_text,
            small_image=small_image,
            small_text=small_text,
            buttons=[{"label": button1_text, "url": button1_url}],
            start=start_time,
            instance=True
        )  # Set the presence
        time.sleep(15)  # Can only update rich presence every 15 seconds

def two_button(client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url):
    ## Discord stuffs
    RPC = Presence(client_id, pipe=0)  # Initialize the client class
    RPC.connect()  # Start the handshake loop
    while True:
        cpu_per = round(psutil.cpu_percent(), 1)  # Get CPU Usage
        mem = psutil.virtual_memory()  # RAM
        mem_per = round(psutil.virtual_memory().percent, 1)
        RPC.update(
            details=f"RAM: {str(mem_per)}% | CPU: {str(cpu_per)}%",
            state=state,
            large_image=large_image,
            large_text=large_text,
            small_image=small_image,
            small_text=small_text,
            buttons=[{"label": button1_text, "url": button1_url}, {"label": button2_text, "url": button2_url}],
            start=start_time,
            instance=True
        )  # Set the presence
        time.sleep(15)  # Can only update rich presence every 15 seconds
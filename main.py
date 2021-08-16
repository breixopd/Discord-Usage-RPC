import rpc, time
from jsontest import importconfig

# RPC
client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url, os, startup = importconfig()

if startup == 1:
    time.sleep(30)

if button1_text == 0:
    rpc.no_button(client_id, state, large_image, small_image, large_text, small_text, os)
elif button1_text != 0 and button2_text == 0:
    rpc.one_button(client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, os)
elif button1_text != 0 and button2_text != 0:
    rpc.two_button(client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url, os)
else:
    print("Please check your config.json file")
    time.sleep(5)
    exit()
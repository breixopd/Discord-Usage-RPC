import json

def importconfig():
    with open("config.json", "r") as f:
        data = json.load(f)
    try:
        client_id = int(data["client_id"])
    except ValueError:
        print("'client_id' needs to be the number in the developer portal!")
        exit()
    state = data["state"]
    large_image = data["large_image"]
    small_image = data["small_image"]
    large_text = data["large_text"]
    small_text = data["small_text"]
    buttons = data["buttons"].upper()
    if buttons == "TRUE":
        try:
            buttonnum = int(data["buttonnum"])
            if buttonnum not in range(1, 3):
                print("Enter how many buttons you want in JSON! (1 or 2)")
                exit()
            elif buttonnum == 1:
                button1_text = data["button1_text"]
                button1_url = data["button1_url"]
                button2_text = 0
                button2_url = 0
                return client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url
            elif buttonnum == 2:
                button1_text = data["button1_text"]
                button1_url = data["button1_url"]
                button2_text = data["button2_text"]
                button2_url = data["button2_url"]
                return client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url
        except ValueError:
            print("Please enter a number in 'buttonnum'!")
            exit()
    elif buttons == "FALSE":
        button1_text = 0
        button1_url = 0
        button2_text = 0
        button2_url = 0
        return client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url
    elif buttons != "TRUE" or buttons != "FALSE":
        print("'buttons' needs to be TRUE or FALSE")
        exit()


client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url = importconfig()
print(f"Client ID: {client_id} | State: {state} | Large image ID: {large_image} | Small image ID: {small_image} | Large image text: {large_text} | Small image text: {small_text} | Button 1 text: {button1_text} | Button 1 URL: {button1_url} | Button 2 text: {button2_text} | Button 2 URL: {button2_url} || This is for testing purposes")
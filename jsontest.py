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
    if state == "":
        state = "Usage RPC: bit.ly/37Br9ml"
    large_image = data["large_image"]
    if large_image == "" or large_image == "YOUR_LARGE_IMAGE_ID":
        print("You need to enter something in 'large_image'!")
        exit()
    small_image = data["small_image"]
    if small_image == "" or small_image == "YOUR_SMALL_IMAGE_ID":
        print("You need to enter something in 'large_image'!")
        exit()
    large_text = data["large_text"]
    if large_text == "" or large_text == "YOUR_LARGE_IMAGE_TEXT":
        large_text = "Star on github!"
    small_text = data["small_text"]
    if small_text == "" or small_text == "YOUR_SMALL_IMAGE_TEXT":
        small_text = "By b2splashyy"
    os = data["os"].upper()
    if os == "TRUE":
        os = 1
    elif os == "FALSE":
        os = 0
    else:
        print("'os' needs to be TRUE of FALSE")
        exit()
    buttons = data["buttons"].upper()
    if buttons == "TRUE":
        try:
            buttonnum = int(data["buttonnum"])
            if buttonnum not in range(1, 3):
                print("Enter how many buttons you want in JSON! (1 or 2)")
                exit()
            elif buttonnum == 1:
                button1_text = data["button1_text"]
                if button1_text == "" or button1_text == "BUTTON_1_TEXT":
                    print("Enter something for 'button1_text'!")
                    exit()
                button1_url = data["button1_url"]
                if button1_url == "" or button1_url == "BUTTON_1_URL":
                    print("Enter something for 'button1_url'!")
                    exit()
                button2_text = 0
                button2_url = 0
                return client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url, os
            elif buttonnum == 2:
                button1_text = data["button1_text"]
                if button1_text == "" or button1_text == "BUTTON_1_TEXT":
                    print("Enter something for 'button1_text'!")
                    exit()
                button1_url = data["button1_url"]
                if button1_url == "" or button1_url == "BUTTON_1_URL":
                    print("Enter something for 'button1_url'!")
                    exit()
                button2_text = data["button2_text"]
                if button2_text == "" or button2_text == "BUTTON_2_TEXT":
                    print("Enter something for 'button2_text'!")
                    exit()
                button2_url = data["button2_url"]
                if button2_url == "" or button2_url == "BUTTON_2_URL":
                    print("Enter something for 'button2_url'!")
                    exit()
                return client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url, os
        except ValueError:
            print("Please enter a number in 'buttonnum'!")
            exit()
    elif buttons == "FALSE":
        button1_text = 0
        button1_url = 0
        button2_text = 0
        button2_url = 0
        return client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url, os
    elif buttons != "TRUE" or buttons != "FALSE":
        print("'buttons' needs to be TRUE or FALSE")
        exit()


client_id, state, large_image, small_image, large_text, small_text, button1_text, button1_url, button2_text, button2_url, os = importconfig()
print(f"Client ID: {client_id} | State: {state} | Large image ID: {large_image} | Small image ID: {small_image} | Large image text: {large_text} | Small image text: {small_text} | Button 1 text: {button1_text} | Button 1 URL: {button1_url} | Button 2 text: {button2_text} | Button 2 URL: {button2_url} | OS: {os} || This is for testing purposes")
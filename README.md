# Discord Usage RPC

A customizable Discord RPC that shows CPU and RAM usage. Made using [pypresence](https://github.com/qwertyquerty/pypresence)

## Installation
Download files and make an RPC [here](https://discord.com/developers/applications) (check Discord docs for how to add images, you can find them [here](https://discord.com/developers/docs/topics/rpc))

## Usage
Edit [the config file example](https://github.com/breixopd/Discord-Usage-RPC/blob/main/config_example.json) with the details for your RPC.
Rename `config_example.json` to `config.json` and put it in the same directory as the python files or `main.exe`.
Run `main.py` or `main.exe`. You can run `main.py` through an interpreter like [PyCharm](https://www.jetbrains.com/pycharm/) or do: 
```bash
python3 main.py
```
In your command line

## Config help
```
client_id - YOUR_ID
state - YOUR_STATE
large_image - YOUR_LARGE_IMAGE_ID
small_image - YOUR_SMALL_IMAGE_ID
large_text - YOUR_LARGE_IMAGE_TEXT
small_text - YOUR_SMALL_IMAGE_TEXT
buttons - TRUE/FALSE
buttonnum - 1/2 (Only 2 buttons can be added)
button1_text - BUTTON_1_TEXT
button1_url - BUTTON_1_URL
button2_text - BUTTON_2_TEXT
button2_url - BUTTON_2_URL
os - TRUE/FALSE (Will be shared in 'state', example, if 'state' is "hi" and 'os' is enabled it will show us as: "OS: [YOUR_OS] | hi")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPL3](https://choosealicense.com/licenses/gpl-3.0/)

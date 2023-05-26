# RiffApi Local

This project is a basic local server for the [Riff Racer](https://store.steampowered.com/app/351990) game. Since the servers of the game have been shut down, it is now impossible to create and play new tracks even if you wish to play in single player - thus a server implementation is necessary.

## Requirements

- Python 3.6+
- Flask

(Or Docker)

## Usage

### Patching ParseOctane.dll

Patch `ParseOctane.dll` to use RiffApi Local changing "https://parseapi.back4app.com" by "http://127.000000000.0.1:5144".

1. Open Steam and go to your game library
2. Right click on "Riff Racer" on the game list
3. Press on "manage" > "browse local files", it will open the folder where the game files are located.
4. Open a command prompt, `shift` + `right-click` and "Open PowerShell window here
5. Run `sed -i "s/https:\/\/parseapi.back4app.com/http:\/\/127.000000000.0.1:5144/g" ParseOctane.dll` or open "ParseOctane.dll" with a text editor and replace all the occurrences of "https://parseapi.back4app.com" by "http://127.000000000.0.1:5144".

### Running the API

You have two options:

1. Use [Docker](https://www.docker.com/products/docker-desktop/) (recommended).

   Open a command prompt on this directory and run `docker compose up --build`

2. Install [Python 3.6+](https://www.python.org/downloads/release/python-368/) and [Flask](https://pypi.org/project/Flask/).

   Run `riffapi-local.py`.

**Important**: keep open the command prompt until you exit the game.

## riffapi.hobune.stream

A more advanced online server with historic data is available at [riffapi.hobune.stream](https://riffapi.hobune.stream/). This server implementation here is for those wishing to run their own local server or in case the hobune server ever goes down.

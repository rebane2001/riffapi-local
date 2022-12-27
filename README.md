# RiffApi Local

This project is a basic local server for the [Riff Racer](https://store.steampowered.com/app/351990) game. Since the servers of the game have been shut down, it is now impossible to create and play new tracks even if you wish to play in single player - thus a server implementation is necessary.

## Requirements

- Python 3.6+
- Flask

## Usage

Run `sed -i "s/https:\/\/parseapi.back4app.com/http:\/\/127.000000000.0.1:5144/g" ParseOctane.dll` in your game directory to patch the Parse API DLL to use RiffApi Local instead. Then, run `riffapi-local.py` and launch the game.

## riffapi.hobune.stream

A more advanced online server with historic data is available at [riffapi.hobune.stream](https://riffapi.hobune.stream/). This server implementation here is for those wishing to run their own local server or in case the hobune server ever goes down.

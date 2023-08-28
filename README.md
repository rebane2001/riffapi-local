# RiffApi Local

This project is a basic local server for the [Riff Racer](https://store.steampowered.com/app/351990) game. Since the servers of the game have been shut down, it is now impossible to create and play new tracks even if you wish to play in single player - thus a server implementation is necessary.

## Requirements

- Python 3.6+
- Flask

(Or Docker)

## Usage

### Patching ParseOctane.dll

Patch `ParseOctane.dll` to use RiffApi Local changing "https://parseapi.back4app.com" with "http://127.000000000.0.1:5144".

You can do so with sed (`sed -i "s/https:\/\/parseapi.back4app.com/http:\/\/127.000000000.0.1:5144/g" ParseOctane.dll`), a hex editor, or by simply using the [website](https://riffapi.hobune.stream/).

### Running the API

There are multiple ways to run the server:

- Run with Python (recommended)
  1. Install [Python 3.6+](https://www.python.org/downloads/).
  2. Install [Flask](https://pypi.org/project/Flask/) with `pip install Flask`.
  3. Run `riffapi-local.py`.

- Run with Docker.
  1. Install Docker.
  2. Run with `docker compose up --build`.

**Important**: keep the command prompt open until you exit the game.

## riffapi.hobune.stream

A more advanced online server with historic data is available at [riffapi.hobune.stream](https://riffapi.hobune.stream/). This server implementation here is for those wishing to run their own local server or in case the hobune server ever goes down.

# Tests for [json-stream](https://github.com/daggaz/json-stream)

## Motivation

Article [Parsing JSON is a minefield](https://seriot.ch/projects/parsing_json.html) and it's collection of JSON examples.

## Clone

Note that this repository uses `git submodules`, so you should clone it with `--recursive` flag:
```bash
git clone --recursive https://github.com/jorektheglitch/json_stream_tests.git
```
or initalize submodules separately after cloning:
```bash
git submodule update --init --recursive
```

## Install dependencies

All dependencies listed in `requirements.txt`, so just create venv, activate ir:
```
python3 -m venv .venv
source .venv/bin/activate
```
and install dependencies:
```
pip install -r requirements.txt
```

## Run tests

```bash
mkdir -p logs
pytest tests | tee "logs/$(date '+%F %X.%N.log')"
```

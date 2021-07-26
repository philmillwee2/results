# results

Convert ACC results .json file to utf-8 for processing purposes.

## Installation

```
pip install -r requirements.txt
pip install -e .
```

## Usage

You'll need a data folder in the project directory. Store original JSON files in the data/original folder. You will also need a data/converted directory as well for the convert items.

To use this app run the **app.py** file using the `python` command.

```
python app.py
```

## Development

### Installation

This will setup the virtual environment and install any dependencies that you need for development.

```
make setup
```

### Usage

This will require activating the virtual environment where you're doing your development work.

```
source .venv/bin/activate
```

### Cleaning Environments

```
make clean
```

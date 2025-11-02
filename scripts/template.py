import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name
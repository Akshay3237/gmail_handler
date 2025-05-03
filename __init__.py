import sys
import os


if __name__=="gmail_handler":
    # Get directory of the current file and add it to sys.path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(script_dir)

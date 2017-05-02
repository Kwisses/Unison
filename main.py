# Unison - Python 3.5 - Johnathon Kwisses (Kwistech)

# Import for adding to Python Path
from os import path
import sys

# Handles main program logic
from brain import Brain


def main():
    # Add "Unison" to Python's path
    sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    # Initialize Brain class object.
    brain = Brain()
    brain.run()

if __name__ == "__main__":
    main()

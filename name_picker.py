import random

def pick_random_name(filename="names.txt"):
    """Reads names from a file and returns one randomly chosen name."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            names = [line.strip() for line in file if line.strip()]  # ignore empty lines
        if not names:
            raise ValueError("The file is empty or contains only blank lines.")
        return random.choice(names)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    chosen_name = pick_random_name()
    if chosen_name:
        print(f"The chosen name is: {chosen_name}")
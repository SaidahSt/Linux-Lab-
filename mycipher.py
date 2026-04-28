
import sys

# Get the shift amount from command line
shift = int(sys.argv[1])
processed_text = ""

# Read from Stdin
for line in sys.stdin:
    for char in line.upper():
        if 'A' <= char <= 'Z':
            # Shift character and wrap around alphabet
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            processed_text += shifted_char

# Print in blocks of 5, 10 blocks per line
for i in range(len(processed_text)):
    print(processed_text[i], end="")
    if (i + 1) % 5 == 0:
        # Check if we need a space or a newline
        if (i + 1) % 50 == 0:
            print()
        else:
            print(" ", end="")
print() # Final newline

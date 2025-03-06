"""
Same Example Without Flyweight Pattern (Heavy Version)

This demonstrates the same functionality as the previous example
but without using the Flyweight pattern - each character has its own
formatting object, which wastes memory.
"""


class CharacterFormat:
    """Format object that stores formatting attributes (no sharing)"""

    def __init__(self, font_name, font_size, bold, italic):
        self.font_name = font_name
        self.font_size = font_size
        self.bold = bold
        self.italic = italic

    def __repr__(self):
        bold_str = "bold" if self.bold else "normal"
        italic_str = "italic" if self.italic else "regular"
        return f"{self.font_name}, {self.font_size}pt, {bold_str}, {italic_str}"


class Character:
    """A character with position and its own formatting"""

    def __init__(self, char, x, y, font_name, font_size, bold, italic):
        self.char = char
        self.x = x
        self.y = y
        # Create a new format object for each character (wasteful)
        self.format = CharacterFormat(font_name, font_size, bold, italic)
        print(f"Created new format for '{char}': {self.format}")

    def render(self):
        """Render the character"""
        print(f"Character '{self.char}' at ({self.x}, {self.y}) with format [{self.format}]")


def main():
    """Example usage without flyweight pattern"""
    # Create a document with several characters
    document = []

    # Add some characters with the same formatting
    print("\nAdding 'Hello' with Arial 12pt bold:")
    x_pos = 0
    for char in "Hello":
        document.append(Character(char, x_pos, 0, "Arial", 12, True, False))
        x_pos += 10

    # Add some characters with different formatting
    print("\nAdding 'World!' with various formats:")
    for i, char in enumerate("World!"):
        if i % 2 == 0:
            # Even positions use the same format as "Hello"
            document.append(Character(char, x_pos, 0, "Arial", 12, True, False))
        else:
            # Odd positions use italic
            document.append(Character(char, x_pos, 0, "Arial", 12, True, True))
        x_pos += 10

    # Render the document
    print("\nRendering document:")
    for char in document:
        char.render()

    # Show memory usage (all characters have their own format)
    print(f"\nNumber of character objects: {len(document)}")
    print(f"Number of format objects: {len(document)} (each character has its own)")
    print(f"Memory wasted: {len(document) - 2} duplicate format objects compared to flyweight version")


if __name__ == "__main__":
    main()
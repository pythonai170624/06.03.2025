"""
Simple Flyweight Pattern Example

This demonstrates the Flyweight pattern with a text formatting example.
Characters share the same formatting attributes when possible to save memory.
"""


class CharacterFormat:
    """Flyweight object that stores shared formatting attributes"""

    def __init__(self, font_name, font_size, bold, italic):
        self.font_name = font_name
        self.font_size = font_size
        self.bold = bold
        self.italic = italic

    def __repr__(self):
        bold_str = "bold" if self.bold else "normal"
        italic_str = "italic" if self.italic else "regular"
        return f"{self.font_name}, {self.font_size}pt, {bold_str}, {italic_str}"


class FormatFactory:
    """Factory that manages format flyweights"""
    _formats = {}

    @classmethod
    def get_format(cls, font_name, font_size, bold, italic):
        # Create a key from the format attributes
        key = (font_name, font_size, bold, italic)

        # Return existing format if it exists
        if key not in cls._formats:
            cls._formats[key] = CharacterFormat(font_name, font_size, bold, italic)
            print(f"Created new format: {cls._formats[key]}")
        else:
            print(f"Reusing format: {cls._formats[key]}")

        return cls._formats[key]


class Character:
    """A character with position and formatting"""

    def __init__(self, char, x, y, font_name, font_size, bold, italic):
        self.char = char
        self.x = x
        self.y = y
        # Use flyweight for formatting
        self.format = FormatFactory.get_format(font_name, font_size, bold, italic)

    def render(self):
        """Render the character"""
        print(f"Character '{self.char}' at ({self.x}, {self.y}) with format [{self.format}]")


def main():
    """Example usage of the flyweight pattern"""
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

    # Show memory savings
    print(f"\nNumber of character objects: {len(document)}")
    print(f"Number of format objects: {len(FormatFactory._formats)}")
    print(f"Memory saving: {len(document) - len(FormatFactory._formats)} format objects")


if __name__ == "__main__":
    main()
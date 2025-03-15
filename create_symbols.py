from PIL import Image, ImageDraw, ImageFont

# Symbols for each face of the dice
symbols = ['α', 'β', 'γ', 'δ', 'Ω', 'Σ']  # Feel free to replace with your symbols

# Generate a PNG for each symbol
for i, symbol in enumerate(symbols, start=1):
    # Create a blank image
    img = Image.new('RGB', (256, 256), color='white')
    draw = ImageDraw.Draw(img)

    # Draw the symbol in the center of the image
    font_size = 120  # Adjust as needed
    try:
        # Use a default font (or replace with a path to a custom font)
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # Fallback if a proper font isn't found
        font = ImageFont.load_default()

    # Calculate the text size using getbbox()
    bbox = font.getbbox(symbol)  # Returns a bounding box as (x_min, y_min, x_max, y_max)
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text

    # Center the text on the image
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2
    draw.text((x, y), symbol, fill='black', font=font)

    # Save the image as "symbol1.png", "symbol2.png", etc.
    img.save(f"symbol{i}.png")

print("PNG files created!")

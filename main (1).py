import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def generate_certificates(excel_path, template_path, output_dir, font_path, font_size=64, y_position=None, text_color=(0, 0, 0)):
    # Debugging: Check paths
    print(f"Excel Path: {excel_path}")
    print(f"Template Path: {template_path}")
    print(f"Output Directory: {output_dir}")
    print(f"Font Path: {font_path}")

    # Check if files and directories exist
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"The Excel file path {excel_path} does not exist.")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"The template file path {template_path} does not exist.")
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"The output directory {output_dir} does not exist.")
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"The font file path {font_path} does not exist.")

    # Load the Excel sheet
    df = pd.read_excel(excel_path)

    # Loop through each name in the Excel sheet
    for index, row in df.iterrows():
        name = row['NAME'].strip()  # Remove any extra spaces

        # Open the certificate template
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        # Define the font and size
        font = ImageFont.truetype(font_path, font_size)

        # Get the image width to calculate the center along the x-axis
        img_width, img_height = img.size

        # Use textbbox to get the bounding box of the text (coordinates of the box around the text)
        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width = text_bbox[2] - text_bbox[0]

        # Center the text along the x-axis
        x_position = (img_width - text_width) // 2

        # Use the provided y_position or set a default if not provided
        if y_position is None:
            y_position = img_height // 2  # Default to center vertically

        # Draw the name on the certificate with specified color
        draw.text((x_position, y_position), name, text_color, font=font)

        # Save the certificate
        output_path = os.path.join(output_dir, f"{name}_certificate.jpg")
        img.save(output_path)
        print(f"Saved certificate for {name} at {output_path}")


# Usage
excel_path = input('Enter Path to your Excel file with names:').strip()
template_path = input('Enter Path to your certificate template:').strip()
output_dir = input('Enter the Directory where you want to save the certificates:').strip()
font_path = input('Enter Path to the font file you want to use:').strip()

# Optional parameters
text_color = (2, 111, 114)  # Change to your desired text color
y_position = 350 # Specify your desired y-axis position

generate_certificates(excel_path, template_path, output_dir, font_path, y_position=y_position, text_color=text_color)

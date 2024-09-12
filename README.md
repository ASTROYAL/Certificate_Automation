# Certificate Name Generator

This Python project automates the process of adding names to a certificate template. Given a list of names, the script customizes each certificate by placing the name in a predefined location on the template image.

## Features

- Automatically adds names to a certificate image.
- Supports custom font style, size, and color for the name text.
- Saves certificates in a specified directory with unique filenames.
- Can handle bulk name lists from a text or CSV file.

## Requirements

- Python 3.x
- Libraries:
  - `Pillow` for image processing
  - `csv` for handling name lists in CSV format (optional)
  
Install the required libraries using:
```bash
pip install Pillow
```

## Usage

1. Place your certificate template (`certificate_template.png`) in the project directory. Ensure it has enough space where the names will be placed.
2. Modify the script to specify the coordinates, font style, and size for the name placement on the certificate.
3. Provide a list of names in a text file (`names.txt`) or CSV file (`names.csv`).

### Running the Script

To run the script:

```bash
python certificate_generator.py
```

Make sure to configure the following parameters in the script:
- `TEMPLATE_PATH`: Path to your certificate template.
- `OUTPUT_DIR`: Directory where the generated certificates will be saved.
- `FONT_PATH`: Path to the `.ttf` font file.
- `FONT_SIZE`: Font size for the name.
- `NAME_COORDS`: X, Y coordinates for the name placement.

### Example

For example, if you have a list of names in `names.txt`, running the script will generate personalized certificates in the `output/` folder.

### Customization

You can customize:
- Font style by changing the `.ttf` file.
- Font size, color, and positioning by modifying the `draw.text()` method.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.

## License

This project is licensed under the MIT License.

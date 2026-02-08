# QR Code Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![GitHub last commit](https://img.shields.io/github/last-commit/athomft/GenerateQRCodes)](https://github.com/athomft/GenerateQRCodes/commits/master)

This Python script generates QR codes with unique random 10-digit numbers and saves them in an organized output directory along with an Excel file.

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
- [Sample Output](#sample-output)
- [License](#license)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/athomft/GenerateQRCodes.git
   cd GenerateQRCodes
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode

Run the script and enter the number of QR codes when prompted:
```bash
python main.py
```

### Command-Line Mode

Generate QR codes directly with command-line arguments:
```bash
# Generate 10 QR codes
python main.py -n 10

# Specify custom output directory
python main.py -n 10 -o my_qr_codes

# Specify custom Excel filename
python main.py -n 10 -e my_codes.xlsx

# Combine options
python main.py -n 10 -o custom_output -e custom_file.xlsx
```

### Command-Line Options

- `-n, --number`: Number of QR codes to generate
- `-o, --output`: Output directory (default: `output`)
- `-e, --excel`: Excel filename (default: `QR_Codes.xlsx`)
- `-h, --help`: Show help message
## Features

- ✓ Generates unique 10-digit random numbers (no duplicates)
- ✓ Creates QR codes as PNG images
- ✓ Organizes output in a dedicated directory
- ✓ Saves all numbers to an Excel file
- ✓ Command-line arguments for automation
- ✓ Error handling for file operations
- ✓ Progress tracking during generation

## Code Explanation

- `generate_random_10_digit(existing_numbers)`: Generates a unique random 10-digit number not in the existing set.
- `generate_qr_code(data, filename)`: Generates a QR code with the provided data and saves it as a PNG image with error handling.
- `save_to_excel(numbers, filepath)`: Saves the generated 10-digit numbers to a specified Excel file.
- `create_output_directory(output_dir)`: Creates the output directory if it doesn't exist.
- `parse_arguments()`: Parses command-line arguments for flexible usage.

## Sample Output

After running the script, you'll see:
```
QR code 1/10 generated: 1234567890
Saved as output/1234567890.png

QR code 2/10 generated: 9876543210
Saved as output/9876543210.png
...

✓ Successfully generated 10/10 QR codes
✓ Numbers saved to output/QR_Codes.xlsx
```

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


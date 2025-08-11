# QR Code Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![GitHub last commit](https://img.shields.io/github/last-commit/athomft/GenerateQRCodes)](https://github.com/athomft/GenerateQRCodes/commits/master)

This Python script generates QR codes with random 10-digit numbers and saves them in a specified Excel file.

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
- [Sample Output](#sample-output)
- [License](#license)

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/athomft/qr-code-generator.git
   ```
2. Clone this repository:
   ```bash
   pip install qrcode[pil] openpyxl
   ```
3. Run the script:
   ```bash
   python3 qr_code_generator.py
   ```
4. Enter the number of QR codes to generate when prompted.

## Installation

You can install the required libraries using pip:
   ```bash
   pip install qrcode[pil] openpyxl
   ```
## Code Explanation

- `generate_random_10_digit()`: Generates a random 10-digit number.
- `generate_qr_code(data, filename)`: Generates a QR code with the provided data and saves it as a PNG image.
- `save_to_excel(numbers)`: Saves the generated 10-digit numbers to an Excel file named "QR Codes.xlsx".

## Sample Output

After running the script and entering the number of QR codes to generate, the script generates QR codes with random 10-digit numbers and saves them as PNG images. The list of generated numbers is also saved to an Excel file named "QR Codes.xlsx".

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


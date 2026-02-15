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

Run the script from the terminal:

```bash
python main.py
```

## Code Explanation

The script generates unique 10-digit identifiers, creates corresponding QR code images using the `qrcode` library, and exports the data mapping to an Excel file using `openpyxl`.

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

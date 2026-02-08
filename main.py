import qrcode
import random
import argparse
import os
import sys
from pathlib import Path
from openpyxl import Workbook

# QR Code Configuration Constants
QR_VERSION = 1
QR_ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H
QR_BOX_SIZE = 10
QR_BORDER = 4
DEFAULT_OUTPUT_DIR = "output"
DEFAULT_EXCEL_FILENAME = "QR_Codes.xlsx"


def generate_random_10_digit(existing_numbers):
    """Generate a unique random 10-digit number not in existing_numbers set."""
    max_attempts = 10000
    for _ in range(max_attempts):
        number = ''.join(random.choices('0123456789', k=10))
        if number not in existing_numbers:
            return number
    raise RuntimeError("Unable to generate unique number after maximum attempts")


def generate_qr_code(data, filename):
    """Generate a QR code with the provided data and save it as a PNG image."""
    try:
        qr = qrcode.QRCode(
            version=QR_VERSION,
            error_correction=QR_ERROR_CORRECTION,
            box_size=QR_BOX_SIZE,
            border=QR_BORDER,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(filename)
        return True
    except Exception as e:
        print(f"Error generating QR code: {e}", file=sys.stderr)
        return False


def save_to_excel(numbers, filepath):
    """Save the generated 10-digit numbers to an Excel file."""
    try:
        wb = Workbook()
        ws = wb.active
        ws.append(["QR Codes"])
        for number in numbers:
            ws.append([number])
        wb.save(filepath)
        return True
    except Exception as e:
        print(f"Error saving to Excel: {e}", file=sys.stderr)
        return False


def create_output_directory(output_dir):
    """Create output directory if it doesn't exist."""
    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating output directory: {e}", file=sys.stderr)
        return False


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate QR codes with random 10-digit numbers"
    )
    parser.add_argument(
        '-n', '--number',
        type=int,
        help='Number of QR codes to generate'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=DEFAULT_OUTPUT_DIR,
        help=f'Output directory for QR codes (default: {DEFAULT_OUTPUT_DIR})'
    )
    parser.add_argument(
        '-e', '--excel',
        type=str,
        default=DEFAULT_EXCEL_FILENAME,
        help=f'Excel filename (default: {DEFAULT_EXCEL_FILENAME})'
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    
    # Create output directory
    if not create_output_directory(args.output):
        sys.exit(1)
    
    # Get number of QR codes to generate
    if args.number:
        num_qr_codes = args.number
    else:
        while True:
            try:
                num_qr_codes = int(
                    input("Enter the number of QR codes to generate: "))
                if num_qr_codes <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Generate QR codes with duplicate prevention
    numbers = []
    existing_numbers = set()
    successful = 0
    
    for i in range(num_qr_codes):
        try:
            random_data = generate_random_10_digit(existing_numbers)
            existing_numbers.add(random_data)
            numbers.append(random_data)
            
            filename = os.path.join(args.output, f"{random_data}.png")
            if generate_qr_code(random_data, filename):
                successful += 1
                print(f"QR code {i+1}/{num_qr_codes} generated: {random_data}")
                print(f"Saved as {filename}\n")
            else:
                print(f"Failed to generate QR code {i+1}")
        except RuntimeError as e:
            print(f"Error: {e}", file=sys.stderr)
            break
    
    # Save to Excel
    if numbers:
        excel_path = os.path.join(args.output, args.excel)
        if save_to_excel(numbers, excel_path):
            print(f"\n✓ Successfully generated {successful}/{num_qr_codes} QR codes")
            print(f"✓ Numbers saved to {excel_path}")
        else:
            print(f"\n✓ Generated {successful}/{num_qr_codes} QR codes")
            print("✗ Failed to save Excel file")
    else:
        print("No QR codes were generated.")

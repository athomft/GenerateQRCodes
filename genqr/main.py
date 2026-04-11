import qrcode
import secrets
import argparse
import sys
import string
import subprocess
from pathlib import Path
from openpyxl import Workbook

__version__ = "2.0.0"
__last_update__ = "2026-04-11 13:30:00"

# ASCII Banner
BANNER = rf"""
  _____ ______ _   _  ____  _____  
 / ____|  ____| \ | |/ __ \|  __ \ 
| |  __| |__  |  \| | |  | | |__) |
| | |_ |  __| | . ` | |  | |  _  / 
| |__| | |____| |\  | |__| | | \ \ 
 \_____|______|_| \_|\___\_\_|  \_\
                                    
genqr version {__version__} {__last_update__}
Command-line QR code generator with secure identifiers
Generate QR codes with random 10-digit numbers
"""

# QR Code Configuration Constants
QR_VERSION = 1
QR_ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H
QR_BOX_SIZE = 10
QR_BORDER = 4
DEFAULT_OUTPUT_DIR = "output"
DEFAULT_EXCEL_FILENAME = "QR_Codes.xlsx"
EXCEL_HEADER = "Code"


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Custom formatter to match specific Usage and Options styling."""
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = "Usage:\n  "
        return super().add_usage(usage, actions, groups, prefix)


def is_frozen():
    """Check if the app is running as a PyInstaller bundle."""
    return getattr(sys, 'frozen', False)

def update_app():
    """Update the app using installation scripts or pip."""
    print("Checking for updates...")
    try:
        if is_frozen():
            if sys.platform == "win32":
                cmd = 'powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/athomft/GenerateQRCodes/main/scripts/install.ps1 | iex"'
                subprocess.Popen(cmd, shell=True)
            else:
                cmd = 'curl -sSL https://raw.githubusercontent.com/athomft/GenerateQRCodes/main/scripts/install.sh | bash'
                subprocess.Popen(cmd, shell=True)
            print("\n✓ Update initiated. Please wait a moment for the new version to download.")
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "genqr"])
            print("\n✓ Update check complete. If a newer version was available, it has been installed.")
    except Exception as e:
        print(f"\n✗ Error during update: {e}")
        sys.exit(1)
    sys.exit(0)


def uninstall_app():
    """Uninstall the app via scripts or pip."""
    confirm = input("Are you sure you want to uninstall genqr? (y/N): ").strip().lower()
    if confirm == 'y':
        try:
            if is_frozen():
                exe_path = sys.executable
                if sys.platform == "win32":
                    import tempfile
                    bat_path = Path(tempfile.gettempdir()) / "uninstall_genqr.bat"
                    with open(bat_path, "w") as f:
                        f.write(f'@echo off\ntimeout /t 2 /nobreak > NUL\ndel "{exe_path}"\ndel "%~f0"\n')
                    subprocess.Popen([str(bat_path)], shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    Path(exe_path).unlink(missing_ok=True)
                print("\n✓ Uninstall complete. Goodbye!")
            else:
                print("Uninstalling genqr...")
                subprocess.Popen([sys.executable, "-m", "pip", "uninstall", "-y", "genqr"])
                print("\n✓ Uninstall initiated. You may now close this terminal.")
        except Exception as e:
            print(f"\n✗ Error during uninstall: {e}")
            sys.exit(1)
    else:
        print("Uninstall cancelled.")
    sys.exit(0)


def generate_random_10_digit(existing_numbers):
    """Generate a unique random 10-digit number not in existing_numbers set."""
    max_attempts = 10000
    digits = string.digits
    for _ in range(max_attempts):
        number = ''.join(secrets.choice(digits) for _ in range(10))
        if number not in existing_numbers:
            return number
    raise RuntimeError("Critical: Unable to generate a unique number after 10,000 attempts.")


def generate_qr_code(data, filename):
    """Generate a QR code and save it as a PNG image."""
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
        img.save(str(filename))
        return True
    except Exception as e:
        print(f"Error generating QR code for '{data}': {e}", file=sys.stderr)
        return False


def save_to_excel(numbers, filepath):
    """Save the generated 10-digit numbers to an Excel file."""
    try:
        wb = Workbook()
        ws = wb.active
        ws.append([EXCEL_HEADER])
        for number in numbers:
            ws.append([number])
        wb.save(str(filepath))
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
        print(f"Error creating output directory '{output_dir}': {e}", file=sys.stderr)
        return False


def positive_int(value):
    """Argparse type checker for positive integers."""
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid integer")


def get_parser():
    """Create and return the argument parser."""
    parser = argparse.ArgumentParser(
        prog="genqr",
        description="",
        formatter_class=CustomHelpFormatter,
        epilog="Example: genqr -n 10 -o my_qrcodes",
        add_help=False
    )
    
    group = parser.add_argument_group("Options")
    group.add_argument(
        '-v', '--version',
        action='version',
        version=f'genqr {__version__} {__last_update__}'
    )
    group.add_argument(
        '-n', '--number',
        type=positive_int,
        help='Number of QR codes to generate (must be > 0)'
    )
    group.add_argument(
        '-o', '--output',
        type=str,
        default=DEFAULT_OUTPUT_DIR,
        help=f'Output directory for QR codes (default: {DEFAULT_OUTPUT_DIR})'
    )
    group.add_argument(
        '-e', '--excel',
        type=str,
        default=DEFAULT_EXCEL_FILENAME,
        help=f'Excel filename (default: {DEFAULT_EXCEL_FILENAME})'
    )
    group.add_argument(
        '--update',
        action='store_true',
        help='Check for updates and install the latest version'
    )
    group.add_argument(
        '--uninstall',
        action='store_true',
        help='Completely remove the application from your system'
    )
    group.add_argument(
        '-h', '--help',
        action='help',
        help='Show help message and exit'
    )
    return parser


def main():
    """Main entry point for the genqr CLI."""
    parser = get_parser()

    # If no arguments are provided, show banner AND help, then CONTINUE to app execution
    if len(sys.argv) == 1:
        print(BANNER)
        parser.print_help()
        print("\n" + "="*50 + "\n")
        args = parser.parse_args([]) 
    else:
        args = parser.parse_args()
        print(BANNER)

    # Handle Update and Uninstall
    if args.update:
        update_app()
    if args.uninstall:
        uninstall_app()

    # Create output directory
    if not create_output_directory(args.output):
        sys.exit(1)
    
    # Get number of QR codes to generate
    if args.number:
        num_qr_codes = args.number
    else:
        while True:
            try:
                user_input = input("Enter the number of QR codes to generate (or 'q' to quit): ").strip().lower()
                if user_input == 'q':
                    print("Exiting.")
                    sys.exit(0)
                num_qr_codes = int(user_input)
                if num_qr_codes <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number or 'q'.")
    
    # Generate QR codes with duplicate prevention
    numbers = []
    existing_numbers = set()
    successful = 0
    
    print(f"\nStarting generation of {num_qr_codes} QR codes...")
    
    for i in range(num_qr_codes):
        try:
            random_data = generate_random_10_digit(existing_numbers)
            existing_numbers.add(random_data)
            numbers.append(random_data)
            
            filename = Path(args.output) / f"{random_data}.png"
            if generate_qr_code(random_data, filename):
                successful += 1
                print(f"[{i+1}/{num_qr_codes}] Generated: {random_data}")
            else:
                print(f"[{i+1}/{num_qr_codes}] Failed to generate image for {random_data}")
        except RuntimeError as e:
            print(f"\nStopped early: {e}", file=sys.stderr)
            break
    
    # Save to Excel
    if numbers:
        excel_path = Path(args.output) / args.excel
        if save_to_excel(numbers, excel_path):
            print(f"\n✓ Successfully generated {successful}/{num_qr_codes} QR codes")
            print(f"✓ Manifest saved to: {excel_path}")
        else:
            print(f"\n✓ Generated {successful}/{num_qr_codes} QR codes")
            print(f"✗ Failed to save manifest to: {excel_path}")
    else:
        print("\nNo QR codes were generated.")


if __name__ == '__main__':
    main()

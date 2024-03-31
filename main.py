import qrcode
import random
from openpyxl import Workbook


def generate_random_10_digit():
    return ''.join(random.choices('0123456789', k=10))


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)


def save_to_excel(numbers):
    wb = Workbook()
    ws = wb.active
    ws.append(["QR Codes"])
    for number in numbers:
        ws.append([number])
    wb.save(f"QR Codes.xlsx")


if __name__ == '__main__':
    numbers = []

    while True:
        try:
            num_qr_codes = int(
                input("Enter the number of QR codes to generate: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(num_qr_codes):
        random_data = generate_random_10_digit()
        numbers.append(random_data)
        filename = f"{random_data}.png"
        generate_qr_code(random_data, filename)
        print(
            f"QR code {i+1} generated with random 10-digit number: ", random_data)
        print(f"Saved as {filename}\n")

    save_to_excel(numbers)
    print("10-digit number saved to QR Codes.xlsx")

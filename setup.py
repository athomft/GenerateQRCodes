from setuptools import setup, find_packages

setup(
    name="genqr",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "qrcode[pil]>=7.0,<8",
        "openpyxl>=3.0.0,<4",
    ],
    entry_points={
        "console_scripts": [
            "genqr=genqr.main:main",
        ],
    },
    author="athomft",
    description="A professional CLI tool to generate QR codes with unique 10-digit identifiers",
    python_requires=">=3.6",
)

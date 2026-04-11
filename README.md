# genqr

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**genqr** is a professional, cross-platform CLI tool to generate batches of QR codes with unique identifiers.

```text
  _____ ______ _   _  ____  _____  
 / ____|  ____| \ | |/ __ \|  __ \ 
| |  __| |__  |  \| | |  | | |__) |
| | |_ |  __| | . ` | |  | |  _  / 
| |__| | |____| |\  | |__| | | \ \ 
 \_____|______|_| \_|\___\_\_|  \_\
```

## Features

- **No Python Required**: Standalone binary for Windows, macOS, and Linux.
- **Single-Command Install**: Fast setup via terminal.
- **Self-Managing**: Built-in `--update` and `--uninstall` commands.
- **Secure Randomness**: Uses secure cryptographically strong identifiers.

## Installation

### Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/athomft/GenerateQRCodes/main/scripts/install.ps1 | iex
```

### macOS / Linux (Terminal)
```bash
curl -sSL https://raw.githubusercontent.com/athomft/GenerateQRCodes/main/scripts/install.sh | bash
```

## Usage

### Direct Command
```bash
genqr -n 10
```

### Options
| Option | Short | Description |
|--------|--------|-------------|
| `--number` | `-n` | Number of QR codes to generate |
| `--output` | `-o` | Output directory (default: `output`) |
| `--excel` | `-e` | Excel filename (default: `QR_Codes.xlsx`) |
| `--update` | | Check for updates and install the latest version |
| `--uninstall` | | Completely remove the application from your system |
| `--version` | `-v` | Show version and exit |
| `--help` | `-h` | Show help message and exit |

## License

This project is licensed under the MIT License.

#!/usr/bin/env bash
set -e

# Wait briefly in case this was called from the app's --update command
sleep 1

REPO="athomft/GenerateQRCodes"
BIN_NAME="genqr"

# Determine OS
OS="$(uname -s)"
if [ "$OS" = "Linux" ]; then
    TARGET_OS="Linux"
elif [ "$OS" = "Darwin" ]; then
    TARGET_OS="macOS"
else
    echo "Unsupported OS: $OS"
    exit 1
fi

# Fetch latest release URL
echo "Looking for the latest release..."
LATEST_URL=$(curl -s https://api.github.com/repos/$REPO/releases/latest | grep "browser_download_url" | grep "$TARGET_OS" | cut -d '"' -f 4)

if [ -z "$LATEST_URL" ]; then
    echo "Could not find a pre-compiled release for $TARGET_OS."
    echo "Please check the GitHub Releases page."
    exit 1
fi

# Define install directory
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

echo "Downloading $BIN_NAME for $TARGET_OS..."
curl -sSL -o "$INSTALL_DIR/$BIN_NAME" "$LATEST_URL"
chmod +x "$INSTALL_DIR/$BIN_NAME"

echo ""
echo "✓ genqr installed successfully to $INSTALL_DIR/$BIN_NAME"

if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "ℹ️  Please add $INSTALL_DIR to your PATH to run 'genqr' from anywhere."
    echo "   Example for bash: echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
    echo "   Example for zsh:  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.zshrc"
fi

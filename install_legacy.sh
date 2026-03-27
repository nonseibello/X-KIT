#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}     X-KIT Legacy Installer             ${NC}"
echo -e "${GREEN}========================================${NC}"

echo -e "${YELLOW}[!] Installing legacy version${NC}"
echo -e "${YELLOW}[!] For older distributions (Ubuntu 20.04, Debian 11, etc.)${NC}\n"

echo -e "${GREEN}Downloading X-KIT (legacy version)...${NC}"

URL="https://github.com/nonseibello/X-KIT/releases/download/v1.0/xkit_old.tar.gz"

wget -q --show-progress $URL -O /tmp/xkit_old.tar.gz

if [ $? -ne 0 ] || [ ! -f /tmp/xkit_old.tar.gz ]; then
    echo -e "${RED}Download failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Extracting...${NC}"
cd /tmp

tar -xzf xkit_old.tar.gz
EXTRACT_RESULT=$?

if [ $EXTRACT_RESULT -ne 0 ]; then
    echo -e "${RED}Extraction failed!${NC}"
    exit 1
fi

if [ -f /tmp/xkit ]; then
    BINARY_NAME="xkit"
elif [ -f /tmp/xkit-new ]; then
    BINARY_NAME="xkit-new"
else
    echo -e "${RED}Binary not found after extraction!${NC}"
    echo "Files in /tmp:"
    ls -la /tmp/xkit* 2>/dev/null
    exit 1
fi

echo -e "${GREEN}Found binary: $BINARY_NAME${NC}"

echo -e "${GREEN}Installing to /usr/local/bin...${NC}"
sudo cp /tmp/$BINARY_NAME /usr/local/bin/xkit
sudo chmod +x /usr/local/bin/xkit

rm -f /tmp/xkit_old.tar.gz /tmp/xkit /tmp/xkit-new 2>/dev/null

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}X-KIT (legacy version) installed!${NC}"
echo -e "${GREEN}Run with: sudo xkit${NC}"
echo -e "${GREEN}========================================${NC}"


if command -v xkit &> /dev/null; then
    echo -e "${GREEN}✓ Installation successful!${NC}"
else
    echo -e "${RED}✗ Installation failed - xkit not found in PATH${NC}"
fi

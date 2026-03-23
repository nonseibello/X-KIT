#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}     X-KIT Network Tool Installer       ${NC}"
echo -e "${GREEN}========================================${NC}"

echo -e "${GREEN}Downloading X-KIT...${NC}"

URL="https://github.com/nonseibello/X-KIT/releases/download/v1.0/xkit.tar.gz"

wget -q --show-progress $URL -O /tmp/xkit.tar.gz

if [ $? -ne 0 ]; then
    echo -e "${RED}Download failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Extracting...${NC}"
cd /tmp
tar -xzf xkit.tar.gz

if [ ! -f /tmp/xkit ]; then
    echo -e "${RED}Extraction failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Installing to /usr/local/bin...${NC}"
sudo cp /tmp/xkit /usr/local/bin/
sudo chmod +x /usr/local/bin/xkit

rm -f /tmp/xkit.tar.gz /tmp/xkit

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}X-KIT installed! Run with: sudo xkit${NC}"
echo -e "${GREEN}========================================${NC}"

#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}     X-KIT Network Tool Installer       ${NC}"
echo -e "${GREEN}========================================${NC}"

echo -e "${GREEN}Downloading X-KIT...${NC}"

URL="https://github.com/nonseibello/X-KIT/releases/download/v1.2/xkit.tar.gz"

wget -q --show-progress $URL -O /tmp/xkit.tar.gz

if [ $? -ne 0 ]; then
    echo -e "${RED}Download failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Extracting...${NC}"
cd /tmp
tar -xzf xkit.tar.gz

echo -e "${GREEN}Installing X-KIT to /usr/local/bin...${NC}"
sudo cp /tmp/xkit /usr/local/bin/
sudo chmod +x /usr/local/bin/xkit

if [ -f /tmp/requirements.txt ]; then
    echo -e "${GREEN}Installing Python dependencies...${NC}"
    sudo pip install -r /tmp/requirements.txt 2>/dev/null || pip install --user -r /tmp/requirements.txt
fi

rm -f /tmp/xkit.tar.gz /tmp/xkit /tmp/requirements.txt

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}X-KIT installed! Run with: sudo xkit${NC}"
echo -e "${GREEN}========================================${NC}"

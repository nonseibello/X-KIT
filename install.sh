#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}     X-KIT Network Tool Installer       ${NC}"
echo -e "${GREEN}========================================${NC}"

echo -e "${GREEN}Downloading X-KIT...${NC}"
URL="https://github.com/nonseibello/X-KIT/releases/download/v1.3/xkit_v1.3.tar.gz"
wget -q --show-progress $URL -O /tmp/xkit_v1.3.tar.gz

if [ $? -ne 0 ]; then
    echo -e "${RED}Download failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Extracting...${NC}"
cd /tmp
tar -xzf xkit_v1.3.tar.gz

echo -e "${GREEN}Removing old version (if present)...${NC}"
sudo rm -f /usr/local/bin/xkit

echo -e "${GREEN}Installing X-KIT to /usr/local/bin...${NC}"
sudo cp /tmp/xkit /usr/local/bin/xkit
sudo chmod +x /usr/local/bin/xkit

rm -f /tmp/xkit_v1.3.tar.gz /tmp/xkit /tmp/requirements.txt /tmp/install_v1.3.sh

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}X-KIT installed! Run with: sudo xkit${NC}"
echo -e "${GREEN}========================================${NC}"
EOF

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}X-KIT installed! Run with: sudo xkit${NC}"
echo -e "${GREEN}========================================${NC}"

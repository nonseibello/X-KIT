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

wget -q --show-progress $URL -O /tmp/xkit_legacy.tar.gz

if [ $? -ne 0 ]; then
    echo -e "${RED}Download failed!${NC}"
    exit 1
fi

echo -e "${GREEN}Extracting...${NC}"
cd /tmp
tar -xzf xkit_legacy.tar.gz

# Cerca il file estratto (potrebbe chiamarsi xkit o xkit_old)
if [ -f /tmp/xkit ]; then
    EXECUTABLE="/tmp/xkit"
elif [ -f /tmp/xkit_old ]; then
    EXECUTABLE="/tmp/xkit_old"
else
    echo -e "${RED}Extraction failed! No executable found${NC}"
    ls -la /tmp/xkit* 2>/dev/null
    exit 1
fi

echo -e "${GREEN}Installing to /usr/local/bin...${NC}"
sudo cp $EXECUTABLE /usr/local/bin/xkit
sudo chmod +x /usr/local/bin/xkit

rm -f /tmp/xkit_legacy.tar.gz /tmp/xkit /tmp/xkit_old 2>/dev/null

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}X-KIT (legacy version) installed!${NC}"
echo -e "${GREEN}Run with: sudo xkit${NC}"
echo -e "${GREEN}========================================${NC}"
EOF

chmod +x install_legacy.sh

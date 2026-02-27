# Initial Container Setup

**Date:** 2026-02-28
**Container:** 104 (sat-ai-tutor)

## First Login
```bash
pct start 104
pct enter 104

apt update
apt upgrade -y

##Installed Packages
Package	Purpose
curl	Download files, test APIs
wget	Alternative downloader
git	Version control
nano	Text editor
htop	Process monitoring
net-tools	Network utilities (ifconfig)
python3-pip	Python package manager

python3 --version
# Python 3.12.3
curl --version  # Works
git --version   # Works

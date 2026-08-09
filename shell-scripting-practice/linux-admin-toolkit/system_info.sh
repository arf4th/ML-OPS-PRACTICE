#!/bin/bash

clear
echo "================================"
echo "   SYSTEM INFORMATION MODULE"
echo "================================"




echo "Current logged-in user: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current working directory $(pwd)"
echo "Shell being used is: $(echo $SHELL)"
echo "System uptime: $(uptime)"
echo "Memory Usage $(free -h)"
echo "Disk Usage $(du -h)"

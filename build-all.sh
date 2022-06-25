#!/bin/zsh

# Build backend
docker build -t boat-manager-backend ./backend

# Build frontend
cd frontend && npm run build
docker build -t boat-manager-frontend .

# Start up
docker-compose up
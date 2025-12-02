#!/usr/bin/env bash
set -euo pipefail

# Entrada para container: inicia Xvfb, x11vnc e noVNC (websockify) e depois executa a app

SCREEN=0
RESOLUTION="1024x768x24"

echo "Starting Xvfb on display ${DISPLAY} with screen ${SCREEN}..."
Xvfb ${DISPLAY} -screen ${SCREEN} ${RESOLUTION} &
XVFB_PID=$!

sleep 0.5

echo "Starting x11vnc on ${DISPLAY} (rfb port 5900)..."
# -noxdamage pode ajudar em alguns ambientes
x11vnc -display ${DISPLAY} -nopw -forever -shared -rfbport 5900 -noxdamage &
X11VNC_PID=$!

sleep 0.5

echo "Starting websockify (noVNC) serving /opt/noVNC on port 6080..."
# Usa websockify como módulo Python; --web serve os ficheiros noVNC
python -m websockify --web /opt/noVNC 6080 localhost:5900 &
WEBSOCKIFY_PID=$!

sleep 0.5

echo "Running application (main.py)..."
# Executa a aplicação em primeiro plano para que o container permaneça vivo
exec python main.py

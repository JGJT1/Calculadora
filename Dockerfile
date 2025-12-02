FROM python:3.11-slim

# Instala dependências do sistema: tkinter (python3-tk), Xvfb, x11vnc, git, wget
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3-tk \
       xvfb \
       x11vnc \
       git \
       wget \
       net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
# websockify será usado para expor VNC via noVNC
RUN pip install --no-cache-dir -r requirements.txt websockify

# baixar noVNC para fornecer UI via browser
RUN git clone --depth 1 https://github.com/novnc/noVNC.git /opt/noVNC || true

COPY . /app

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:0

# Porta para acessar via navegador (noVNC)
EXPOSE 6080

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

CMD ["/usr/local/bin/docker-entrypoint.sh"]

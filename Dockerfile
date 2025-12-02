FROM python:3.11-slim

# Instala dependências do sistema (tkinter para PySimpleGUI/Tk)
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-tk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]

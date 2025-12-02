# Calculadora (Tkinter)

Projeto base de uma calculadora desktop em Python usando Tkinter (biblioteca
inclusa no Python).

Requisitos
- Python 3.8+
- (Opcional) Docker se quiser rodar em container

Execução local

1. Crie um ambiente virtual (recomendado):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Um exemplo de build/run (Windows):

```powershell
docker build -t calculadora:local .
# Exemplo de execução (ajuste DISPLAY conforme seu X server):
docker run --rm -p 6080:6080 calculadora:local
```

Notas
- Tkinter já vem com o Python em Windows e facilita a execução local sem Docker.
- O `Dockerfile` provido serve como base; para produção de GUI em contêineres
  consulte documentação específica do seu X server e Docker Desktop.

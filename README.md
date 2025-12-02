# Calculadora (Tkinter)

Projeto base de uma calculadora desktop em Python usando Tkinter (biblioteca
inclusa no Python). Esta versão evita dependências de GUI de terceiros.

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

Execução via Docker (observações sobre Windows)

O `Dockerfile` instala `python3-tk` no container. No entanto, para exibir a
GUI você precisa de um X server no host. No Windows, instale e execute o VcXsrv
ou Xming e permita conexões. Use `host.docker.internal:0.0` como DISPLAY em
geral.

Um exemplo de build/run (Windows):

```powershell
docker build -t calculadora:local .
# Exemplo de execução (ajuste DISPLAY conforme seu X server):
docker run -e DISPLAY=host.docker.internal:0.0 --rm calculadora:local
```

Notas
- Tkinter já vem com o Python em Windows e facilita a execução local sem Docker.
- O `Dockerfile` provido serve como base; para produção de GUI em contêineres
  consulte documentação específica do seu X server e Docker Desktop.

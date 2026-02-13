# O Dockerfile é como uma receita de bolo para criar um computadorzinho mágico (Container).

# 1. ESCOLHER A BASE (O CHÃO)
# Estamos dizendo: "Começe com um sistema que já sabe falar Python".
# É como se estivéssemos comprando um caderno que já vem com linhas.
FROM python:3.9-slim

# 2. PREPARAR A MESA (O LOCAL DE TRABALHO)
# Estamos criando uma pasta chamada "app" dentro do container e entrando nela.
# É como se estivéssemos abrindo nosso caderno na primeira página.
WORKDIR /app

# 3. TRAZER AS FERRAMENTAS (COPIAR ARQUIVOS)
# Estamos copiando nosso arquivo "app.py" do nosso computador para dentro do container.
# É como se estivéssemos colando uma figurinha no caderno.
COPY app.py .

# 4. O COMANDO FINAL (O BOTÃO DE "LIGAR")
# Quando o container ligar, ele vai executar este comando.
# É como dizer: "Computador, leia o arquivo app.py com o Python!".
CMD ["python", "app.py"]

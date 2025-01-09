FROM python:3.11-slim

# Nastavení pracovního adresáře v kontejneru
WORKDIR /app

# Zkopírování souboru requirements.txt a jeho instalace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Nainstalování závislostí pro Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-dev \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libexpat1 \
    libxcb1 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    wget \
    curl \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Instalace Playwright a jeho prohlížečů
RUN pip install playwright && playwright install-deps && playwright install

# Zkopírování celé aplikace do kontejneru
COPY . .

# Nastavení proměnného prostředí pro Playwright (instalace prohlížečů)
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0

# Exponování portu, na kterém běží aplikace
EXPOSE 8000

# Příkaz pro spuštění aplikace
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

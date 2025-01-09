FROM python:3.11-slim

# Nastavení pracovního adresáře v kontejneru
WORKDIR /app

# Zkopírování souboru requirements.txt a jeho instalace
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Zkopírování celé aplikace do kontejneru
COPY . .

# Nastavení proměnného prostředí pro Playwright (instalace prohlížečů)
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0

# Instalace prohlížečů pro Playwright
RUN playwright install

# Exponování portu, na kterém běží aplikace
EXPOSE 8000

# Příkaz pro spuštění aplikace
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

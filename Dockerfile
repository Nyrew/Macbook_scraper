# Použijte Playwright image s verzí 1.40.0
FROM mcr.microsoft.com/playwright:v1.40.0-jammy

# Nastavte pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujte requirements.txt do pracovního adresáře
COPY requirements.txt .

# Nainstalujte závislosti
RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-cache-dir -r requirements.txt

# Zkopírujte zbytek kódu aplikace do pracovního adresáře
COPY . .

# Otevřete port, na kterém bude aplikace běžet
EXPOSE 8000

# Příkaz pro spuštění aplikace
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

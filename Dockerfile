# Použijte oficiální Python image jako základ
FROM python:3.9-slim

# Nainstalujte Playwright a jeho závislosti
RUN pip install playwright
RUN playwright install

# Nastavte pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujte requirements.txt do pracovního adresáře
COPY requirements.txt .

# Nainstalujte závislosti
RUN pip install --no-cache-dir -r requirements.txt

# Zkopírujte zbytek kódu aplikace do pracovního adresáře
COPY . .

# Otevřete port, na kterém bude aplikace běžet
EXPOSE 8000

# Příkaz pro spuštění aplikace
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
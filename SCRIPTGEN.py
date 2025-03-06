import os
import time
from datetime import datetime
from selenium import webdriver
import img2pdf

# 🔗 URL Power BI 
POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiYzRkODM3NWEtNWM1OS00YTRkLWExODYtY2UzYjYyZTE1NTIxIiwidCI6Ijg2ZjA0NzBmLTI1MjgtNGViYi1iNjdiLTM2NDM2YzNhMzBmOCJ9&pageName=ReportSectione9e5c0104dd8e1d16397"

# 📂 Carpeta donde se guardarán los reportes
output_folder = "Reportes_PowerBI"
os.makedirs(output_folder, exist_ok=True)

# ⏳ Obtener fecha y hora actual para nombrar archivos
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_file = os.path.join(output_folder, f"Reporte_PowerBI_{timestamp}.png")
pdf_file = os.path.join(output_folder, f"Reporte_PowerBI_{timestamp}.pdf")

# 🌐 Configurar Selenium (modo headless para no abrir navegador)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=3000,2000")
options.add_argument("--disable-gpu")

# 🚀 Inicializar WebDriver de Chrome
driver = webdriver.Chrome(options=options)
driver.get(POWER_BI_URL)

# 🔍 Ajustar zoom (opcional para mejorar calidad)
driver.execute_script("document.body.style.zoom='250%'")

# ⏳ Esperar para cargar Power BI
time.sleep(15)

# 📸 Capturar pantalla en HD
driver.save_screenshot(screenshot_file)

# ❌ Cerrar el navegador
driver.quit()

# 🖼️ Convertir la imagen en PDF
with open(pdf_file, "wb") as f:
    f.write(img2pdf.convert(screenshot_file))

# 🗑️ Eliminar imagen temporal
os.remove(screenshot_file)

print(f"✅ PDF generado en: {pdf_file}")







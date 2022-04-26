import json
# pip install selenium
from selenium import webdriver
# pip install beautifulsoup4
from bs4 import BeautifulSoup

url = 'https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html'
# https://chromedriver.chromium.org/home
driver = webdriver.Chrome(
    executable_path=r'C:\Utilities\chromedriver.exe')
driver.implicitly_wait(30)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', id='tabledatasii')
# print(table)

headers = [heading.text.replace("No.", "id")
           for heading in table.find_all('th')]
# print(headers)

table_rows = [row for row in table.find_all('tr')]
# print(table_rows)

results = [{headers[index]: cell.text for index,
            cell in enumerate(row.find_all("td"))} for row in table_rows]

# Nueva lista sin objetos vacios
lista_final = [elemento for elemento in results if elemento]
# print(lista_final)

# la Lista de diccionarios de Python en una cadena JSON
data = json.dumps(lista_final)
data_two = json.loads(data)
# print(data_two)

# se crea un archivo data.json
# abrir data.jason en modo de escritura "w"
jsonFile = open("data.json", "w")
jsonFile.write(data)
jsonFile.close()

# Comprobar
for i in data_two:
    if "id" in i:
        if i["id"] == "1":
            print(i)

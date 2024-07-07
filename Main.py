import requests
from bs4 import BeautifulSoup

def printData(mainArray):
    if not mainArray[0] or not mainArray[1]:
        print("No data to print.")
        return

    max_length_name = max(len(item.text.strip()) for item in mainArray[0])
    max_length_number = max(len(item.text.strip()) for item in mainArray[1])

    # Print header
    print(f"{'Name':<{max_length_name}} {'Number':<{max_length_number}}")
    print('-' * (max_length_name + max_length_number + 1))

    # Print rows
    for i in range(min(9, len(mainArray[0]))):
        name = mainArray[0][i].text.strip()
        number = mainArray[1][i].text.strip()
        print(f"{name:<{max_length_name}} {number:<{max_length_number}}")

def getData(stock="NIFTY"):
    url = f'https://www.screener.in/company/{stock}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    NameS = "name"
    NumberS = "number"
    nameArray = soup.find_all(class_=NameS)
    numberArray = soup.find_all(class_=NumberS)
    mainArray = [nameArray, numberArray]
    return mainArray

print("Stock Data")
printData(getData("adanient"))
print("Nifty Data")
printData(getData())

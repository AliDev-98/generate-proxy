import random

def generate_proxy():
    # generate proxy
    proxy = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}:{random.randint(1000,9999)}"
    return proxy

def save_proxies(num_proxies):
    # Please open the file for writing
    with open("proxies.txt", "w") as file:
        # Generate num_proxies proxies and save them in a file
        for i in range(num_proxies):
            proxy = generate_proxy()
            file.write(proxy + "\n")

# Generate 10 proxies and save them in a file named proxies.txt
save_proxies(1000000)

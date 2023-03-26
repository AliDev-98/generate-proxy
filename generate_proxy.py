import random

def generate_proxy():
    # توليد البروكسي
    proxy = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}:{random.randint(1000,9999)}"
    return proxy

def save_proxies(num_proxies):
    # افتح الملف للكتابة
    with open("proxies.txt", "w") as file:
        # توليد عدد num_proxies من البروكسيات وحفظها في الملف
        for i in range(num_proxies):
            proxy = generate_proxy()
            file.write(proxy + "\n")

# توليد 10 بروكسيات وحفظها في ملف باسم proxies.txt
save_proxies(1000000)

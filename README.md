# TOTP Authenticator CLI Tool

A command-line tool to generate TOTP (Time-based One-Time Password) codes using HMAC-SHA512. 
Built for developers and curious minds who want a simple, standards-compliant CLI for generating 2FA codes.

## Features

- Generates TOTP codes using [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)
- Supports secret from base32 or your email (hashed into a secret)
- Shows remaining time for the current code
- Input validation and retry loop
- CLI experience – no GUI, no bloat

## Installation

```bash
git clone https://github.com/asrithcheepurupalli/totp-cli.git
cd totp-cli
pip install -r requirements.txt
```

## Usage

```bash
python totp.py
```

You’ll be prompted to choose between:

- `e` — Enter your email (internally hashed)
- `b` — Enter a Base32 secret directly

Example run:

```
Use email or base32 secret? (e/b): e
Enter your email: user@example.com

TOTP Code: 123456
Time remaining: 27 seconds
```

If invalid input is given, the script will ask to restart.

## Tech Stack

- Python 3
- `pyotp` for TOTP generation
- `hashlib` for email hashing
- `time` and `datetime` for syncing

## Author

**Lok Sai Asrith Cheepurupalli**  
GitHub: [asrithcheepurupalli](https://github.com/asrithcheepurupalli)  
Portfolio: [asrithcheepurupalli.codes](https://asrithcheepurupalli.codes)

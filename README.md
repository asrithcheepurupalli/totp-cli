# TOTP CLI

A simple command-line tool to generate Time-Based One-Time Passwords (TOTP) using HMAC-SHA512. It follows the RFC 6238 standard and only uses Python’s standard library.

This tool is useful for learning how 2FA systems work behind the scenes. It can generate secure codes either using an email as a base secret or a Base32-encoded key (like Google Authenticator and similar apps use).

## Features

- Generates TOTP codes that refresh every 30 seconds
- Uses HMAC-SHA512 (more secure than default SHA-1)
- Validates email or secret input
- Optional retry with clean restarts
- No external dependencies required

## How to Run

```bash
python3 main.py

# PySentinel

A Python-based web security scanner designed to identify common web security misconfigurations and vulnerabilities.

## Overview

PySentinel is a lightweight security testing tool built with Python. It performs automated checks against web applications and presents security findings in a simple, readable format.

The project is being developed as a practical cybersecurity portfolio project, with a focus on web application security and penetration testing.

## Current Features

* HTTP response analysis
* HTTP status code detection
* Server information detection
* Content-Type detection
* Response size analysis
* Security header detection

### Security Headers Checked

* Content-Security-Policy
* Strict-Transport-Security
* X-Frame-Options
* X-Content-Type-Options
* Referrer-Policy

## Installation

Clone the repository:

```bash
git clone git@github.com:lekssayshamza/PySentinel.git
cd PySentinel
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install requests
```

## Usage

Run PySentinel against a target:

```bash
python pysentinel/scanner.py https://example.com
```

Example output:

```text
Target: https://example.com
Status Code: 200
Server: cloudflare
Content-Type: text/html; charset=utf-8
Response Size: 577 bytes

Security Headers:
[-] Content-Security-Policy: Missing
[-] Strict-Transport-Security: Missing
[-] X-Frame-Options: Missing
[-] X-Content-Type-Options: Missing
[-] Referrer-Policy: Missing
```

## Project Structure

```text
PySentinel/
├── pysentinel/
│   ├── __init__.py
│   └── scanner.py
├── .gitignore
└── README.md
```

## Roadmap

* [ ] Improved security header analysis
* [ ] Cookie security analysis
* [ ] Technology detection
* [ ] Directory and file discovery
* [ ] XSS detection
* [ ] SQL injection detection
* [ ] Open redirect detection
* [ ] HTML security reports
* [ ] Command-line interface
* [ ] Unit tests
* [ ] Configuration support

## Disclaimer

PySentinel is intended for authorized security testing and educational purposes only.

Only scan systems and applications that you own or have explicit permission to test. The author is not responsible for misuse of this tool.

## Author

**Hamza Lekssays**

Cybersecurity Engineering Student

GitHub: [@lekssayshamza](https://github.com/lekssayshamza)

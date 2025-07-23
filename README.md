# Reverse Shell Simulation and Detection – Internship Project

## 📌 Project Overview

This project demonstrates the simulation of a basic **reverse shell attack** and its detection using **Wireshark**, designed for educational and defensive security learning purposes as part of a SOC Analyst internship.

It includes:
- A custom reverse shell written in Python
- Compilation of the reverse shell into a Windows executable
- Execution simulation from a Windows machine
- Netcat listener on Kali Linux for receiving shell
- Network capture and detection via Wireshark
- Final report documenting the attack and detection steps

> ⚠️ This project is conducted in a **controlled lab environment** for educational purposes only. Do not deploy or use this outside of approved environments.

---
## 📁 Directory Structure
rev_shell_simulation/
├── update/ # Payload code and executable
├── listener/ # Netcat command logs
├── wireshark_analysis/ # PCAP files and notes
├── report/ # Final PDF report
├── README.md # Project overview
├── LICENSE # (MIT or your choice)
└── .gitignore # Files to exclude from Git


---

## 🛠️ Tools Used

- Python 3.11
- PyInstaller (for .exe generation)
- Windows 11 (attacker simulation)
- Kali Linux (listener / Wireshark)
- Netcat
- Wireshark

---

## Prerequisites

- **Python 3.x** — install from [python.org](https://www.python.org/downloads/) or your OS package manager.
- **Wireshark** — install via your OS package manager or from [wireshark.org](https://www.wireshark.org/download.html).
- Install Python dependencies:
bash - 
pip install -r requirements.txt

---

## 🎯 Attack Simulation

- A stealthy Python reverse shell connects back to the Kali machine over a specified port.
- The Python script is compiled into a `.exe` using PyInstaller with the `--noconsole` flag for stealth.
- A Netcat listener is set up on the attacker's machine to receive the shell.
- Wireshark is used to monitor and analyze the reverse shell traffic.

---

## 🔎 Detection Strategy

- **Wireshark** filters like `ip.dst == YOUR_VICTIM_IP` were used to identify suspicious inbound connections.
- Manual analysis of payload behavior and commands executed.
- Review of PCAP file and extracted session data.

---

## 📄 Report

A detailed PDF report is included in the `report/` folder with:
- Attack setup
- Shell execution
- Network behavior
- Detection insights

---

## 🚨 Disclaimer

This project is strictly for **educational and research purposes** in a lab setup. Unauthorized or malicious use of reverse shells is illegal and unethical.

---

## 📬 Contact

For questions or clarifications related to this project, please reach out via GitHub Issues or connect with the author.


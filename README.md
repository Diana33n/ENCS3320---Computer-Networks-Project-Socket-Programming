
# ENCS3320 - Computer Networks Project: Socket Programming

This repository contains the implementation and documentation for **Socket Programming** completed as part of **ENCS3320 – Computer Networks**. The project demonstrates client-server communication using TCP and UDP protocols and explores basic network commands with Wireshark analysis.

## Overview

The project is divided into three parts:

1. **Commands and Wireshark**

   * Learn and apply networking commands: `ping`, `tracert`, `nslookup`, `telnet`.
   * Use Wireshark to capture and analyze DNS messages.

2. **Socket Programming**

   * Develop and test TCP and UDP client-server applications.
   * Understand connection-oriented (TCP) and connectionless (UDP) communication.

3. **Web Server Implementation**

   * Build a simple HTTP web server using socket programming in Python.
   * Serve static HTML pages and handle HTTP requests.

This project highlights the practical differences between TCP and UDP while implementing real-world network interactions.


## Features

* TCP client replaces vowels in a string and returns the result to the user.
* UDP server manages messages from multiple clients, storing and displaying the latest communication.
* Basic web server serves localized HTML content in English and Arabic.
* Wireshark captures DNS requests for analysis.

---

## How to Run

### Prerequisites

* Python 3.x installed
* Enable Telnet on Windows (for part 1 testing)
* Wireshark (for packet capturing)

### Running TCP Client and Server

1. Start the TCP server (code not included here but referenced in the report).
2. Run the TCP client:

```bash
python TCP\ client.txt
```

3. Enter a message when prompted. The server will return the message with vowels replaced by `#`.

### Running UDP Server

1. Run the UDP server:

```bash
python UDP\ Server.txt
```

2. Clients can connect to the server, send messages, and receive responses.

---

## Team Members

| Name          | Student ID |
| ------------- | ---------- |
| Diana Naseer  | 1210363    |
| Hala Mohammed | 1210312    |
| Rua Srour     | 1221727    |

Instructor: Dr. Ibrahim Nemer
Date: 15 August 2024

---

## References

* [Wireshark](https://www.wireshark.org/)
* [Python Socket Programming](https://docs.python.org/3/library/socket.html)
* [BGPView.io](https://bgpview.io)
* [Socket Programming Video Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)



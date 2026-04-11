# 🧅 ONION — AI Smart Security & Virtual Assistant System

ONION is an AI-powered smart home security and virtual assistant system built using **Python**, **Arduino**, and **Computer Vision**.

It integrates **voice commands**, **face recognition**, **gas detection**, **motion sensing**, and **hardware automation** into a single intelligent system capable of interacting with both software and physical hardware.

Originally developed in **2022**, this project demonstrates early integration of **AI + IoT + Embedded Systems**.

---

# 📌 Project Overview

ONION combines:

• Artificial Intelligence  
• Computer Vision  
• Voice Recognition  
• Embedded Systems  
• Smart Security Automation  

Python handles:

• Voice recognition  
• Face recognition  
• AI responses  
• Internet features  

Arduino handles:

• Sensors  
• Door locking  
• Distance measurement  
• Motion detection  
• Gas detection  

Both communicate using:

**Serial Communication (9600 baud)**

---

# 🧠 System Modes

## 🟢 Normal Mode — Assistant Mode

Runs:

main.py

Functions:

• Face Recognition Login  
• Voice Assistant  
• Door Lock Control  
• Distance Measurement  
• Web Automation  
• Email Sending  
• WhatsApp Messaging  
• Weather & News  
• Brightness Control  

Command:

security protocol

Switches system to:

**Security Mode**

---

## 🔴 Security Mode

Runs:

Security.py

Monitors:

• PIR Motion Sensor  
• Gas Sensor  

Triggers alerts when:

• Motion detected  
• Gas detected  

Exit command:

security protocol

Returns to:

main.py

---

## 🟡 Sleep Mode

Runs:

Hot Words.py

Waits for:

wake up  
onion  
hello  

Then launches:

main.py

---

# ⚙️ Features

✔ Face Recognition Login  
✔ Voice Controlled Assistant  
✔ Smart Door Lock  
✔ Motion Detection Alerts  
✔ Gas Leak Detection  
✔ Ultrasonic Distance Measurement  
✔ OLED Display Output  
✔ Email Sending  
✔ WhatsApp Messaging  
✔ Web Automation  
✔ Weather & News  
✔ Screen Brightness Control  
✔ Serial Hardware Communication  

---

# 🧰 Hardware Components Used

| Component | Quantity |
|----------|----------|
| Arduino Uno / Nano | 1 |
| PIR Motion Sensor | 1 |
| MQ Gas Sensor | 1 |
| Ultrasonic Sensor HC-SR04 | 1 |
| Servo Motor | 1 |
| OLED Display SSD1306 (I2C) | 1 |
| USB Webcam | 1 |
| Microphone | 1 |
| Speaker | 1 |
| Breadboard | 1 |
| Jumper Wires | Multiple |

---

# 🔌 COMPLETE WIRING INSTRUCTIONS

Follow these connections exactly.

---

# 🔧 Servo Motor (Door Lock)

| Servo Wire | Connect To |
|-------------|-------------|
| Red (VCC) | Arduino 5V |
| Brown/Black (GND) | Arduino GND |
| Yellow/Orange (Signal) | Arduino Pin 2 |

---

# 🔧 PIR Motion Sensor

| PIR Pin | Connect To |
|----------|-------------|
| VCC | Arduino 5V |
| GND | Arduino GND |
| OUT | Arduino Pin 9 |

---

# 🔧 MQ Gas Sensor

| MQ Pin | Connect To |
|--------|-------------|
| VCC | Arduino 5V |
| GND | Arduino GND |
| AOUT | Arduino A3 |

Digital output not used.

---

# 🔧 Ultrasonic Sensor (HC-SR04)

| HC-SR04 Pin | Connect To |
|--------------|-------------|
| VCC | Arduino 5V |
| GND | Arduino GND |
| TRIG | Arduino Pin 5 |
| ECHO | Arduino Pin 6 |

---

# 🔧 OLED Display (SSD1306 I2C)

| OLED Pin | Connect To |
|----------|-------------|
| VCC | Arduino 5V |
| GND | Arduino GND |
| SDA | Arduino A4 |
| SCL | Arduino A5 |

I2C Address:

0x3C

---

# 🔧 USB Connection

Connect:

Arduino → PC via USB cable

Used for:

Serial Communication

Baud Rate:

9600

---

# 💻 Software Requirements

Install:

Python 3.8+

Arduino IDE

---

# 📦 Installation & Setup

## 🐍 Install Python Libraries

Run the following commands in terminal:

```bash
pip install speechrecognition
pip install pyttsx3
pip install face_recognition
pip install pywhatkit
pip install wikipedia
pip install pyjokes
pip install screen-brightness-control
pip install gnews
pip install ip2geotools
pip install opencv-python
pip install numpy
pip install pyserial
pip install GoogleNews

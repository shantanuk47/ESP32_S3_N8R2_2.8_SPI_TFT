# ESP32-S3 N8R2 2.8" SPI TFT Display Stack (ILI9341)

Professional embedded firmware project for validating and developing a scalable display stack using the **ILI9341 SPI TFT controller** and **XPT2046 resistive touch controller** on the **ESP32-S3 N8R2 (HW-678)** platform.

This repository follows strict embedded architecture principles, modular firmware design, Git-controlled firmware versioning, and disciplined coding standards inspired by MISRA-oriented practices.

---

# 1. Project Objective

This project serves two primary goals.

### Hardware Validation

The initial phase focuses on verifying hardware compatibility between the ESP32-S3 platform and the 2.8" SPI TFT display module.

Validation includes:

* SPI communication verification
* Display initialization sequence testing
* Basic graphics rendering
* Touch controller communication validation

### Firmware Foundation

Once hardware compatibility is confirmed, the repository evolves into a structured embedded firmware framework capable of supporting additional peripherals and system services.

Key engineering goals:

* Reusable display driver architecture
* Clean driver abstraction layers
* Strict firmware structure discipline
* Maintainable and scalable embedded codebase

This repository prioritizes **long-term firmware stability and maintainability** over quick prototyping.

---

# 2. Current Status

**Firmware Version:** v0.1.0 (Initial Setup)
**Current Phase:** Phase 1 – Hardware Validation

Current focus:

* SPI bus initialization
* Display controller communication
* Basic display test patterns
* Hardware compatibility verification

Touch validation will follow once display communication is confirmed stable.

---

# 3. Hardware Information

Board        : ESP32-S3 N8R2 (HW-678)
Flash        : 8MB
PSRAM        : 2MB
MCU          : ESP32-S3
USB          : Native USB

Display Controller : ILI9341
Touch Controller   : XPT2046
Display Size       : 2.8 inch
Resolution         : 240 x 320
Interface          : SPI

---

# 4. Pin Configuration

## SPI Bus (Shared)

SCLK  → GPIO12
MOSI  → GPIO11
MISO  → GPIO13

Both the display controller and touch controller share the same SPI bus.

---

## Display (ILI9341)

CS     → GPIO10
DC     → GPIO8
RESET  → GPIO9
LED    → 3.3V

Backlight is currently always enabled.
Future revisions may move the backlight to a PWM-controlled GPIO.

---

## Touch Controller (XPT2046)

T_CS   → GPIO7
T_IRQ  → GPIO6

The touch controller communicates using the same SPI bus as the display.

---

# 5. Development Environment

Framework    : ESP-IDF (FreeRTOS-based)
Build System : PlatformIO
IDE          : Visual Studio Code
Environment  : esp32s3_hw678

Example configuration:

```
[env:esp32s3_hw678]
platform = espressif32
board = rymcu-esp32-s3-devkitc-1
framework = espidf
monitor_speed = 115200
```

PlatformIO manages the ESP-IDF toolchain automatically.

---

# 6. Firmware Versioning

Firmware versioning is automatically generated using **Git tags** during the build process.

A Python script extracts version information from the Git repository and generates a firmware version header file.

Version information is derived using:

```
git describe --tags --always --dirty
```

Example:

```
v0.1.0-3-g91acbd2
```

Meaning:

* **v0.1.0** → latest Git tag
* **3** → commits ahead of tag
* **g91acbd2** → commit hash
* **-dirty** → uncommitted changes present

---

## Automatic Version Header Generation

A Python script generates firmware version metadata during the build process.

Script location:

```
scripts/generate_version.py
```

Generated file:

```
include/version.h
```

Example generated content:

```
#define FW_VERSION "v0.1.0-3-g91acbd2"
#define FW_BUILD_DATE "2026-03-15"
#define FW_BUILD_TIME "14:21:08"
```

The generated header file is **not committed to Git**.

This ensures:

* build traceability
* reproducible firmware builds
* accurate version identification during runtime

---

# 7. Project Architecture

The firmware follows a **strict layered architecture inspired by AUTOSAR design principles** while remaining lightweight and practical for embedded systems.

Architecture layers:

Application Layer
↓
Service Layer
↓
Hardware Abstraction Layer (HAL)
↓
Driver Layer
↓
ESP-IDF Drivers
↓
Hardware

Application logic must **never directly access hardware drivers**.

All hardware interaction must pass through the abstraction layers.

---

### Example Runtime Flow

```
main.c
 └── system_init()
     ├── spi_bus_init()
     ├── display_init()
     ├── touch_init()
     └── application_start()
```

This ensures deterministic initialization and clear system flow.

---

# 8. Repository Structure

```
ESP32_S3_N8R2_2.8_SPI_TFT/
│
├── src/
│   └── main.c
│
├── include/
│   ├── config.h
│   ├── version.h (auto-generated)
│   └── system_init.h
│
├── drivers/
│   ├── spi_bus/
│   ├── ili9341/
│   └── xpt2046/
│
├── services/
│   ├── display_service/
│   └── touch_service/
│
├── docs/
│
├── test/
│
├── scripts/
│   └── generate_version.py
│
├── platformio.ini
├── .gitignore
└── README.md
```

The structure is designed to support future expansion and additional hardware modules.

---

# 9. Coding Standards

This project enforces disciplined embedded firmware practices.

Key rules:

* MISRA-inspired coding style
* Strict compiler warnings enabled
* No uncontrolled global variables
* No magic numbers
* Deterministic module behavior
* Mandatory file documentation headers

---

## 9.1 Comment Rules

Allowed:

```
/* Multi-line comment */
```

Not allowed:

```
// comment
```

Single-line `//` comments are reserved only for temporarily disabling code.

---

## 9.2 Mandatory File Header

Every source and header file must begin with:

```
/============================================================
Project : ESP32-S3 N8R2 2.8" SPI TFT Display Stack
Author  : Shantanu Kumar
GitHub  : https://github.com/shantanuk47

Date :
File :
Purpose :
============================================================/
```

Files without this header are considered non-compliant.

---

# 10. Build & Flash Process

All operations can be performed using PlatformIO GUI or CLI.

Clean project:

```
pio run -t clean
```

Build firmware:

```
pio run
```

Upload firmware:

```
pio run -t upload
```

Serial monitor:

```
pio device monitor
```

Default baud rate:

```
115200
```

---

# 11. Git Discipline

The following items are not tracked in the repository:

* `.pio/`
* build artifacts
* compiled binaries (.bin, .elf, .map)
* IDE configuration files
* `include/version.h` (auto-generated)

Only stable source code and configuration files are version controlled.

Release builds must always be tagged before deployment.

---

# 12. Engineering Philosophy

Embedded firmware must be:

Predictable
Testable
Maintainable
Traceable
Hardware-abstracted

This project prioritizes **long-term maintainability and architectural clarity** over quick experimental development.

---

# 13. Future Expansion

The firmware architecture is designed to support additional hardware modules including:

* RTC modules
* CAN communication interfaces
* Joystick controllers
* Rotary encoders
* Advanced graphical user interfaces

The goal is to evolve this repository into a **scalable embedded system platform**.

---

# 14. License

License to be defined.

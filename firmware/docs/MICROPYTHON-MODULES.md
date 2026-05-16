# MicroPython Module Surface

The Replay 2026 Badge embeds MicroPython v1.27 in the Arduino firmware. The
default public firmware exposes the practical app-authoring modules we have
validated on badge hardware.

## Enabled By Default

| Module | Notes |
|--------|-------|
| `badge` | Badge-specific OLED, LED matrix, buttons, joystick, IMU, haptics, IR, contact card, boops, HTTP, and app helpers. Auto-imported at boot. |
| `sys` | `sys.path`, `sys.exit()`, REPL prompt strings, platform metadata. |
| `os` | VFS-backed filesystem APIs on the badge FatFS partition. |
| `time` | Sleep, ticks, epoch helpers, and local/gmtime conversions. |
| `math`, `cmath`, `random` | Game and animation math. |
| `json`, `struct`, `array`, `binascii`, `collections`, `io` | Data handling and small persistence helpers. |
| `errno`, `gc`, `micropython`, `uctypes` | Runtime inspection, memory management, and low-level data layouts. |
| `select` | Polling support for stream-style APIs. |
| `network` | `network.WLAN` for WiFi status and 2.4 GHz access-point scans. |
| `socket` | ESP32/lwIP socket support for TCP/UDP clients and simple servers. |
| `_espnow` | Low-level ESP-NOW API from the ESP32 MicroPython port. The higher-level `espnow.py` wrapper is still pending filesystem packaging. |
| `machine` | ESP32 pin, ADC, PWM, Timer, RTC, UART, SPI, SoftI2C, WDT, and `time_pulse_us()` APIs. Hardware I2C stays off because it conflicts with Arduino's I2C driver; use `SoftI2C`. |

## Gated For Future Validation

The source tree carries hooks for a larger ESP32 MicroPython surface, but the
default release does not promise these modules yet:

| Feature | Current status |
|---------|----------------|
| `ssl`/`tls`, `websocket`, `webrepl` | Build-gated while TLS/WebREPL behavior is validated with the badge WiFi service. Upstream v1.27 uses `extmod/modtls_mbedtls.c`. |
| `espnow` | The public Python wrapper remains pending; `_espnow` is enabled for smoke testing. |
| `bluetooth` | Build-gated; needs a full NimBLE validation pass. |
| `_thread` | Build-gated; the event-poll and GIL path needs more soak testing in the embedded runtime. |

Use `firmware/initial_filesystem/micropython_tests/testImports.py` and
`firmware/initial_filesystem/micropython_tests/test_timers.py` as badge-side smoke tests
when changing the module surface.

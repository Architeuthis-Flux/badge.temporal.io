# Diagnostics Examples

These scripts are intentionally grouped under `/apps/diagnostics` so the main
Apps menu stays focused while developers still have readable examples to learn
from in JumperIDE or over USB serial.

They are not packaged as one launchable folder app because each file is meant
to demonstrate a specific subsystem.

| File | Demonstrates |
|------|-------------|
| `api_test.py` | Interactive badge API test menu |
| `input_test.py` | Buttons, joystick, and IMU input inspection |
| `ir_loopback_test.py` | IR send/receive loopback checks |
| `ir_poll_test.py` | IR polling cadence and receive constraints |
| `http_test.py` | MicroPython HTTP GET smoke test |
| `gc_bench.py` | GC pause measurement benchmark |
| `viperide_reinit.py` | Serial/editor reconnection helper |

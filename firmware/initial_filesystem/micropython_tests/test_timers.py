import time
from machine import Timer, WDT, Pin, time_pulse_us

print("=== Timer, WDT, and pulse test ===")
oled_clear()
oled_set_cursor(0, 0)
oled_print("Timer/WDT Test")
oled_show()

tick_count = 0

def on_tick(t):
    global tick_count
    tick_count += 1

tim = Timer(0)
tim.init(period=50, mode=Timer.PERIODIC, callback=on_tick)
time.sleep_ms(300)
tim.deinit()

periodic_ok = tick_count >= 4
print("periodic:", tick_count, "OK" if periodic_ok else "FAIL")

one_shot_fired = False

def on_oneshot(t):
    global one_shot_fired
    one_shot_fired = True

tim2 = Timer(1)
tim2.init(period=100, mode=Timer.ONE_SHOT, callback=on_oneshot)
time.sleep_ms(200)
tim2.deinit()

print("one-shot:", "OK" if one_shot_fired else "FAIL")

wdt = WDT(timeout=8000)
wdt.feed()
print("WDT: OK")

try:
    p = Pin(44, Pin.IN)
    pulse = time_pulse_us(p, 1, 1000)
    print("time_pulse_us:", pulse)
    pulse_ok = True
except Exception as exc:
    print("time_pulse_us: FAIL", exc)
    pulse_ok = False

oled_clear()
oled_set_cursor(0, 0)
oled_print("Timer/WDT Test")
oled_set_cursor(0, 14)
oled_print("periodic: " + ("OK" if periodic_ok else "FAIL"))
oled_set_cursor(0, 28)
oled_print("one-shot: " + ("OK" if one_shot_fired else "FAIL"))
oled_set_cursor(0, 42)
oled_print("WDT/pulse: " + ("OK" if pulse_ok else "FAIL"))
oled_show()

time.sleep_ms(3000)
exit()

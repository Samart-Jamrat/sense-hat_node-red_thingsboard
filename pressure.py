from sense_emu import SenseHat
import time

sense = SenseHat()


yellow = (255, 255, 0)

blue = (0, 0, 255)

# ช่วงความดันอากาศที่ใช้แสดงผล
MIN_PRESSURE = 950
MAX_PRESSURE = 1050

while True:
    pressure = sense.pressure  # อ่านค่าความดันอากาศ (hPa)

    # แปลง pressure ให้อยู่ในช่วง 0-64 ช่อง
    level = int((pressure - MIN_PRESSURE) / (MAX_PRESSURE - MIN_PRESSURE) * 64)

    # กันค่าเกินช่วง
    level = max(0, min(64, level))

    pixels = [yellow if i < level else blue for i in range(64)]
    sense.set_pixels(pixels)

    print(f"Pressure: {pressure:.2f} hPa, Level: {level}/64")
    time.sleep(1)

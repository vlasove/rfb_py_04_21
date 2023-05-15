# Решение задачи K

MIN_PULSE = 1000
MAX_PULSE = -1

LOW_PULSE = 100
HIGH_PULSE = 140

count = 0

while True:
    pulse = float(input())
    if pulse < 0:
        break
    
    if pulse >= LOW_PULSE and pulse <= HIGH_PULSE:
        count += 1

        if pulse > MAX_PULSE:
            MAX_PULSE = pulse

        if pulse < MIN_PULSE:
            MIN_PULSE = pulse

print(count) # Вывод количества отобранных космонавтов
print(MIN_PULSE, MAX_PULSE)
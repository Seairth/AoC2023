sum_cal = 0

with open('input.txt', 'r') as f:
    for line in f:
        digits = [c for c in line if c in '0123456789']
        cal = int(digits[0] + digits[-1])
        sum_cal += cal

print(sum_cal)
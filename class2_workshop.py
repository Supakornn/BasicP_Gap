distance = int(input("Enter distance: "))
if distance > 500: # 501 +
    print("45 B")
elif distance > 300: # 301 - 500
    print("35 B")
elif distance > 100: # 101 - 300
    print("25 B")
elif distance > 50: # 51 - 100
    print("15 B")
elif distance > 5: # 5 - 50
    print("10 B")
else: # < 5
    print("Not send")
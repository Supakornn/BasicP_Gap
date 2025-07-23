slime = 40
sword = 10
hammer = 5
hand = 1

while True:
    choice = int(input("1. ต่อสู้มอน 2. ออก เลือกอะไร?: "))

    if choice == 1:
        slime = 40 
        print("เลือดมอน", slime)
        print("อาวุธที่เรามี 1. ดาบ(10) 2. ค้อน(5) 3. หมัด(1)")
        num = int(input("จะตีกี่รอบ: "))
        for i in range(1, num + 1):
            print(f"\n-- รอบที่ {i} --")
            eq = int(input("1. ดาบ(10) 2. ค้อน(5) 3. หมัด(1) เลือกอะไร?: "))
            
            if eq == 1:
                slime -= sword
                print("คุณใช้ดาบ ฟันใส่มอนสเตอร์!")
            elif eq == 2:
                slime -= hammer
                print("คุณใช้ค้อน ทุบมอนสเตอร์!")
            elif eq == 3:
                slime -= hand
                print("คุณชกด้วยหมัด!")

            if slime == 0:
                print("มอนสเตอร์ตายเรียบร้อย!")
                break
            elif slime < 0:
                print("แรงเกินไป! มอนสเตอร์ไม่ตาย แต่เลือดบวกกลับมา!")
                slime = 20 
                print("เลือดมอนกลับมา:", slime)
            else:
                print("เลือดมอนเหลือ:", slime)
        
        if slime > 0:
            print("\nมอนสเตอร์ยังไม่ตาย คุณตายเอง ฮ่าๆ!")
        print("-" * 30)

    elif choice == 2:
        print("ลาก่อนนักรบ")
        break
    else:
        print("กรุณาเลือก 1 หรือ 2 เท่านั้น")

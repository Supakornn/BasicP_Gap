# haverice = True
# havespoon = False
# havehand = True

# if haverice:
#     if havespoon:
#         print("กินข้าว")
#     elif havehand:
#         print("กินข้าวเหนียว")


# score = int(input("Enter your score: "))

# if score >= 0:
#     if score <= 100:
#         if score >= 80: # 80 - 100
#             print("Grade A")
#         if score >= 70: 
#             if score < 80: # 70 - 79
#                 print("Grade B")
#         if score >= 60:
#             if score < 70: # 60 - 69
#                 print("Grade C")        
#         if score >= 50:
#             if score < 60: # 50 - 59
#                 print("Grade D")
#         if score < 50: # < 50
#             print("Grade F")  


# for i in range(1,10,2):
#     print(i)

# (1,10,2)
# start = 1
# stop = 10 (9)
# step = 2

# [1, 3, 5, 7 ,9]

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1 


while True:
    choice = int(input("กรอก 1) เพื่อบวกเลข, กรอก 2) เพื่อออก: "))
    
    if choice == 1:
        num = int(input("จำนวนเลขที่ต้องการจะบวก: "))
        sumation = 0
        
        for i in range(num):
            num1 = int(input("กรอกเลข: "))
            sumation = sumation + num1

        print("ผลลัพธ์", sumation) 
    
    if choice == 2:
        print("บาย บาย")
        break

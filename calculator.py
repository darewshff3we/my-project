# تعريف دالة للجمع
def add(x, y):
    return x + y

# تعريف دالة للطرح
def subtract(x, y):
    return x - y

# تعريف دالة للضرب
def multiply(x, y):
    return x * y

# تعريف دالة للقسمة
def divide(x, y):
    if y == 0:
        return "لا يمكن القسمة على صفر!"
    return x / y

# عرض الخيارات للمستخدم
print("اختر عملية:")
print("1. جمع")
print("2. طرح")
print("3. ضرب")
print("4. قسمة")

# استلام اختيار المستخدم
choice = input("أدخل رقم العملية (1/2/3/4): ")

# استلام الأرقام من المستخدم
num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))

# تنفيذ العملية المطلوبة
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("خيار غير صالح")
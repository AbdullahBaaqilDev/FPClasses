"""
وظيفتها                                |     اسمها
______________________________________________________________________________________________________________________________________________________________________
upper      | تعيد جميع احرف النص كاحرف كبيرة
lower      | تعيد جميع احرف النص كأحرف صغيرة
capitalize | تعيد أول حرف من الجملة حرف كبير وباقي احرف الكلمات احرف صغيرة
count      | تعيد عدد مرات تكرار الجملة المطلوب عدها
endswith   | تعيد صح او خطأ اذا كانت الجملة تنتهي بالأحرف المطلوبة
startswith | تعيد صح او خطا اذا كانت الجملة تبدأ بالأحرف المطلوبة
isdigit    | تعيد صح او خطأ اذا اكان النص عبارة عن رقم
"""
# Examples
z = "moHamed hussain baaqeil"
print("\nupper function")
print(z.upper())
print("\nlower function")
print(z.lower())
print("\ncapitalize function")
print(z.capitalize())
print("\ncount function")
print(z.count("a"))
print("\nendswith function")
print(z.endswith("d"))
print(z.endswith("eil"))
print("\nstartswith function")
print(z.startswith("s"))
print(z.startswith("m"))
print("\nisdigit function")
print(z.isdigit())
z = "10"
print(z.isdigit())
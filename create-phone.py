filename = "phone.txt"

with open(filename, "w") as f:
    for i in range(100_000_000): 
        number = f"09{str(i).zfill(8)}\n" 
        f.write(number)
    for i in range(100_000_000):  
        number = f"08{str(i).zfill(8)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"07{str(i).zfill(8)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"06{str(i).zfill(8)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"02{str(i).zfill(7)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"03{str(i).zfill(7)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"04{str(i).zfill(7)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"04{str(i).zfill(7)}\n"
        f.write(number)
    for i in range(100_000_000):  
        number = f"05{str(i).zfill(7)}\n"
        f.write(number)
    


print(f"สร้างไฟล์ {filename} เรียบร้อยแล้ว")

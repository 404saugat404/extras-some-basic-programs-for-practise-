def second(h,m,s):
    total_sec=h*3600+m*60+s
    return total_sec


hour=int(input("enter the hour: "))

min=int(input("enter the min: "))

sec=int(input("enter the sec: "))

total_second=second(hour,min,sec)
print(f"total sec is {total_second}")
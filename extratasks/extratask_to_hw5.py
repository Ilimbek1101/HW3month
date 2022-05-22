def make_readable(seconds):
    if type(seconds) == int and 0 <= seconds < 360000:
        HH = seconds // 3600
        MM = (seconds - HH*3600) // 60
        SS = seconds - HH*3600 - MM*60
        if HH < 10:
            HH = f"0{HH}"
        if MM < 10:
            MM = f"0{MM}"
        if SS < 10:
            SS = f"0{SS}"
        print(f"{HH}:{MM}:{SS}")
    else:
        print("Необходимо вводить неотрицательное целое число не более 359 999.")

make_readable(0)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)
make_readable(253629)
make_readable(-3745)
make_readable('Hello!')
"""
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.

    Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
          - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

"""

def timeConversion(s):
    hh, mm, ss = s.split(":", 2)
    ampm = ss[-2:]
    sss = ss[:2]
    if ampm == 'AM':
        if hh == "12":
            new_hh = '00'
        else:
            if hh[0] == '0':
                new_hh = f"0{int(hh) + 0}"
            else:
                new_hh = int(hh) + 0

        return f"{new_hh}:{mm}:{sss}"

    if ampm == 'PM':
        if hh == "12":
            new_hh = hh
        else:
            new_hh = int(hh) + 12
        
        return f"{new_hh}:{mm}:{sss}"


if __name__ == '__main__':

    ans = timeConversion("06:40:03AM")
    print(ans)
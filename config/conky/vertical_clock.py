import datetime
import sys

now = datetime.datetime.now()
# Change locale logic if needed, but hardcoding Kanji is safer
date_str = now.strftime('今日は%m月%d日')
time_str = now.strftime('%H時%M分・・・よ')
trans = str.maketrans('0123456789', '０１２３４５６７８９')
d_s = date_str.translate(trans)
t_s = time_str.translate(trans)

offset_down = 1  # How many chars to shove the Time down
gap = '　'       # Full-width space

max_len = max(len(d_s), len(t_s) + offset_down)

for i in range(max_len):
    # Date Char (Right Column)
    c_date = d_s[i] if i < len(d_s) else '　'
    
    # Time Char (Left Column)
    t_idx = i - offset_down
    c_time = t_s[t_idx] if (t_idx >= 0 and t_idx < len(t_s)) else '　'
    
    # Print: [Time] [Gap] [Date]
    print(f'{c_time}{gap}{c_date}') # With time on left

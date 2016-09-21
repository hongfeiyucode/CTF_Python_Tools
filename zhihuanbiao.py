import string
text = 'thinkingInAndroid'#.upper()
table=string.maketrans(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ',b'ISNOTKEYABCDFGHJLMPQRUVWXZ')
# 从前者换为后者，正常的思维模式
# table = string.maketrans(
# string.ascii_lowercase,
# string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print text.translate(table)#.lower()  #str.translate(text,table) is ok too
# .upper().lower() 为转换大小写
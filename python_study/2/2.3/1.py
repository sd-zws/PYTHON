#------字符串的大小写
name = "helLo pYthon"
print(name.title())
#Hello Python
print(name.upper())
#HELLO PYTHON
print(name.lower())
#hello python
#方法后面跟着括号，是因为方法通常需要额外的信息来完成工作，这种信息是括号内提供的。

#------字符串中使用变量
_file_name = "hello"
file_name_2 = f"{_file_name.title()} python"
print(file_name_2+"!")
#Hello python!
#f字符串。f是format(设置格式)的简写。
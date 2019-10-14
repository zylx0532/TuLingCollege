#常规FORMAT
s="我是：{}|我来自：{}|今年：{}岁了"
print(s.format("睿鑫","中国",11))

#占位FORMAT
s="我是：{1}|我来自：{0}|今年：{2}岁了"
print(s.format("中国","睿鑫",11))

#命名FORMAT
s="我是：{name}|我来自：{froom}|今年：{age}岁了"
print(s.format(froom="中国",name="睿鑫",age=11))

#字典FORMAT
#需要解包“**”
s="我是：{name}|我来自：{froom}|今年：{age}岁了"
s_d={"name":"睿鑫","froom":"中国","age":11}
print(s.format(**s_d))

#数字格式化
s="a{:.2f},b{:.3f}"
print(s.format(1.2434,3.45678))


#^<>    居中、左、右对齐 后面带宽度
#:      后面跟填充的字符，只能是一个字符不指定默认用空格填充
#+      表示在正数前显示+，负数前显示- ， 空格表示在正数前加空格
#bdox   分别是二、十、八、十六进制
#可以用大括号｛｝来转义大括号




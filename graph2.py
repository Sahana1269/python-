import matplotlib.pyplot as s

left = [23,45,60,90]

height = [13,56,90,10]

tick_label = ['2000', '2005', '2010', '2015']

s.bar(left, height,tick_label = tick_label,width=5,color = ['blue','green'])


s.xlabel("X Axis")
s.ylabel("Y Axis")
s.title("variation")
s.show()
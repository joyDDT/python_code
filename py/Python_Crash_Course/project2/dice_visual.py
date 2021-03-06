import pygal
from die import Die

#创建两个D6色子
die_1 = Die( )
die_2 = Die( )

#投掷多次色子，并将结果储存到一个列表中
results = [ ]
for roll_num in range(1000000):
    result = die_1.roll( ) + die_2.roll( )
    results.append(result)

#分析结果
frequencies = [ ]
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#可视化结果
hist = pygal.Bar( )

hist.title = 'Results of rolling two D6 dice 10000 times'
hist.x_labels =[x for x in range(2, max_result+1)]
#使用for循环来实现自动添加x坐标
##for i in range(2, max_result+1):
##    hist.x_labels.append(i)
    
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

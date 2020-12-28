import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show

# 多种基本图元绘制方法，网格展示
# 数据
N = 9
x = np.linspace(-2, 2, N)
y = x ** 2
sizes1 = 10
sizes2 = np.linspace(10, 20, N)
# xpts = np.array([-.09, -.12, .0, .12, .09])
# ypts = np.array([-.1, .02, .1, .02, -.1])
# 画布列表
figures = []
p = figure(title="circle")
p.circle(x, y, radius=0.1, color="#3288BD")
figures.append(p)
p = figure(title="x")
p.scatter(x, y, marker="x", size=8, color="#FF7F50")
figures.append(p)
p = figure(title="triangle")
p.scatter(x, y, marker="triangle", size=sizes1, color="#DD1C77", fill_color=None)
figures.append(p)
p = figure(title="diamond")
p.scatter(x, y, marker="diamond", size=sizes2, color="#1C9099", line_width=2)
figures.append(p)
# 网格展示
show(gridplot(figures, ncols=2, plot_width=200, plot_height=200))

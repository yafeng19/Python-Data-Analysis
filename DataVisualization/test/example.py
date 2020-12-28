#导入库
from bokeh.plotting import figure ,output_notebook,show
#output_notebook()   #在notebook 中显示
#数据
x=[3,7,2,4,5]
y=[1,2,5,6,3]
#画布：尺寸
p=figure(plot_width=400,plot_height=400)
#绘图：设定点的坐标、大小、颜色、透明度
p.circle(x,y,size=20,color="navy",alpha=0.5)
#显示
show(p)
from bokeh.sampledata.iris import flowers
from bokeh.transform import factor_cmap, factor_mark
from bokeh.plotting import figure, show

# 鸢尾花品种及分类标记
SPECIES = ['setosa', 'versicolor', 'virginica']
MARKERS = ['circle', 'x', 'diamond']
# 画布
p = figure(title="Iris Morphology", background_fill_color="#ffffff")
# 绘图
p.scatter("petal_length", "sepal_width", source=flowers, legend_group="species", fill_alpha=0.4, size=12,
          marker=factor_mark('species', MARKERS, SPECIES), color=factor_cmap('species', 'Category10_3', SPECIES))
# 其他
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Sepal Width'
# 显示
show(p)

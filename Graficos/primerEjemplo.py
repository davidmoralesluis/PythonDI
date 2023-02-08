
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4


doc = SimpleDocTemplate('informeGraficos.pdf', pagesize=A4)
guion = []
d = Drawing(400,200)
datos = [
    (13, 14, 23, 4, 5, 42, 19, 10),
    (12, 23, 25, 19, 32, 39, 12, 34)
]

gbarras = VerticalBarChart()
gbarras.x = 50
gbarras.y = 50
gbarras.height = 125
gbarras.width = 300
gbarras.data = datos
gbarras.strokeColor = colors.black
gbarras.valueAxis.valueMin = 0
gbarras.valueAxis.valueMax = 50
gbarras.valueAxis.valueStep = 10
gbarras.categoryAxis.labels.boxAnchor = 'nw'
gbarras.categoryAxis.labels.dx = 8
gbarras.categoryAxis.labels.dy = -2
gbarras.categoryAxis.labels.angle = -30
gbarras.categoryAxis.categoryNames = ['Xan', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago']
gbarras.groupSpacing = 10
gbarras.barSpacing = 2
d.add(gbarras)
guion.append(d)

guion.append(Spacer(20, 40))

d = Drawing(300,200)
gTarta = Pie()
gTarta.x = 65
gTarta.y = 15
gTarta.height = 170
gTarta.width = 170
gTarta.data = [10, 20, 30, 40, 50]
gTarta.labels = ['Edge', 'Brave','Safari', 'Firefox', 'Chrome']
gTarta.slices.strokeWidth = 0.5
gTarta.slices[3].popout = 10
gTarta.slices[3].strokeWidth = 2
gTarta.slices[3].strokeDashArray = [8,2]
gTarta.slices[3].labelRadius = 1.75
gTarta.slices[3].fontColor = colors.red
gTarta.sideLabels = 1

d.add(gTarta)


lenda = Legend()
lenda.x = 370
lenda.y = 0
lenda.dx = 8
lenda.dy = 8
lenda.fontName = 'Helvetica'
lenda.fontSize = 7
lenda.boxAnchor = 'n'
lenda.columnMaximum = 10
lenda.strokeWidth = 1
lenda.strokeColor = colors.black
lenda.deltax = 75
lenda.deltay = 10
lenda.autoXPadding = 5
lenda.yGap = 0
lenda.dxTextSpace = 5
lenda.alignment = 'right'
lenda.dividerLines = 1|2|4
lenda.dividerOffsY = 4.5
lenda.subCols.rpad = 30

colores = [colors.blue,colors.red,colors.green,colors.yellow,colors.pink]
for i, color in enumerate(colores):
    gTarta.slices[i].fillColor = color

lenda.colorNamePairs = [(
    gTarta.slices[i].fillColor,
    (gTarta.labels[i][0:20], '%0.2f' % gTarta.data[i]))
    for i in range(len(gTarta.data))
]

d.add(lenda)
guion.append(d)

doc.build(guion)


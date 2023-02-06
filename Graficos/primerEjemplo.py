
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
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
gTarta.slices[3].strokeDashArray = [2,2]
gTarta.slices[3].labelRadius = 1.75
gTarta.slices[3].fontColor = colors.red
gTarta.sideLabels = 1

d.add(gTarta)
guion.append(d)




doc.build(guion)


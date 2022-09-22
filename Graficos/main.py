from turtle import color
import matplotlib.pyplot as grafico
from pyparsing import col

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul']
temp = [30, 31, 27, 15, 18, 29, 35]

grafico.ion()
grafico.style.use('ggplot')
grafico.ylabel('Temp / C')
grafico.xlabel('Mês', color='blue')
grafico.axis(ymin=0, ymax=40)
grafico.title('Temperaturas Médias Mensais')
grafico.plot(meses, temp, label='Temperaturas', marker='o')
grafico.fill_between(meses, temp, color='r')
#grafico.bar(meses, temp)
grafico.legend()
grafico.show()
grafico.ioff()
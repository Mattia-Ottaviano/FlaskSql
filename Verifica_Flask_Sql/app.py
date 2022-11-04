from flask import Flask,render_template, request, redirect, url_for, Response
app = Flask(__name__)

import io
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import pymssql


@app.route('/', methods=['GET'])     
def home():
    return render_template('home.html')


@app.route('/infoUser', methods=['GET'])     
def infoUser():
  conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='ottaviano.mattia', password='xxx123##', database='ottaviano.mattia')
  nome = request.args['nome']
  cognome = request.args['cognome']  
  if 1=1:
  query = f'SELECT * from Sales.customers where {'nome'} in (select first_name from Sales.customers) and {'cognome'} in (select second_name from Sales.customers)'
  df = pd.read_sql(query,conn)
  else:
    return render_template('errore.html')
  return render_template('result.html', dati = list(df.values.tolist()))
  

  



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
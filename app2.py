from flask import Flask,render_template, request, redirect, url_for, Response
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route('/infoUser', methods=['GET'])     
def infoUser():
    return render_template('home2.html')

@app.route('/result', methods=['GET'])     
def result():
    nome = request.args['nome']
    cognome = request.args['cognome']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user= 'ottaviano.mattia', password='xxx123##', database='ottaviano.mattia')

    query = f"select * from sales.customers where first_name = '{nome}' and last_name = '{cognome}'"
    df = pd.read_sql(query, conn)
    dati = list(df.values.tolist())
    if dati == []:
        return render_template('errore1.html')
    else:
        # visualizzare le informazioni
        return render_template('risultati2.html', nomiColonne = df.columns.values, dati = list(df.values.tolist()))












if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask,render_template, request, redirect, url_for, Response
app = Flask(__name__)

import pandas as pd
import pymssql 

@app.route('/', methods=['GET'])     
def home():
    return render_template('home1.html')



@app.route('/ricerca', methods=['GET'])     
def ricerca():
    nomeStore = request.args['store']
    
    # collegamento al Database
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user= 'ottaviano.mattia', password='xxx123##', database='ottaviano.mattia')

    # Invio query al Database e ricezione informazioni
    query = f"select sf.first_name, sf.last_name from sales.stores as st inner join sales.staffs as sf on sf.store_id = st.store_id where st.store_name = '{nomeStore}'"
    df = pd.read_sql(query, conn)
    dati = list(df.values.tolist())
    if dati == []:
        return render_template('errore1.html')
    else:
        # visualizzare le informazioni
        return render_template('risultati1.html', nomiColonne = df.columns.values, dati = list(df.values.tolist()))















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
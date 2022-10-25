from flask import Flask,render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])     
def home():
    return render_template('home.html')


@app.route('/opzione', methods=['GET'])     
def opzione():
    scelta = request.args['scelta']
    if scelta == 'es1':
        return render_template('es1.html')
    elif scelta == 'es2':
        return render_template('es2.html')
    if scelta == 'es3':
        return render_template('es3.html')
    elif scelta == 'es4':
        return render_template('es4.html')

    



@app.route('/result', methods=['GET'])     
def result():
    # collegamento al Database
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user= 'ottaviano.mattia', password='minou#@123!Mo05', database='ottaviano.mattia')

    # Invio query al Database e ricezione informazioni
    NomeProdotto = request.args['NomeProdotto']
    query = f"select * from production.products inner join production where product_name like '{NomeProdotto}%' "
    dfProdotti = pd.read_sql(query,conn)
    # visualizzare le informazioni
    return render_template('result.html', nomiColonne = dfProdotti.columns.values, dati = list(dfProdotti.values.tolist()))
    


 





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
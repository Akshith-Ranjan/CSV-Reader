#!/usr/bin/python
from flask import Flask, render_template,request
import csv
app = Flask(__name__)

#READ FUNCTION READ CSV FILE AND RETURNS LIST
def read_file(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        data=[r for r in reader]
        return data


@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.args.get('a') and request.args.get('b')):
        #FETCHING GET PARAMETERS
        a = request.args.get('a', '')
        b = request.args.getlist('b')
        try:
            #DATAYPE CONVERSION AND READING REQUIRED CSV FILE
            for x in range(len(b)):
                b[x]=int(b[x])
            data = read_file("data/" + a)
            #REDERING TEMPLATE WITH CSV TABLE CONTENTS
            return render_template("index.html", data=data, b=b, a=a.replace('.csv','').title())
        except:
            #RENDERING TEMPLATE WITH ERROR 404
            error=['404','Page not found.']
            return render_template("index.html", error=error)
    else:
        #RENDERING TEMPLATE
        return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

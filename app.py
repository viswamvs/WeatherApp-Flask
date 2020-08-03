from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from operator import itemgetter

app = Flask(__name__)

@app.route('/')
def index():    
    city=[{'name':'New Delhi'}, 
    {'name':'Mumbai'}, 
    {'name':'Chennai'}, 
    {'name':'Kolkatta'}, 
    {'name':'Bangalore'}, 
    {'name':'Visakhapatnam'}, 
    {'name':'Ranchi'}, 
    {'name':'Hyderabad'}, 
    {'name':'Indore'}, 
    {'name':'Jaipur'},
    {'name':'Ahmedabad'},
    {'name':'Bhubaneswar'},
    {'name':'Kanpur'},
    {'name':'Jabalpur'},
    {'name':'Lucknow'},
    {'name':'Pune'},
    {'name': 'Vellore'}]
    newlist = sorted(city, key=itemgetter('name'))  
    return render_template(  'weather.html', data=newlist)


@app.route("/result" , methods=['GET', 'POST'])
def result():    
    data = []    
    error = None    
    select = request.form.get('comp_select')    
    resp = query_api(select)    
    pp(resp)    
    if resp:       
        data.append(resp)    
        if len(data) != 2:        
            error = 'Bad Response from Weather API'    
            return render_template('result.html', data=data, error=error)


if __name__=='__main__':   
    app.run(debug=True)

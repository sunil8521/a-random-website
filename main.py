from flask import Flask, render_template,jsonify
app=Flask(__name__,template_folder='all_details')
joblist=[
    {
      'id':1,
      'tittle':'web-devloper',
      'salary':'12,000'
    },
    {
      'id':2,
      'tittle':'data-scientist',
      'salary':'90,000'
    },
    {
      'id':3,
      'tittle':'software-devloper',
      'salary':'1,20,000'
    },
    {
      'id':4,
      'tittle':'hacker',
      'salary':'12,20,000'
    },
    {
      'id':5,
      'tittle':'CEO',
      'salary':'5,00,000'
    },
    {
      'id':6,
      'tittle':'Engineer',
      'salary':'1,00,000'
    },
    {
      'id':7,
      'tittle':'Produc Management',
      'salary':'2,00,000'
    }
]
@app.route('/')
def hell():
  return render_template('home.html',job=joblist,sitename='job')

@app.route('/api/joblist')
def jobs():
  return jsonify(joblist)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

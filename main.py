from flask import Flask, render_template,jsonify
from data import store,by_id
app=Flask(__name__,template_folder='all_details')
@app.route('/')
def hell():
  joblist=store()
  return render_template('home.html',job=joblist,sitename='job')

@app.route('/api/joblist')
def jobs():
  joblist=store()
  return jsonify(joblist)

@app.route("/jobs/<id>")
def jobs_detail(id):
  detail=by_id(id)
  if not detail:
    return render_template('error.html')
  return render_template('detail.html',jobinfo=detail)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

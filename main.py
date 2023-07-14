from flask import Flask, render_template,jsonify,request
from data import store,by_id,detail_add
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

@app.route("/jobs/<id>/apply",methods=['post'])
def apply_for_job(id):
  data=request.form
  detail=by_id(id)
  detail_add(data["full_name"],data["email"],data["linkedin"],data["education"],data["experience"],detail["Tittle"])
  return render_template('submitted.html',persondata=data,jobname=detail)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)


import sys
sys.path.insert(1, './castor/api')

from user import get_users, get_user
from study import get_studies, get_study, get_study_user
from export_data import export_study_data
from institute import get_study_institutes, get_study_institute
from record import get_study_records, get_study_record
from step import get_study_step
from flask import Flask, render_template, request
from json import dumps, loads
from datetime import datetime as dt
import os

f = open('devel.env', 'r')
env = loads(f.read())

for key in env.keys():
  os.environ[key] = env[key]

app = Flask(__name__)
#
# FILTER TEMPLATES
#
@app.template_filter('dumpjson')
def dumpjson(jsonObject):
  return dumps(jsonObject, indent=2)

@app.template_filter('date')
def date(datetimeString):
  dateTime = dt.strptime(datetimeString, '%Y-%m-%d %H:%M:%S.%f')
  return '{:%Y-%m-%d %H:%M}'.format(dateTime)

#
# ROUTES
#
@app.route('/')
@app.route('/index')
def index():
  studiesData = get_studies()
  studies = studiesData['_embedded']['study']
  for studyData in studies:
    domain = 'us' if 'data' in studyData['domain'] else 'uk'
    studyRecordsData = get_study_records(studyData['study_id'], domain=domain)['_embedded']['records']
    studyData.update({
      "records": studyRecordsData
    })  

  return render_template('index.html', data=studies)

@app.route('/study/<string:studyID>/institutes')
def study_institutes(studyID):
  domain=request.args.get('domain')

  institutesData = get_study_institutes(studyID, domain)

  institutes = institutesData['_embedded']['institutes']
  attributes = institutes[0].keys()
  attributes.remove('_links')
  attributes.remove('id')
  attributes.remove('institute_id')

  return render_template('study_institutes.html', studyID=studyID, data=institutes, keys=sorted(attributes), size=len(institutes), domain=domain)

@app.route('/study/<string:studyID>/records')
def study_records(studyID):
  domain=request.args.get('domain')

  recordsData = get_study_records(studyID, domain)
  
  records = recordsData['_embedded']['records']
  attributes = records[0].keys()
  attributes.remove('_embedded')
  attributes.remove('_links')
  attributes.remove('id')
  attributes.remove('record_id')
  
  return render_template('study_records.html', studyID=studyID, data=records, keys=sorted(attributes), size=len(records), domain=domain)

@app.route('/api/user/<string:userID>')
def user(userID):
  userData = get_user(userID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=userData)

@app.route('/api/study/<string:studyID>')
def study(studyID):
  studyData = get_study(studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=studyData)

@app.route('/api/study/<string:studyID>/user/<string:userID>')
def study_user(studyID, userID):
  studyUserData = get_study_user(studyID, userID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=studyUserData)  

@app.route('/api/study/<string:studyID>/step/<string:stepID>')
def study_step(studyID, stepID):
  studyStepData = get_study_step(studyID, stepID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=studyStepData)  

@app.route('/api/study/<string:studyID>/record/<string:recordID>')
def record(studyID, recordID):
  recordData = get_study_record(recordID, studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=recordData)

@app.route('/api/study/<string:studyID>/institute/<string:instituteID>')
def institute(studyID, instituteID):
  instituteData = get_study_institute(instituteID, studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=instituteData)  

@app.route('/api/study/<string:studyID>/export/data')
def export_data(studyID):
  exportData = export_study_data(studyID, domain=request.args.get('domain'))

  return render_template('json_viewer.html', data=exportData)

if __name__ == '__main__':
  app.run()
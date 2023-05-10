#/usr/bin/python3
import os
from flask import Flask, jsonify, request, abort, render_template, redirect, url_for, make_response
import json

debug = 1

app = Flask(__name__)

### This is our simplified CMDB for demo purposes
vms = {
    'fin_01' : "finance1",
    'fin_02' : "finance1",
    'fin_03' : "finance1",
    'mkt_01' : "marketing1",
    'mkt_02' : "marketing1",
    }

quotas = {
    'Manufacturing' : 400,
    'Marketing' : 900,
    'Finance' : 500,
    'Engineering' : 90000
    }

teams = {
    'manufacturing1' : 'Manufacturing',
    'marketing1' : 'Marketing',
    'finance1' : 'Finance',
    'engineering1' : 'Engineering'
    }

### WEB UI ROUTES ###
@app.route('/cmdb')
def cmdb():
    if request.method == 'GET':
        return render_template('cmdb.html', vms=vms, quotas=quotas, teams=teams)


@app.route('/', methods=['GET','POST'])
def index():

    resp = make_response(render_template('menu.html')) 
    return resp

@app.route('/adhocbackup', methods=['GET', 'POST'])
def adhocbackup():
    if request.method == 'GET':

        return render_template('adhocbackup.html',vms=vms)

    if request.method == 'POST':
        req_details = request.form.to_dict()
        if debug:
            print(req_details)

        return render_template('success.html', operation_type="Adhoc Backup", jobid="dummy ID")

@app.route('/registervm', methods=['GET', 'POST'])
def registervm():
    if request.method == 'GET':

        return render_template('registervm.html')

    if request.method == 'POST':
        req_details = request.form.to_dict()
        if debug:
            print(req_details)

        return render_template('success.html', operation_type="Register VM", jobid="dummy ID")

@app.route('/restorebackup', methods=['GET', 'POST'])
def restorebackup():
    if request.method == 'GET':

        return render_template('restorebackup.html',vms=vms)

    if request.method == 'POST':
        req_details = request.form.to_dict()
        if debug:
            print(req_details)

        return render_template('success.html', operation_type="Restore Backup", jobid="dummy ID")

@app.route('/vm', methods=['GET', 'POST'])
def vm():
    if request.method == 'GET':
        return render_template('vm.html')

    if request.method == 'POST':
        req_details = request.form.to_dict()
        if debug:
            print(req_details)
        return render_template('success.html', operation_type="Create VM", jobid="Dummy ID")


if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '80')), threaded=True)


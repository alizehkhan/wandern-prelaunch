############ Seyhan Van Khan & Alizeh Khan
############ Wandern - wanderntrails.com
############ An easy way to find and book mountain huts and campsites on popular hiking trails.
############ December 2020

################################ IMPORT MODULES ################################


from os import environ
from airtable import Airtable
from flask import Flask, send_from_directory, render_template, redirect, request, url_for


################################### INIT APP ###################################


app = Flask(__name__, static_url_path='/assets', static_folder='assets')
app.secret_key = "sanjayguptabobsteve"


##################################### INDEX ####################################


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		record = {
	    "Email": request.form["email"]
		}
		emailsAirtable = Airtable(environ.get('AIRTABLE_TABLE'), 'Emails', environ.get('AIRTABLE_KEY'))
		emailsAirtable.insert(record)

		return redirect('/')


################################ PRIVACY POLICY ################################


@app.route('/privacy')
def privacy():
	return render_template('privacy.html')


############################## FAVICONS & SITEMAP ##############################


@app.route('/apple-touch-icon.png')
@app.route('/favicon.ico')
@app.route('/icon-192.png')
@app.route('/icon-512.png')
@app.route('/icon.svg')
@app.route('/manifest.webmanifest')
@app.route('/app-logo.png')
def favicons():
	return send_from_directory('assets/images/favicons', request.path[1:])


@app.route('/sitemap.xml')
def sitemap():
	return send_from_directory('assets', 'sitemap.xml')


################################# OTHER ROUTES #################################


@app.route('/<path:dummy>')
def fallback(dummy):
	return redirect(url_for('/'))


#################################### APP RUN ###################################


if __name__ == "__main__":
	app.run(debug=True)

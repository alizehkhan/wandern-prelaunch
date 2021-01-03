############ Seyhan Van Khan & Alizeh Khan
############ Wandern - wanderntrails.com
############ An easy way to find and book mountain huts and campsites on popular hiking trails.
############ December 2020

################################ IMPORT MODULES ################################


from importlib.util import find_spec
from os import environ
from socket import gethostbyname_ex, gethostname

from flask import Flask, redirect, render_template, request, send_from_directory, url_for

if find_spec('airtable'):
	from airtable import Airtable
	import mailchimp_marketing as MailchimpMarketing
	from mailchimp_marketing.api_client import ApiClientError


##################################### APIs #####################################


def addEmailToAirtable(email):
	emailsAirtable = Airtable(environ.get('AIRTABLE_WANDERN_TABLE'), 'Emails', environ.get('AIRTABLE_KEY'))
	emailsAirtable.insert({"Email": email})


def addEmailToMailchimp(email):
	mailchimp = MailchimpMarketing.Client()
	mailchimp.set_config({
		"api_key": environ.get('MAILCHIMP_KEY'),
		"server": environ.get('MAILCHIMP_SERVER_PREFIX')
	})

	memberInfo = {
		"email_address": email,
		"status": "subscribed",
	}

	try:
		response = mailchimp.lists.add_list_member(environ.get('MAILCHIMP_AUDIENCE_ID'), memberInfo)
		print("response: {}".format(response))
		return "success"
	except ApiClientError as error:
		print("An exception occurred: {}".format(error.text))
		return "userExists" if '"Member Exists"' in error.text else "error"


################################### INIT APP ###################################


app = Flask(__name__, static_url_path='/assets', static_folder='assets')
app.secret_key = "sanjayguptabobsteve"


##################################### INDEX ####################################


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html', inputMessage='')
	else:
		try:
			# add email as a Mailchimp contact & return type of response
			# success | userExists | error
			response = addEmailToMailchimp(request.form['email'])

			# if no errors, add email to airtable
			if response == 'success':
				addEmailToAirtable(request.form['email'])
			# errors or no errors, render index.html with the correct response
			return render_template('index.html', inputMessage=response)

		# any other error raised, put error message on html
		except:
			return render_template('index.html', inputMessage='error')


################################ PRIVACY POLICY ################################


@app.route('/privacy')
@app.route('/privacypolicy')
@app.route('/privacy-policy')
def privacy():
	return render_template('privacy.html')


############################## FAVICONS & SITEMAP ##############################


@app.route('/apple-touch-icon.png')
@app.route('/favicon.ico')
@app.route('/icon-192.png')
@app.route('/icon-512.png')
@app.route('/icon.svg')
@app.route('/manifest.webmanifest')
@app.route('/og-image.png')
def favicons():
	return send_from_directory('assets/images/favicons', request.path[1:])


@app.route('/sitemap.xml')
def sitemap():
	return send_from_directory('assets', 'sitemap.xml')


############################## OTHER ROUTES - 404 ##############################


@app.route('/<path:dummy>')
def fallback(dummy):
	return redirect(url_for('/'))


##################################### RUN ######################################


if __name__ == "__main__":
	ipAddress = gethostbyname_ex(gethostname())[-1][-1]
	if ipAddress[:3] == "192":
		app.run(debug=True, host=ipAddress)
	else:
		app.run(debug=True)

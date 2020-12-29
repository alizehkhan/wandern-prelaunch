############ Seyhan Van Khan & Alizeh Khan
############ Wandern - wanderntrails.com
############ An easy way to find and book mountain huts and campsites on popular hiking trails.
############ December 2020

################################ IMPORT MODULES ################################


from os import environ

from flask import Flask, send_from_directory, render_template, redirect, request, url_for

# if importlib.util.find_spec('airtable'):
from airtable import Airtable
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


##################################### APIs #####################################


def addEmailToAirtable(email):
	emailsAirtable = Airtable(environ.get('AIRTABLE_WANDERN_TABLE'), 'Emails', environ.get('AIRTABLE_KEY'))
	emailsAirtable.insert({"Email": email})

def addContactToMailchimp(email):
	mailchimp = MailchimpMarketing.Client()
	mailchimp.set_config({
		"api_key": environ.get('MAILCHIMP_KEY'),
		"server": environ.get('MAILCHIMP_SERVER_PREFIX')
	})

	member_info = {
		"email_address": email,
		"status": "subscribed",
	}

	try:
		response = mailchimp.lists.add_list_member(environ.get('MAILCHIMP_AUDIENCE_ID'), member_info)
		print("response: {}".format(response))
	except ApiClientError as error:
		print("An exception occurred: {}".format(error.text))


################################### INIT APP ###################################


app = Flask(__name__, static_url_path='/assets', static_folder='assets')
app.secret_key = "sanjayguptabobsteve"


##################################### INDEX ####################################


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		if environ.get('AIRTABLE_WANDERN_TABLE'):
			addEmailToAirtable(request.form['email'])
			addContactToMailchimp(request.form['email'])
		else:
			print("\n\n\n\nYou dont have API key environment variables on your mac you dumbass.\n\n\n")

		return redirect('/')


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


################################# OTHER ROUTES #################################


@app.route('/<path:dummy>')
def fallback(dummy):
	return redirect(url_for('/'))


#################################### APP RUN ###################################


if __name__ == "__main__":
	# app.run(debug=True)
	addContactToMailchimp("seyhan546+2@gmail.com")

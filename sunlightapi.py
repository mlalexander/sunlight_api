import urllib2, json

API_KEY = '70f72edb0e034b10bc328c468e591b54'

def get_bills(state, subject):

    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=%s&type=bill&subject=%s&apikey=%s' % (state, subject, API_KEY))
    json_object = json.load(response)

    for result in json_object:
        print result['title']

    return

get_bills('mo', 'Transportation')

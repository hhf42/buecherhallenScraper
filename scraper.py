# Python 3
import requests
import time
import re
import messagebird

# MessageBird API Key
MessageBirdKey = 'nnnn'

# SMS Empfänger im Format +49...
SMSEmpfaenger = 'nnnn'

# Liste der gesuchten Bücher im Format der HTML-Seitennamen, auf buecherhallen.de nach dem Buch suchen, auswählen
# und dann aus dem Seitennamen entnehmen.
BuecherListe = [
    'T019354435',
    'T01902219X',
    'T019354423',
    'T016419898',
    ]

# Liste der zu durchsuchenden Bücherhallen, also die, die man gut erreichen kann. Eine Rückgabe ist überall möglich.
BuecherhallenListe = [
    'Alstertal',
    'Volksdorf',
    ]

UrlBasis = 'https://www.buecherhallen.de/suchergebnis-detail/medium/'

# Funktion, um eine SMS zu verschicken unter Verwendung der messagebird.com API
#
def SchickeSMS(SMSText):
    client = messagebird.Client(MessageBirdKey)
    message = client.message_create(
        'Buchscraper',
        SMSEmpfaenger,
        SMSText,
        {'reference' : 'Foobar'}
        )

# Funktion, um nach einem Buch in einer Bücherhalle zu suchen und ggf. eine SMS zu schicken
# wenn sich das Layout der Website ändert, dann läuft die regex ins Leere, das kann man sicher eleganter machen
#
def SucheBuch(GesuchtesBuch,GesuchteBuecherhalle):
    UrlBuch = UrlBasis+GesuchtesBuch+'.html'
    #print(time.ctime(),UrlBuch)
    try:
        Website = requests.get(UrlBuch)
    except:
        print(time.ctime(),'Request nicht möglich')
    try:
        r = re.search(GesuchteBuecherhalle+'</span>\n    <span class="medium-availability-item-title-icon">\n              <svg width="19px" height="19px" viewBox="0 0 19 19" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" role="img" aria-label="Verfügbar">', str(Website.text))
    except:
        print(time.ctime(),'Regex nicht möglich')
        r = 0

    if r:
        print(time.ctime(),'Buch '+GesuchtesBuch+' gefunden in '+GesuchteBuecherhalle)
        SchickeSMS('Buch '+GesuchtesBuch+' gefunden in '+GesuchteBuecherhalle)
    else:
        print(time.ctime(),'Buch '+GesuchtesBuch+' nicht in '+GesuchteBuecherhalle)
        
# Nach allen Büchern in allen Bücherhallen suchen und dann eine Stunde warten. 
#
while True:
    for Buch in BuecherListe:
        for Buecherhalle in BuecherhallenListe:
            SucheBuch(Buch, Buecherhalle)
    
    print(time.ctime(),'Beendet, 1h warten')
    time.sleep(3600)

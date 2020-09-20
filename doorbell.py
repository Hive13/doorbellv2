from flask import Flask
from flask import request
import xmltodict
import time
import simpleaudio as sa

api = Flask(__name__)

@api.route('/event', methods=['POST'])
def phone_event():
    xmlevent = xmltodict.parse(request.data)
    if 'IncomingCallEvent' in xmlevent['PolycomIPPhone']:
        print('INCOMING CALL FROM ' + xmlevent['PolycomIPPhone']['IncomingCallEvent']['CallingPartyName'])
        phonesound = sa.WaveObject.from_wave_file('phone.wav')
        for x in range(1,3):
            play_obj = phonesound.play()
            play_obj.wait_done()
            time.sleep(4)
    return 'Accepted'

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0', port=7466)

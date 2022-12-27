from flask import Flask, request
import string
import random
app = Flask(__name__)

news = {
    "title": "RiffApiLocal",
    "msg": "You're connected to RiffApiLocal.\nOnline features are unavailable.\nNo data will be saved.",
}
username = "RiffApiLocal"

responses = {
    "Configuration": '{"results":[{"objectId":"ITz5K79wcQ","updatedAt":"2015-10-06T15:37:10.761Z","RegionGroup":"Default","createdAt":"2015-08-27T16:48:23.993Z","OnTrackCoinValue":10,"TrackConversionCost":300,"ShareScoreCoinReward":200,"WatchAdCoinReward":200,"TrackCreatorCoinReward":100}]}',
    "News": f'{{"results":[{{"objectId":"RiffApiLocalNews","updatedAt":"2000-01-01T00:00:00.000Z","de":"{news["msg"]}","createdAt":"2000-01-01T00:00:00.000Z","ru":"{news["msg"]}","en":"{news["msg"]}","esTitle":"{news["title"]}","it":"{news["msg"]}","fr":"{news["msg"]}","frTitle":"{news["title"]}","itTitle":"{news["title"]}","es":"{news["msg"]}","enTitle":"{news["title"]}","Status":"Active","ruTitle":"{news["title"]}","deTitle":"{news["title"]}","Pinned":true,"ID":16}}]}}',
    "Profile_Steam": f'{{"results":[{{"objectId":"{username}Profile","SystemID":"1","FavouriteCar":1,"FavouriteSong":"null","FavouriteGenre":"pop","DriverLevel":0,"Platform":"PC","Username":"{username}","createdAt":"2000-01-01T00:00:00.000Z","updatedAt":"2000-01-01T00:00:00.000Z"}}]}}',
    "Version": '{"results":[{"objectId":"BoJMZ1TQJZ","updatedAt":"2015-02-10T21:05:53.214Z","Ver":100,"createdAt":"2015-02-10T20:50:24.164Z"}]}',
    "_Installation": '{"opens":1,"updatedAt":"2000-01-01T00:00:00.000Z"}'
}

@app.route('/events/AppOpened', methods=['GET', 'POST'])
def AppOpened():
    return '{}'

@app.route('/files/<file>', methods=['GET', 'POST'])
def Files(file):
    return '{"url":"http://127.0.0.1/file.bin","name":"file.bin"}'

@app.route('/classes/<event>', methods=['GET'])
def ClassEventGET(event):
    return responses.get(event, '{"results":[]}')

@app.route('/classes/<event>', methods=['POST', 'PUT'])
def ClassEventPOST(event):
    return f'{{"objectId":"{"".join(random.choice(string.ascii_lowercase) for _ in range(10))}","createdAt":"2000-01-01T00:00:00.000Z"}}'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5144, debug=False)

# sed -i "s/https:\/\/parseapi.back4app.com/http:\/\/127.000000000.0.1:5144/g" ParseOctane.dll

from flask import render_template, Flask, request
import cryptocode



app = Flask(__name__, static_url_path='/static')

def read_key():
    f = open("../shared_photons/key.txt", "r")
    key = f.read()
    return key

@app.route('/', methods=['GET'])
def index():
    data = request.args.get('data')
    key = read_key()
    data_decoded = cryptocode.decrypt(data, key)
    print(data_decoded)
    return render_template('index.html', data = data_decoded)


if __name__ == '__main__':
     app.run(port='5001')



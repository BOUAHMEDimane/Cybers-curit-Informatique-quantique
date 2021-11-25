from flask import render_template, Flask, request
import cryptocode



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = cryptocode.decrypt(request.args.get('data'), '123')
    print(data)
    return render_template('index.html', data = data)


if __name__ == '__main__':
     app.run(port='5001')



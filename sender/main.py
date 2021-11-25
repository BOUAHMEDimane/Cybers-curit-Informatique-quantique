# import quantumrandom
# import requests

# key = quantumrandom.get_data(data_type='hex16', array_length=1, block_size=10)

# print(key)

# data = input("Give your data")

# print(data)

# # Encrypt our data with our key

# data +=key[0]
# print(data)

# x = requests.post("http://127.0.0.1:5002/", json = {"content":data})

# print(x)


from flask import render_template, Flask, request, redirect
import cryptocode
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/crypte', methods=['POST'])
def crypte():
    data = request.form['data']
    print(data)
    encoded_data = cryptocode.encrypt(data, '123')

    return redirect('http://127.0.0.1:5001/?data='+encoded_data)


if __name__ == '__main__':
     app.run(port='5000')



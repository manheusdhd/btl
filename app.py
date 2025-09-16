from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name', 'Khách')
    text = request.form.get('text', '').strip()
    if text:
        messages.append({'name': name, 'text': text})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

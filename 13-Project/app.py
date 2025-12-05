from flask import Flask, render_template, request, session, redirect, url_for
from sentiment import analyze_sentiment

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        feedbacks = request.form.get('feedbacks', '').strip().split('\n')
        if feedbacks:
            for text in feedbacks:
                if text.strip():
                    sentiment, emoji, confidence = analyze_sentiment(text.strip())
                    result = {
                        'text': text.strip(),
                        'sentiment': sentiment,
                        'emoji': emoji,
                        'confidence': confidence
                    }
                    results.append(result)

                    if 'history' not in session:
                        session['history'] = []
                    session['history'].append(result)
            session.modified = True
   
    return render_template('index.html', results=results, history=session.get('history', []))

@app.route('/delete_history')
def delete_history():
    session.pop('history', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
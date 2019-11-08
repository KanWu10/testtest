from flask import Flask, request, render_template, redirect
from textblob import TextBlob
from jieba import analyse

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        text = request.form['text']  
        option = request.form['option']  

        if option == 'sentiment analyse':
            blob_obj = TextBlob(text)
            sentiment_score = blob_obj.sentiment.polarity
            result = 'sentiment analyse: %.2f (-1.0 negative，1.0positive)' % sentiment_score

        elif option == 'keyword extraction':
            keywords = analyse.extract_tags(text)
            result = 'Top3 keyword: %s' % (' / '.join(keywords[:3]))

        elif option == 'Part-of-speech':
            blob_obj = TextBlob(text)
            tags = [v + '/' + t for v, t in blob_obj.tags]
            result = 'Part-of-speech Result:\n %s' % ('\n'.join(tags))

        elif option == 'Noun Phrase Extraction':
            blob_obj = TextBlob(text)
            result = 'Noun Phrase:\n %s' % (' / '.join(blob_obj.noun_phrases))

        return render_template('index.html', result=result, oldtext=text)

    return render_template('index.html', name=0)


if __name__ == '__main__':
    app.run()

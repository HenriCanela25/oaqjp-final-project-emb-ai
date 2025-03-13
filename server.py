""" This is the server module """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def server_emotion_detector():
    """This function is for analyze the text given by the user"""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is not None:

        dominant_emotion = response.pop('dominant_emotion')

        result = f"""For the given statement, the system response is {response}.
        The dominant emotion is {dominant_emotion}"""

        return result

    return "Invalid text! Please try again!"

@app.route('/')
def render_page():
    """This function is for returning the main page"""

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

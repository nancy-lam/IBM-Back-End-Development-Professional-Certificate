""" 
    Develop a web application called Emotion Detector 
    integrated with Embeddable Watson AI libraries.
    Execute over the flask channel and deploy on localhost:5000. 
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Extract text from thr HTML interface 
    and run emotion_detector function 
    to show the emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input ! Try again."

    return f"For the given statement, the system response is " \
       f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
       f"'joy': {joy}, and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

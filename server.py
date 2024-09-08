''' Servery.py
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detector_function():
    '''Function calling the application
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['Dominant emotion'] is None:
        response_text = "Invalid text! Please try again!."
    else:
        response_text = f"Emotion: {response['Dominant emotion']} Score: {response['Score']}."
    return response_text

@app.route("/")
def render_index_page():
    '''Rendering HTML
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from robot_speech_to_text.executor import SpeechToTextExecutor

if __name__ == '__main__':
    text = SpeechToTextExecutor().execute()
    print(text)


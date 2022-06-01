import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone()  as audio:
    print("talk")
    # data=r.listen(audio)
    data=r.listen(audio)
    text=r.recognize_google(data)
    print("{done")
print(text)

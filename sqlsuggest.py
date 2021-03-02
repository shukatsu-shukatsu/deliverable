import pya3rt_v1
import speech_recognition as sr
from datetime import datetime


apikey = "aaaaaaaaaaaaaa"
client = pya3rt_v1.SQLSuggestClient(apikey)

#ログとしてテキストに保存する
filename = datetime.now().strftime('%Y%m%d')
txt ='logs/'+ filename +".txt"

with open(txt,'a') as f:
    f.write(filename + "\n") 


r = sr.Recognizer()
mic = sr.Microphone()

while True:
    print("何か言ってください")

    with mic as source:
        #ノイズ対策
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print ("認識中")
#todo:自己学習させたCSVファイルをもとにSQLを返すようにする
#現状は外部APIに頼っている
    try:
        # "ストップ" と言ったら音声認識を止める
        if r.recognize_google(audio, language='ja-JP') == "ストップ":
            print("end")
            break
        else:
            print(r.recognize_google(audio, language='ja-JP'))
            print(client.sql_suggest(r.recognize_google(audio, language='ja-JP')))

            #ファイルに内容追加する
            with open(txt,"a",newline='\n') as f:
                f.write('\n' + r.recognize_google(audio, language='ja-JP'))
                f.write('：' + client.sql_suggest(r.recognize_google(audio, language='ja-JP')).get('sql'))


    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
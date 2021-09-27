import re
import requests


# ************************************************
# remove_custom_emoji
# 絵文字IDは読み上げない
# ************************************************


def remove_custom_emoji(text):

    # pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>'    # カスタム絵文字のパターン
    pattern = r'<:'    # カスタム絵文字のパターン
    text = re.sub(pattern, '', text)   # 置換処理
    pattern = r':[0-9]+>'    # カスタム絵文字のパターン
    return re.sub(pattern, '', text)   # 置換処理

# ************************************************
# url_shouryaku
# URLなら省略
# ************************************************


def url_shouryaku(text):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern, 'URLは省略するのデス！', text)   # 置換処理

# ************************************************
# remove_picture
# 画像ファイルなら読み上げない
# ************************************************


def remove_picture(text):
    pattern = r'.*(\.jpg|\.jpeg|\.gif|\.png|\.bmp)'
    return re.sub(pattern, '', text)   # 置換処理

# ************************************************
# remove_command
# コマンドは読み上げない
# ************************************************


def remove_command(text):
    pattern = r'^\!.*'
    return re.sub(pattern, '', text)   # 置換処理

# ************************************************
# remove_log
# 参加ログは読み上げない
# ************************************************


def remove_log(text):
    pattern = r'(\【VC参加ログ\】.*)'
    return re.sub(pattern, '', text)   # 置換処理


# ************************************************
# creat_WAV
# message.contentをテキストファイルと音声ファイルに書き込む
# 引数：inputText
# 書き込みファイル：input.txt、output.wav
# ************************************************


def creat_WAV(inputText):

    inputText = remove_custom_emoji(inputText)   # 絵文字IDは読み上げない
    inputText = remove_command(inputText)   # コマンドは読み上げない
    inputText = url_shouryaku(inputText)   # URLなら省略
    inputText = remove_picture(inputText)   # 画像なら読み上げない
    inputText = remove_log(inputText)   # 参加ログなら読み上げない

    payload = {'text': inputText, 'speaker': 0}
    headers = {'accept': 'application/json'}
    r = requests.post('http://127.0.0.1:50021/audio_query',
                      params=payload, headers=headers)
    queryDict = r.json()

    queryDict['kana'] = ""  # ここを虚無にしないとエスケープ付近が解読できずに422エラーが起きて処理が終わる

    payload = {'speaker': 0}
    headers = {'accept': 'audio/wav', 'Content-Type': 'application/json'}
    audio = requests.post('http://127.0.0.1:50021/synthesis',
                          params=payload, headers=headers, json=queryDict)
    audio.raise_for_status()

    # 出力ファイル名　and　Path
    ow = 'output.wav'
    with open(ow, 'wb') as file:
        file.write(audio.content)

    # return audio.content
    return True


if __name__ == '__main__':
    creat_WAV('テスト')

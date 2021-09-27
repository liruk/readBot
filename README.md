# readBot
##【fork元】  
https://qiita.com/Nemy/items/d895114d3ba9a9d7cb62  
This is the source code of the reading bot of Discord. It's a little better than when I posted it on Qiita.  
## 実行方法
1.まずVOICEVOX（ソフトウェア、ないしエンジン）をインストールします。  
2.次に、VOICEVOXを起動します。サーバが立ちさえすればbatファイルで起動しても構いません。  
3.read_boy.pyのトークンを己のbotが持つトークンに書き換えます。server_id_testとtext_id_testも必要ならば書き換えてください。  
4.以下のコマンドを実行します。  
`PS path\to\this\program> python read_bot.py`  
5.音声チャンネルに入り、テキストチャンネルで.joinすれば入ってくれます。そうすると読み上げてくれます。さよならは.byeです。    
## 今後の展望  
現在合成した音声を逐次ファイルに書き出しているため、これをオンメモリでできればなと思います。  
ただ、特に策があるわけでもないです。FFmpegPCMAudioにBytesIOを渡しても上手く行かなかったんですね……。  
メンテも気が向いたらなので、割と放置すると思います。  

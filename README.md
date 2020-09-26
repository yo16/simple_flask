# simple_flask

## このアプリについて
このアプリは、[Flask](https://flask.palletsprojects.com/en/1.1.x/)でトップページにHello Worldって表示するだけのHTTPアプリです。
DockerContainerを使って作ったので、`.dockercontainer`というフォルダがありますが、それはなくても動きます。

## これを作った理由
理由は２つあります。
- １つは、VS CodeのDocker-Containersを試したかったということです。
- もう１つは、通常使う大きなアプリを作る上で、「基本はこれとして、大きなアプリは何が違うか」という比較対象として持っておきたかったことです。
  - 参考：[Explorer Flask](http://exploreflask.com/en/latest/index.html)

## 環境構築
```
pip install -r requirements.txt
```

## 起動方法
```
python ./simple_app/app.py
```

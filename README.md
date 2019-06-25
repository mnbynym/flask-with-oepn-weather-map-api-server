# flask-with-oepn-weather-map-api-server-example
FlaskでOpenWeatherMapにアクセスして天気情報を取得して返すWeb APIサーバーのサンプル

サーバーでPythonと関連ツールをインストール
`$ sudo yum -y install python3.x86_64 python3-pip.noarch python3-tools.x86_64`

pip3でFlaskおよび必要なパッケージをインストール
`$ sudo pip3 install flask flask-cors requests json`

サーバーの実行
Flaskはデフォルトで5000番ポートで起動するためサーバーのセキュリティ設定が必要

`$ export FLASK_APP=api_server.py`
`$ flask run --debugger --reload --host=0.0.0.0`

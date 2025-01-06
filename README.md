PostgreSQLとFlaskアプリケーションのセットアップ手順

1. DockerでPostgreSQLを起動

PostgreSQLをDockerで起動するために、以下のコマンドを実行します：

# PostgreSQLのDockerコンテナをバックグラウンドで起動
docker-compose up -d

起動確認

コンテナが正しく起動しているか確認します：

docker ps

不要なコンテナの削除

過去のDockerコンテナが原因でPostgreSQLが起動できない場合は、以下のコマンドで不要なコンテナを削除してください：

docker ps -a

削除コマンドの例：

docker rm -f [コンテナID]

2. Flaskアプリケーションのセットアップ

環境変数の設定

Flaskアプリケーションを指定するために、以下を実行します：

※Win環境
set FLASK_APP=app.py

※Mac環境
export FLASK_APP=app.py

データベースマイグレーションの初期化

マイグレーションの初期化

flask db init

マイグレーションスクリプトの作成

flask db migrate -m "Initial migration for Employ table"

マイグレーションの適用

flask db upgrade

アプリケーションの起動

アプリケーションを起動するには以下を実行します：

python app.py

3. Seedでデータを挿入

初期データを挿入するために、以下のコマンドを実行します：

python seed.py

このコマンドでデータベースに初期データが挿入されます。

4. よく使うコマンド一覧

コマンド

説明

docker-compose up -d

PostgreSQLのコンテナをバックグラウンドで起動

docker ps

起動中のDockerコンテナを確認

docker ps -a

全てのコンテナを確認

docker rm -f [コンテナID]

不要なコンテナを削除

flask db init

マイグレーションの初期化

flask db migrate -m ...

マイグレーションスクリプトを作成

flask db upgrade

マイグレーションをデータベースに適用

python app.py

アプリケーションを起動

python seed.py

初期データを挿入

これでアプリケーションのセットアップが完了です！必要に応じて各手順を実行してください。

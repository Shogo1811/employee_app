# ベースイメージをPythonに設定
FROM python:3.9

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係をインストールするため、requirements.txtをコピー
COPY requirements.txt /app/

# Pythonライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . /app/

# Flaskアプリケーションを実行
CMD ["flask", "run", "--host=0.0.0.0"]

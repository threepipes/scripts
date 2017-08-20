# scripts
PYTHONPATHに置く自分用の汎用的なスクリプト群

python3.6で動作確認済み

## notification

### requirements

- slackweb

### 概要

処理・作業が終わった後にリモートで通知を受け取るためのスクリプト

- slack: 自分用slackに通知を投げる

``` python
import notification as nf
nf.slack('test message') # slackにmessageが飛ぶ
```


## Connector/Database

### requirements

- mysql.connector

### 概要

mysql.connectorのラッパーライブラリ
Connector: 主にテーブルへの操作に関するSQLを実行する
Database: 具体テーブルを表す(Connectorのさらにラッパー的な)
基本的にはDatabaseをさらに継承したクラスを作成して利用

``` python
class FileDB(Database):
    table_name = 'File'
    key = 'file_name'
    column = [
        'file_name',
        'user_name',
    ]
    data_table = {
        'file_name': 'VARCHAR(50)',
        'user_name': 'VARCHAR(30)',
    }

    def __init__(self):
        super().__init__(self.table_name, self.key, self.column, self.data_table)

# Fileテーブルとの接続を確保
fdb = FileDB()

# Fileテーブルの作成
fdb.init_table()

# データの挿入
insert_data = {
    'file_name': 'foo.cpp',
    'user_name': 'threepipes'
}
fdb.insert(insert_data)

# データの表示
for data in fdb.select(where={'file_name': 'foo.cpp'}):
    print(data)
```

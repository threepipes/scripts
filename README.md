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

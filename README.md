# 経穴-LAB（リンクで使えるWebアプリ）

このアプリは **Streamlit** で動きます。  
最終的に「URLをタップするだけ」で使える形にするには、無料の公開先を使います。

---

## いちばん簡単：Streamlit Community Cloud（無料）

### 0) 事前に必要なもの
- GitHubアカウント（無料）
- Streamlit Cloudアカウント（無料：GitHubでサインイン可）

### 1) GitHubにアップロード（このフォルダ一式）
1. GitHubで **New repository**（新規）を作る
2. そのリポジトリに、以下4ファイルをアップする
   - app.py
   - requirements.txt
   - README.md
   - 経穴アプリ作成ファイル.xlsx

### 2) Streamlit Cloudで公開してURLを作る
1. Streamlit Cloud にログイン
2. **New app** を押す
3. Repository と **app.py** を選ぶ
4. Deploy（公開）

→ 数十秒でURLが発行されます。  
そのURLをクラスに共有すればOK（検索に出にくい・URLを知ってる人だけアクセス）。

---

## もう少し守りたい場合（任意）
「URLが漏れるのが心配」なら、合言葉入力を追加できます（後からでもOK）。

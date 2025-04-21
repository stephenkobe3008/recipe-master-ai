# recipe-master-ai

# 料理マイスター - AI搭載スマートレシピ生成器

料理マイスターは、AIを活用した高度なレシピ生成アプリケーションです。ユーザーの要望に合わせてパーソナライズされたレシピを提供します。

## 主な機能

- **カスタマイズ可能なレシピ生成**
  - 料理名を入力するだけで詳細なレシピを生成
  - 食事制限（ベジタリアン、ヴィーガン、グルテンフリーなど）の指定
  - 調理時間の指定（15分以内、30分以内など）
  - 難易度レベルの設定（初心者、中級者、上級者）

- **ユーザーフレンドリーな機能**
  - 料理名の提案機能
  - レシピ履歴の保存
  - 印刷機能
  - モダンでレスポンシブなデザイン

- **詳細なレシピ情報**
  - 材料リスト（人数分）
  - 段階的な調理手順
  - 調理のポイント
  - カロリー情報

## インストール方法

### 前提条件
- Python 3.9以上
- OpenAI APIキー

### セットアップ手順

1. リポジトリをクローン
   ```
   git clone https://github.com/your-username/recipe-master-ai.git
   cd recipe-master-ai
   ```

2. 仮想環境を作成して有効化（オプション）
   ```
   python -m venv venv
   source venv/bin/activate  # Linuxの場合
   venv\Scripts\activate  # Windowsの場合
   ```

3. 依存パッケージをインストール
   ```
   pip install -r requirements.txt
   ```

4. .envファイルを作成し、環境変数を設定
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

5. アプリケーションを実行
   ```
   python app.py
   ```

6. ブラウザで`http://localhost:5000`にアクセス

## Docker での実行

Dockerを使用して簡単に実行することもできます。

1. Dockerイメージをビルド
   ```
   docker build -t recipe-master-ai .
   ```

2. コンテナを実行
   ```
   docker run -p 5000:5000 --env-file .env recipe-master-ai
   ```

3. ブラウザで`http://localhost:5000`にアクセス

## 技術スタック

- **バックエンド**
  - Flask (Webフレームワーク)
  - OpenAI API (GPT-4)
  - Python-dotenv (環境変数管理)

- **フロントエンド**
  - HTML5 / CSS3 / JavaScript
  - Font Awesome (アイコン)

## 今後の開発予定

- 多言語サポート
- レシピの共有機能
- 料理完成イメージのAI生成
- 食材の在庫管理と買い物リスト生成
- 詳細な栄養情報

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

コントリビューションを歓迎します！Pull requestを送る前に、変更内容についてissueを作成してください。

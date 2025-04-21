import os
from dotenv import load_dotenv
import openai
from flask import Flask, render_template, request, jsonify, session
import json
import random

# 環境変数のロード
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret_key")

# レシピ履歴を保存するための辞書
RECIPE_HISTORY = {}

@app.route('/')
def home():
    # セッションIDがない場合は生成
    if 'user_id' not in session:
        session['user_id'] = str(random.randint(1000, 9999))
    
    # このユーザーの履歴を取得（なければ空リストを作成）
    user_id = session['user_id']
    if user_id not in RECIPE_HISTORY:
        RECIPE_HISTORY[user_id] = []
    
    return render_template('index.html', history=RECIPE_HISTORY[user_id])

@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    # リクエストから情報を取得
    dish_name = request.form.get('dish_name')
    dietary_restrictions = request.form.get('dietary_restrictions', '')
    cooking_time = request.form.get('cooking_time', '任意')
    difficulty = request.form.get('difficulty', '任意')
    
    # プロンプトの作成
    prompt = f"{dish_name}のレシピを教えてください。\n"
    if dietary_restrictions:
        prompt += f"dietary条件: {dietary_restrictions}\n"
    if cooking_time != '任意':
        prompt += f"調理時間: {cooking_time}\n"
    if difficulty != '任意':
        prompt += f"難易度: {difficulty}\n"
    
    prompt += "レシピは以下の形式で返してください：\n"
    prompt += "1. 材料（人数分）\n2. 調理手順\n3. 調理のポイント\n4. カロリー（概算）"
    
    try:
        # GPT-4を使用してレシピを生成
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "あなたは経験豊富な料理人で、詳細で分かりやすいレシピを提供します。"},
                {"role": "user", "content": prompt}
            ]
        )
        
        recipe_content = response['choices'][0]['message']['content']
        
        # セッションに保存
        if 'user_id' in session:
            user_id = session['user_id']
            if user_id not in RECIPE_HISTORY:
                RECIPE_HISTORY[user_id] = []
            
            # 履歴に追加（最新を先頭に）
            RECIPE_HISTORY[user_id].insert(0, {
                'dish_name': dish_name,
                'recipe': recipe_content,
                'dietary_restrictions': dietary_restrictions,
                'cooking_time': cooking_time,
                'difficulty': difficulty
            })
            
            # 履歴は最大10件まで保存
            if len(RECIPE_HISTORY[user_id]) > 10:
                RECIPE_HISTORY[user_id] = RECIPE_HISTORY[user_id][:10]
        
        return jsonify({
            "recipe": recipe_content,
            "success": True
        })
    
    except Exception as e:
        return jsonify({
            "error": str(e),
            "success": False
        })

@app.route('/clear_history', methods=['POST'])
def clear_history():
    if 'user_id' in session:
        user_id = session['user_id']
        if user_id in RECIPE_HISTORY:
            RECIPE_HISTORY[user_id] = []
    
    return jsonify({"success": True})

@app.route('/get_random_suggestion', methods=['GET'])
def get_random_suggestion():
    suggestions = [
        "ナポリタン", "カレーライス", "チキン南蛮", "肉じゃが", "餃子",
        "ラーメン", "オムライス", "ハンバーグ", "天ぷら", "味噌汁",
        "寿司", "焼きそば", "唐揚げ", "親子丼", "牛丼",
        "サラダ", "グラタン", "パスタ", "ピザ", "シチュー"
    ]
    
    return jsonify({
        "suggestion": random.choice(suggestions)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
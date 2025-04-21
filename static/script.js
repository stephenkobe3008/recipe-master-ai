document.addEventListener('DOMContentLoaded', function() {
    // 要素の参照を取得
    const recipeForm = document.getElementById('recipe-form');
    const dishNameInput = document.getElementById('dish_name');
    const dietaryRestrictionsSelect = document.getElementById('dietary_restrictions');
    const cookingTimeSelect = document.getElementById('cooking_time');
    const difficultySelect = document.getElementById('difficulty');
    const suggestionBtn = document.getElementById('suggestion-btn');
    const loadingIndicator = document.getElementById('loading');
    const resultSection = document.getElementById('result');
    const recipeTitleEl = document.getElementById('recipe-title');
    const recipeContentEl = document.getElementById('recipe');
    const printBtn = document.getElementById('print-btn');
    const clearHistoryBtn = document.getElementById('clear-history-btn');
    const historyList = document.getElementById('history-list');

    // レシピ生成フォームの送信イベント
    recipeForm.addEventListener('submit', function(event) {
        event.preventDefault();
        generateRecipe();
    });

    // 料理名の提案ボタンのクリックイベント
    suggestionBtn.addEventListener('click', function() {
        getRandomSuggestion();
    });

    // 印刷ボタンのクリックイベント
    if (printBtn) {
        printBtn.addEventListener('click', function() {
            window.print();
        });
    }

    // 履歴クリアボタンのクリックイベント
    if (clearHistoryBtn) {
        clearHistoryBtn.addEventListener('click', function() {
            clearHistory();
        });
    }

    // 履歴アイテムのクリックイベント
    if (historyList) {
        historyList.addEventListener('click', function(event) {
            const historyItem = event.target.closest('.history-item');
            if (historyItem) {
                const recipeData = historyItem.getAttribute('data-recipe');
                if (recipeData) {
                    displayRecipeFromHistory(historyItem.querySelector('.history-dish-name').textContent, JSON.parse(recipeData));
                }
            }
        });
    }

    // レシピ生成関数
    function generateRecipe() {
        // 入力値の取得
        const dishName = dishNameInput.value.trim();
        const dietaryRestrictions = dietaryRestrictionsSelect.value;
        const cookingTime = cookingTimeSelect.value;
        const difficulty = difficultySelect.value;

        // 入力チェック
        if (!dishName) {
            alert('料理名を入力してください');
            return;
        }

        // UI状態の更新
        loadingIndicator.classList.remove('hidden');
        resultSection.classList.add('hidden');

        // FormDataの作成
        const formData = new FormData();
        formData.append('dish_name', dishName);
        formData.append('dietary_restrictions', dietaryRestrictions);
        formData.append('cooking_time', cookingTime);
        formData.append('difficulty', difficulty);

        // APIリクエスト
        fetch('/generate_recipe', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            loadingIndicator.classList.add('hidden');
            
            if (data.success) {
                // レシピの表示
                displayRecipe(dishName, data.recipe);
                
                // ページの更新（履歴を反映するため）
                setTimeout(() => {
                    window.location.reload();
                }, 1000);
            } else {
                // エラー表示
                alert('エラーが発生しました: ' + data.error);
            }
        })
        .catch(error => {
            loadingIndicator.classList.add('hidden');
            alert('通信エラーが発生しました: ' + error);
            console.error('Error:', error);
        });
    }

    // レシピ表示関数
    function displayRecipe(dishName, recipeContent) {
        recipeTitleEl.textContent = dishName + 'のレシピ';
        
        // 改行を保持して表示
        recipeContentEl.innerHTML = formatRecipeContent(recipeContent);}})
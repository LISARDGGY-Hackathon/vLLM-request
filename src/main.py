import requests
import json



def main():
    api_url1 = "http://210.61.209.139:45014/v1/chat/completions"
    api_url2 = "http://210.61.209.139:45005/v1/chat/completions"

    # 依據您的慣用環境，假設使用者希望 AI 程式設計師的故事
    payload = {
        "model": "gpt-oss-120b", # 這裡的模型名稱通常是啟動服務時所載入的名稱
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a short story about a computer programmer who uses fish shell and vim."},
        ],
        "temperature": 0.7,
        "max_tokens": 512,
        "stream": True # 設定為 True 可啟用串流（Streaming）
    }

    try:
        response = requests.post(api_url1, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        response.raise_for_status() # 檢查是否有 HTTP 錯誤

        # 處理回應
        data = response.json()
        if data and 'choices' in data and data['choices']:
            print("Generated Text:")
            print(data['choices'][0]['message']['content'])
        else:
            print("Error: Invalid response format.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

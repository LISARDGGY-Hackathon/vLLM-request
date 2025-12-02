import requests
import json

from openai import OpenAI

def main():
    api_url1 = "http://210.61.209.139:45014/v1/chat/completions"
    api_url2 = "http://210.61.209.139:45005/v1/chat/completions"

    client = OpenAI(
        base_url=api_url1,
        api_key="your_api_key_here",
    )

    msg = "Hello, how are you?"

    try:
        response = client.chat.completions.create(
            model="gpt-oss-120b",
            messages=[{"role": "user", "content": msg}],
            max_tokens=100,
            temperature=0.7,
        )

        choice = response.choices[0]

        # 支援不同 SDK 回傳格式的擷取方法
        if hasattr(choice, "message") and getattr(choice.message, "content", None):
            generated_text = choice.message.content
        elif isinstance(choice, dict):
            generated_text = choice.get("message", {}).get("content") or choice.get("text")
        else:
            generated_text = getattr(choice, "text", None)

        print("Prompt:", msg)
        print("Generated Text:", generated_text)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()

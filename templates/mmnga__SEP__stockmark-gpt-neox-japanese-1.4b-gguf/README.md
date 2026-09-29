---
license: mit
language:
- ja
tags:
- gpt-neox
---
# stockmark-gpt-neox-japanese-1.4b-gguf
[stockmarkさんが公開しているgpt-neox-japanese-1.4b](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b)のggufフォーマット変換版です。

注意:こちらはブランチで試用になります。llama.cpp本家にgptneoxが実装された時に、このggufファイルが使用できない可能性があります。

***[GitHubリポジトリの readme はこちら](https://github.com/mmnga/llama.cpp/tree/mmnga-dev)***

## Usage (試用)

```
git clone --branch mmnga-dev https://github.com/mmnga/llama.cpp.git
cd llama.cpp
make -j
./main -m 'stockmark-gpt-neox-japanese-1.4b-q4_0.gguf' -n 128 -p '吾輩は猫である。名前は実を言うと、'  --top_p 0.9 --temp 0.7 --repeat-penalty 1.1
```

**CUBLAS**
```
LLAMA_CUBLAS=1 make -j
./main -m 'stockmark-gpt-neox-japanese-1.4b-q4_0.gguf' -n 128 -p '吾輩は猫である。名前は実を言うと、' -ngl 24
```
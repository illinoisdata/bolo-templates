---
license: cc-by-sa-4.0
language:
- ja
tags:
- gpt-neox
---
# cyberagent-open-calm-1b-gguf
[cyberagentさんが公開しているopen-calm-1b](https://huggingface.co/cyberagent/open-calm-1b)のggufフォーマット変換版です。  

他モデルはこちら  
[mmnga/cyberagent-open-calm-7b-gguf](https://huggingface.co/mmnga/cyberagent-open-calm-7b-gguf)  
[mmnga/cyberagent-open-calm-3b-gguf](https://huggingface.co/mmnga/cyberagent-open-calm-3b-gguf)  
[mmnga/cyberagent-open-calm-1b-gguf](https://huggingface.co/mmnga/cyberagent-open-calm-1b-gguf)  

注意:こちらはブランチで試用になります。llama.cpp本家にgptneoxが実装された時に、このggufファイルが使用できない可能性があります。

***[GitHubリポジトリの readme はこちら](https://github.com/mmnga/llama.cpp/tree/mmnga-dev)***


## Usage (試用)

```
git clone --branch mmnga-dev https://github.com/mmnga/llama.cpp.git
cd llama.cpp
make -j
./main -m 'cyberagent-open-calm-1b-q4_0.gguf' -n 128 -p '吾輩は猫である。名前は実を言うと、'  --top_p 0.9 --temp 0.7 --repeat-penalty 1.1
```

**CUBLAS**
```
LLAMA_CUBLAS=1 make -j
./main -m 'cyberagent-open-calm-1b-q4_0.gguf' -n 128 -p '吾輩は猫である。名前は実を言うと、' -ngl 32
```
---
license: other
license_name: yandexgpt-5-lite-8b
license_link: LICENSE
language:
- ru
- en
---
# YandexGPT-5-Lite-Instruct-GGUF
Квантизованная версия YandexGPT 5 Lite 8B Instruct. Информация о модели доступна в основном репозитории: [YandexGPT-5-Lite-8B-instruct](https://huggingface.co/yandex/YandexGPT-5-Lite-8B-instruct).

**UPD**: Мы обновили `.gguf` файл в изначальном репозитории на наиболее близкий по качеству к оригинальной модели.

## llama.cpp
Для начала нужно собрать [llama.cpp](https://github.com/ggml-org/llama.cpp) (или обновить, если уже есть):
```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -B build
cmake --build build --config Release
cd ..
```
Можно ускорить сборку если позволяют ресурсы: `cmake --build build --config Release -j 10`

Запуск модели в интерактивном режиме:
```bash
llama.cpp/build/bin/llama-cli -m YandexGPT-5-Lite-8B-instruct-Q4_K_M.gguf
```
Мы рекомендуем использовать интерактивный режим только для ознакомления с моделью.

Запуск сервера:
```bash
llama.cpp/build/bin/llama-server -m YandexGPT-5-Lite-8B-instruct-Q4_K_M.gguf -c 32768
```
Если позволяют ресурсы, можно ускорить инференс, добавив `-t 10`.

## Ollama
Запуск модели в интерактивном режиме:
```bash
ollama run yandex/YandexGPT-5-Lite-8B-instruct-GGUF
```
Мы рекомендуем использовать интерактивный режим только для ознакомления с моделью.

## Особенности шаблона
Мы используем нестандартный шаблон диалога — модель обучена генерировать только одну реплику после последовательности `Ассистент:[SEP]`, завершая её токеном `</s>`. При этом диалог в промпте может быть любой длины.

Это приводит к тому, что в интерактивном режиме модель может выдавать результаты, отличающиеся от вызова модели в режиме генерации на фиксированном диалоге. Поэтому мы рекомендуем использовать интерактивный режим только для ознакомления с моделью.
---
license: apache-2.0
language:
- zh
tags:
- token-classification
---

[中文](#中文版本) | [English](#english-version)

## 中文版本

這是一個**繁體中文**命名實體識別 (NER) 模型，可用於提取**商品名稱**中的各種屬性，例如品牌、名稱、顏色等。

關於如何使用模型，請參考 [Product-Name-NER-for-EE5327701](https://github.com/clw8998/Product-Name-NER-for-EE5327701)。

關於各種屬性的標註規則，以及模型在各個屬性的 F1-score，請參考下表：

| 編號 | 標籤屬性            | 說明                                                                                          | F1-score |
|-----|-------------------|---------------------------------------------------------------------------------------------|-------|
| 1   | **品牌**            | 商品品牌名稱，如 華碩、LG                                                                     | 0.8770 |
| 2   | **名稱**        | 商品中所有的“產品系列”，以及商人為了特殊目的所特別額外創造出的商品名稱，不包含特殊主題或是產品類型，不含廣告詞。如 iPhone 12、ROG 3060Ti | 0.5941 |
| 3   | **產品**        | 實際產品名稱(類型)。如 電腦、滑鼠、鍵盤、螢幕、玩具、餅乾、衛生紙                                    | 0.8001 |
| 4   | **產品序號**        | 商品序號，該產品所擁有的唯一數字字母組合序號，不含系列名。                                                | 0.8443 |
| 5   | **顏色**            | 顏色資訊，包含化妝品以及明亮色調。如 花朵紅、藍色系、晶亮                                                   | 0.8898 |
| 6   | **材質**            | 產品的製造材料，請注意，不是產品成分。如 木製、PVC 材質、304 不銹鋼                                        | 0.7810 |
| 7   | **對象與族群**        | 適用的人與動物的族群。如 新生兒、寵物用、高齡族群                                                            | 0.8755 |
| 8   | **適用物體、事件與場所** | 適用的物品、事件、場所。如 手部用、騎車用、廚房用                                                     | 0.7614 |
| 9   | **特殊主題**        | 產品附有特殊主題或為創造作。如 航海王、J.K. Rowling                                                  | 0.4979 |
| 10  | **形狀**            | 商品形狀及其外觀詞彙。如 圓形、鈕扣形、可愛熊、無袖、長筒、窄邊框                                             | 0.7793 |
| 11  | **圖案**            | 產品上的圖案，如 圓形、螺旋形圖案                                                                   | 0.5731 |
| 12  | **尺寸**            | 商品大小，常以數字和特殊規格形式出現。如 120x80x10cm（長寬高）、XL、ATX                                      | 0.8420 |
| 13  | **重量**            | 商品重量，常以數字和特殊規格形式出現。如 10g、極輕                                                    | 0.9105 |
| 14  | **容量**            | 商品容量，常以數字和特殊規格形式出現。如 128G（電腦）、大容量                                            | 0.9220 |
| 15  | **包裝組合**        | 產品的包裝方式、組合方式。如 10 入、10g/包、鍵盤滑鼠組合、送電池                                             | 0.7478 |
| 16  | **功能與規格**        | 產品的用途與特殊規格，如 USB 3.0、陽光防曬、防水                                                        | 0.7960 |
| 17  | **Macro F1-score**  |                          | 0.7807 |

## English Version

This is a **Traditional Chinese** Named Entity Recognition (NER) model designed for extracting various attributes from **product names**, such as brand, name, color, etc.

For details on how to use the model, please refer to [Product-Name-NER-for-EE5327701](https://github.com/clw8998/Product-Name-NER-for-EE5327701).

The following table provides the annotation rules for various attributes, along with the F1-scores for each attribute:

| No.  | Attribute (English)           | Description                                                                                     | F1-score |
|------|-------------------------------|-------------------------------------------------------------------------------------------------|----------|
| 1    | **品牌 (brand)**               | The product's brand name, such as Asus, LG                                                      | 0.8770   |
| 2    | **名稱 (name)**                | The "product series" or name created by the seller for special purposes. Excludes special topics or product types. Does not include advertisements. For example, iPhone 12, ROG 3060Ti | 0.5941   |
| 3    | **產品 (product)**             | The actual product name (type), such as computer, mouse, keyboard, monitor, toy, snack, tissue   | 0.8001   |
| 4    | **產品序號 (product serial number)** | The product's unique alphanumeric code, excluding series names                                  | 0.8443   |
| 5    | **顏色 (color)**               | The color information, including cosmetics and brightness. For example, floral red, blue, crystal | 0.8898   |
| 6    | **材質 (material)**            | The material used in the product, not ingredients. For example, wood, PVC, 304 stainless steel  | 0.7810   |
| 7    | **對象與族群 (target group)**   | The target audience, such as newborns, pets, seniors                                            | 0.8755   |
| 8    | **適用物體、事件與場所 (applicable item, event, or place)** | The item, event, or place the product is applicable for. For example, hand-use, cycling, kitchen | 0.7614   |
| 9    | **特殊主題 (special topic)**    | Special themes or brands. For example, One Piece, J.K. Rowling                                  | 0.4979   |
| 10   | **形狀 (shape)**               | The product's shape and appearance description. For example, round, button shape, bear shape     | 0.7793   |
| 11   | **圖案 (pattern)**             | Patterns on the product, such as round or spiral patterns                                       | 0.5731   |
| 12   | **尺寸 (size)**                | Product size, often in numerical or specific form. For example, 120x80x10cm (LxWxH), XL, ATX    | 0.8420   |
| 13   | **重量 (weight)**              | Product weight, often in numerical or specific form. For example, 10g, ultra-light               | 0.9105   |
| 14   | **容量 (capacity)**            | Product capacity, often in numerical or specific form. For example, 128GB (computer), large capacity | 0.9220   |
| 15   | **包裝組合 (package combination)** | The product's packaging method or combination. For example, 10 pieces, 10g/package, keyboard & mouse combo, battery included | 0.7478   |
| 16   | **功能與規格 (function & specifications)** | The product's functions and special specifications. For example, USB3.0, sun protection, waterproof | 0.7960   |
| 17   | **Macro F1-score**             | Overall F1-score                                                                                | 0.7807   |
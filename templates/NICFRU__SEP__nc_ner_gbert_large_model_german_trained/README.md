# nc_ner_gbert_large_model_german_trained

Dieses Modell ist eine feinjustierte Variante von `deepset/gbert-large` und wurde auf dem `german-ler`-Datensatz mit **feingranularen juristischen Entitäten** (19 Labels) trainiert.  
Es dient dem Vergleich mit kleineren BERT-Modellen hinsichtlich Performance und Effizienz im juristischen NER-Kontext.

## Evaluationsergebnisse

- **F1-Score (micro avg)**: 0.9401  
- **Precision (micro avg)**: 0.9218  
- **Recall (micro avg)**: 0.9592  
- **Loss**: 0.0139  

### Klassenweise Metriken (fine level)

| Klasse | Bedeutung         | Coarse | Coarse Bedeutung     | Precision | Recall  | F1-Score | Support |
|--------|-------------------|--------|-----------------------|-----------|---------|----------|---------|
| PER    | Person            | PER    | Person                | 0.9086    | 0.9191  | 0.9138   | 173     |
| RR     | Judge             | PER    | Person                | 0.9861    | 1.0000  | 0.9930   | 142     |
| AN     | Lawyer            | PER    | Person                | 1.0000    | 0.8333  | 0.9091   | 6       |
| LD     | Country           | LOC    | Location              | 0.9858    | 0.9329  | 0.9586   | 149     |
| ST     | City              | LOC    | Location              | 0.7639    | 0.8594  | 0.8088   | 64      |
| STR    | Street            | LOC    | Location              | 0.9286    | 0.8667  | 0.8966   | 15      |
| LDS    | Landscape         | LOC    | Location              | 0.5278    | 0.8636  | 0.6552   | 22      |
| ORG    | Organization      | ORG    | Organization          | 0.9204    | 0.9204  | 0.9204   | 113     |
| UN     | Company           | ORG    | Organization          | 0.9358    | 0.9444  | 0.9401   | 108     |
| INN    | Institution       | ORG    | Organization          | 0.9241    | 0.9324  | 0.9283   | 222     |
| GRT    | Court             | ORG    | Organization          | 0.9748    | 0.9626  | 0.9687   | 321     |
| MRK    | Brand             | ORG    | Organization          | 0.7632    | 0.9063  | 0.8286   | 32      |
| GS     | Law               | NRM    | Legal norm            | 0.9777    | 0.9890  | 0.9833   | 1818    |
| VO     | Ordinance         | NRM    | Legal norm            | 0.9048    | 0.8028  | 0.8507   | 71      |
| EUN    | EU legal norm     | NRM    | Legal norm            | 0.9045    | 0.9667  | 0.9251   | 150     |
| VS     | Regulation        | REG    | Case-by-c. regul.     | 0.7794    | 0.8281  | 0.8030   | 64      |
| VT     | Contract          | REG    | Case-by-c. regul.     | 0.8942    | 0.9621  | 0.9269   | 290     |
| RS     | Court decision    | RS     | Court decision        | 0.9104    | 0.9799  | 0.9439   | 1245    |
| LIT    | Legal literature  | LIT    | Legal literature      | 0.7337    | 0.8599  | 0.7918   | 314     |

### Durchschnittswerte:

- **Macro avg (F1)**: 0.8919  
- **Weighted avg (F1)**: 0.9413  

---

## Hinweis zur Metrikwahl

Für die Gesamteinschätzung wird der **micro-average F1-Score** verwendet, da hier **alle Vorhersagen gleich gewichtet** werden – unabhängig von der Klassengröße. Diese Methode ist besonders geeignet für sequenzbasierte Aufgaben wie NER, bei denen jede Token-Entscheidung den gleichen Einfluss auf die Gesamtleistung hat.

### Überblick über die Metriktypen:

- **Micro average**: Gesamtanzahl aller True Positives, False Positives und False Negatives → *alle Klassenbeiträge gleich gewichtet*  
- **Macro average**: Durchschnitt der Metriken über alle Klassen → *alle Klassen gleich wichtig*, unabhängig vom Support  
- **Weighted average**: Durchschnitt über alle Klassen, *gewichtet nach Klassengröße* → häufige Klassen haben mehr Einfluss  


## Trainingskonfiguration

- **Modell**: `deepset/gbert-large`  
- **Datensatz**: `german-ler` (BIO-annotiert, 19 Feinlabels)  
- **Trainingsepochen**: 6  
- **Batchgröße**: 32  
- **Lernrate**: 2e-5  
- **Weight Decay**: 0.01  
- **Evaluation alle**: 200 Schritte  
- **Selektion nach**: F1-Score  
- **Early Stopping**: aktiviert, um Überanpassung zu vermeiden  

---

## Nutzung

Das Modell eignet sich für juristische NER-Anwendungen, bei denen eine **detaillierte Extraktion juristisch relevanter Entitäten** aus deutschsprachigen Rechtstexten gefragt ist – z. B. in LegalTech-Systemen, automatisierten Schriftsatzanalysen oder für juristische Wissensgraphen.

### Training results

| loss | epoch | step | eval_loss | eval_f1 | eval_precision | eval_recall |
| --- | --- | --- | --- | --- | --- | --- |
| 0.6156 | 0.029958058717795086 | 50 | nan | nan | nan | nan |
| 0.131 | 0.05991611743559017 | 100 | nan | nan | nan | nan |
| 0.0901 | 0.08987417615338526 | 150 | nan | nan | nan | nan |
| 0.0647 | 0.11983223487118035 | 200 | nan | nan | nan | nan |
| nan | 0.11983223487118035 | 200 | 0.05919138714671135 | 0.732017823042648 | 0.6748826291079812 | 0.799721835883171 |
| 0.0684 | 0.14979029358897544 | 250 | nan | nan | nan | nan |
| 0.0574 | 0.17974835230677053 | 300 | nan | nan | nan | nan |
| 0.0581 | 0.2097064110245656 | 350 | nan | nan | nan | nan |
| 0.0529 | 0.2396644697423607 | 400 | nan | nan | nan | nan |
| nan | 0.2396644697423607 | 400 | 0.05266263708472252 | 0.6787610619469026 | 0.6119355353438647 | 0.7619709914563878 |
| 0.0468 | 0.2696225284601558 | 450 | nan | nan | nan | nan |
| 0.0477 | 0.2995805871779509 | 500 | nan | nan | nan | nan |
| 0.0486 | 0.32953864589574594 | 550 | nan | nan | nan | nan |
| 0.0332 | 0.35949670461354105 | 600 | nan | nan | nan | nan |
| nan | 0.35949670461354105 | 600 | 0.040142327547073364 | 0.8362893490574796 | 0.7850418410041841 | 0.8946950129147626 |
| 0.0426 | 0.3894547633313361 | 650 | nan | nan | nan | nan |
| 0.04 | 0.4194128220491312 | 700 | nan | nan | nan | nan |
| 0.0329 | 0.44937088076692633 | 750 | nan | nan | nan | nan |
| 0.0428 | 0.4793289394847214 | 800 | nan | nan | nan | nan |
| nan | 0.4793289394847214 | 800 | 0.037605926394462585 | 0.7773444753946147 | 0.7296496426703852 | 0.8317107093184979 |
| 0.0358 | 0.5092869982025164 | 850 | nan | nan | nan | nan |
| 0.0351 | 0.5392450569203115 | 900 | nan | nan | nan | nan |
| 0.0332 | 0.5692031156381067 | 950 | nan | nan | nan | nan |
| 0.0307 | 0.5991611743559018 | 1000 | nan | nan | nan | nan |
| nan | 0.5991611743559018 | 1000 | 0.029554303735494614 | 0.8686291321329903 | 0.8343704245973645 | 0.9058215775879197 |
| 0.0346 | 0.6291192330736968 | 1050 | nan | nan | nan | nan |
| 0.0242 | 0.6590772917914919 | 1100 | nan | nan | nan | nan |
| 0.0243 | 0.689035350509287 | 1150 | nan | nan | nan | nan |
| 0.0332 | 0.7189934092270821 | 1200 | nan | nan | nan | nan |
| nan | 0.7189934092270821 | 1200 | 0.028585752472281456 | 0.8749881167411351 | 0.8388625592417062 | 0.9143651897476655 |
| 0.0378 | 0.7489514679448772 | 1250 | nan | nan | nan | nan |
| 0.0246 | 0.7789095266626722 | 1300 | nan | nan | nan | nan |
| 0.0342 | 0.8088675853804673 | 1350 | nan | nan | nan | nan |
| 0.0291 | 0.8388256440982624 | 1400 | nan | nan | nan | nan |
| nan | 0.8388256440982624 | 1400 | 0.02948427014052868 | 0.8413112311417397 | 0.7917616126205084 | 0.8974766540830519 |
| 0.0406 | 0.8687837028160575 | 1450 | nan | nan | nan | nan |
| 0.0372 | 0.8987417615338527 | 1500 | nan | nan | nan | nan |
| 0.025 | 0.9286998202516477 | 1550 | nan | nan | nan | nan |
| 0.0264 | 0.9586578789694428 | 1600 | nan | nan | nan | nan |
| nan | 0.9586578789694428 | 1600 | 0.025683972984552383 | 0.8732658417697787 | 0.8266193433895297 | 0.9254917544208225 |
| 0.03 | 0.9886159376872379 | 1650 | nan | nan | nan | nan |
| 0.0205 | 1.0185739964050329 | 1700 | nan | nan | nan | nan |
| 0.0145 | 1.048532055122828 | 1750 | nan | nan | nan | nan |
| 0.0139 | 1.078490113840623 | 1800 | nan | nan | nan | nan |
| nan | 1.078490113840623 | 1800 | 0.02673141472041607 | 0.8959493184872336 | 0.8666666666666667 | 0.9272799523147228 |
| 0.0163 | 1.1084481725584183 | 1850 | nan | nan | nan | nan |
| 0.0239 | 1.1384062312762133 | 1900 | nan | nan | nan | nan |
| 0.0156 | 1.1683642899940083 | 1950 | nan | nan | nan | nan |
| 0.0178 | 1.1983223487118035 | 2000 | nan | nan | nan | nan |
| nan | 1.1983223487118035 | 2000 | 0.02600107342004776 | 0.8435423682533904 | 0.7783003023177696 | 0.9207232267037552 |
| 0.0157 | 1.2282804074295985 | 2050 | nan | nan | nan | nan |
| 0.0149 | 1.2582384661473935 | 2100 | nan | nan | nan | nan |
| 0.0227 | 1.2881965248651888 | 2150 | nan | nan | nan | nan |
| 0.0192 | 1.3181545835829838 | 2200 | nan | nan | nan | nan |
| nan | 1.3181545835829838 | 2200 | 0.024343570694327354 | 0.8778073848496383 | 0.8423744292237443 | 0.9163520762964434 |
| 0.0152 | 1.348112642300779 | 2250 | nan | nan | nan | nan |
| 0.0205 | 1.378070701018574 | 2300 | nan | nan | nan | nan |
| 0.024 | 1.4080287597363692 | 2350 | nan | nan | nan | nan |
| 0.0322 | 1.4379868184541642 | 2400 | nan | nan | nan | nan |
| nan | 1.4379868184541642 | 2400 | 0.035087354481220245 | 0.6913349741152508 | 0.6034074074074074 | 0.8092588913173058 |
| 0.0201 | 1.4679448771719592 | 2450 | nan | nan | nan | nan |
| 0.0224 | 1.4979029358897544 | 2500 | nan | nan | nan | nan |
| 0.0425 | 1.5278609946075494 | 2550 | nan | nan | nan | nan |
| 0.0474 | 1.5578190533253444 | 2600 | nan | nan | nan | nan |
| nan | 1.5578190533253444 | 2600 | 0.031948916614055634 | 0.7382958394857986 | 0.6558641975308642 | 0.8444267832306775 |
| 0.021 | 1.5877771120431396 | 2650 | nan | nan | nan | nan |
| 0.0228 | 1.6177351707609346 | 2700 | nan | nan | nan | nan |
| 0.0237 | 1.6476932294787296 | 2750 | nan | nan | nan | nan |
| 0.0224 | 1.6776512881965249 | 2800 | nan | nan | nan | nan |
| nan | 1.6776512881965249 | 2800 | 0.029736803844571114 | 0.7946308724832215 | 0.7228915662650602 | 0.8821776276574608 |
| 0.0261 | 1.70760934691432 | 2850 | nan | nan | nan | nan |
| 0.021 | 1.737567405632115 | 2900 | nan | nan | nan | nan |
| 0.0174 | 1.76752546434991 | 2950 | nan | nan | nan | nan |
| 0.021 | 1.7974835230677053 | 3000 | nan | nan | nan | nan |
| nan | 1.7974835230677053 | 3000 | 0.02513810805976391 | 0.798989078436682 | 0.7320542507442938 | 0.8793959864891715 |
| 0.0169 | 1.8274415817855003 | 3050 | nan | nan | nan | nan |
| 0.0221 | 1.8573996405032953 | 3100 | nan | nan | nan | nan |
| 0.0217 | 1.8873576992210905 | 3150 | nan | nan | nan | nan |
| 0.0174 | 1.9173157579388855 | 3200 | nan | nan | nan | nan |
| nan | 1.9173157579388855 | 3200 | 0.023385705426335335 | 0.8838001514004542 | 0.8437217705510388 | 0.9278760182793563 |
| 0.0204 | 1.9472738166566805 | 3250 | nan | nan | nan | nan |
| 0.0219 | 1.9772318753744758 | 3300 | nan | nan | nan | nan |
| 0.0089 | 2.007189934092271 | 3350 | nan | nan | nan | nan |
| 0.0082 | 2.0371479928100658 | 3400 | nan | nan | nan | nan |
| nan | 2.0371479928100658 | 3400 | 0.019637661054730415 | 0.9227039084472893 | 0.9012883668056082 | 0.9451619312537254 |
| 0.0083 | 2.067106051527861 | 3450 | nan | nan | nan | nan |
| 0.0092 | 2.097064110245656 | 3500 | nan | nan | nan | nan |
| 0.0065 | 2.127022168963451 | 3550 | nan | nan | nan | nan |
| 0.0078 | 2.156980227681246 | 3600 | nan | nan | nan | nan |
| nan | 2.156980227681246 | 3600 | 0.020610226318240166 | 0.9047120418848168 | 0.868421052631579 | 0.9441684879793364 |
| 0.0092 | 2.1869382863990414 | 3650 | nan | nan | nan | nan |
| 0.0057 | 2.2168963451168366 | 3700 | nan | nan | nan | nan |
| 0.0061 | 2.2468544038346314 | 3750 | nan | nan | nan | nan |
| 0.0084 | 2.2768124625524266 | 3800 | nan | nan | nan | nan |
| nan | 2.2768124625524266 | 3800 | 0.02074912004172802 | 0.9234182098765432 | 0.897282099343955 | 0.9511225909000596 |
| 0.0125 | 2.306770521270222 | 3850 | nan | nan | nan | nan |
| 0.0123 | 2.3367285799880166 | 3900 | nan | nan | nan | nan |
| 0.011 | 2.366686638705812 | 3950 | nan | nan | nan | nan |
| 0.0067 | 2.396644697423607 | 4000 | nan | nan | nan | nan |
| nan | 2.396644697423607 | 4000 | 0.02030772715806961 | 0.9292713689725429 | 0.9080394387561623 | 0.9515199682098152 |
| 0.0082 | 2.426602756141402 | 4050 | nan | nan | nan | nan |
| 0.0091 | 2.456560814859197 | 4100 | nan | nan | nan | nan |
| 0.0074 | 2.4865188735769923 | 4150 | nan | nan | nan | nan |
| 0.0113 | 2.516476932294787 | 4200 | nan | nan | nan | nan |
| nan | 2.516476932294787 | 4200 | 0.021802891045808792 | 0.9147645189251661 | 0.8876635514018691 | 0.9435724220147029 |
| 0.0115 | 2.5464349910125823 | 4250 | nan | nan | nan | nan |
| 0.0182 | 2.5763930497303775 | 4300 | nan | nan | nan | nan |
| 0.0094 | 2.6063511084481723 | 4350 | nan | nan | nan | nan |
| 0.0118 | 2.6363091671659675 | 4400 | nan | nan | nan | nan |
| nan | 2.6363091671659675 | 4400 | 0.02236076258122921 | 0.9153225806451613 | 0.8855656697009102 | 0.9471488178025035 |
| 0.0098 | 2.6662672258837627 | 4450 | nan | nan | nan | nan |
| 0.0079 | 2.696225284601558 | 4500 | nan | nan | nan | nan |
| 0.0084 | 2.7261833433193527 | 4550 | nan | nan | nan | nan |
| 0.0065 | 2.756141402037148 | 4600 | nan | nan | nan | nan |
| nan | 2.756141402037148 | 4600 | 0.022946279495954514 | 0.9190857363294436 | 0.8929910044977512 | 0.9467514404927478 |
| 0.0069 | 2.786099460754943 | 4650 | nan | nan | nan | nan |
| 0.0086 | 2.8160575194727384 | 4700 | nan | nan | nan | nan |
| 0.0086 | 2.846015578190533 | 4750 | nan | nan | nan | nan |
| 0.01 | 2.8759736369083284 | 4800 | nan | nan | nan | nan |
| nan | 2.8759736369083284 | 4800 | 0.02151244319975376 | 0.8928809048569528 | 0.8558673469387755 | 0.933240611961057 |
| 0.0076 | 2.9059316956261236 | 4850 | nan | nan | nan | nan |
| 0.0087 | 2.9358897543439184 | 4900 | nan | nan | nan | nan |
| 0.0112 | 2.9658478130617136 | 4950 | nan | nan | nan | nan |
| 0.0104 | 2.995805871779509 | 5000 | nan | nan | nan | nan |
| nan | 2.995805871779509 | 5000 | 0.023878246545791626 | 0.8814202981106997 | 0.844 | 0.9223127359427776 |
| 0.0096 | 3.0257639304973036 | 5050 | nan | nan | nan | nan |
| 0.0066 | 3.055721989215099 | 5100 | nan | nan | nan | nan |
| 0.007 | 3.085680047932894 | 5150 | nan | nan | nan | nan |
| 0.0073 | 3.115638106650689 | 5200 | nan | nan | nan | nan |
| nan | 3.115638106650689 | 5200 | 0.021819742396473885 | 0.9022657450076804 | 0.8729333085639978 | 0.9336379892708127 |
| 0.0049 | 3.145596165368484 | 5250 | nan | nan | nan | nan |
| 0.0045 | 3.1755542240862793 | 5300 | nan | nan | nan | nan |
| 0.0068 | 3.205512282804074 | 5350 | nan | nan | nan | nan |
| 0.0074 | 3.2354703415218693 | 5400 | nan | nan | nan | nan |
| nan | 3.2354703415218693 | 5400 | 0.023947738111019135 | 0.8841031453669594 | 0.8426359380626576 | 0.9298629048281343 |
| 0.0063 | 3.2654284002396645 | 5450 | nan | nan | nan | nan |
| 0.0059 | 3.2953864589574597 | 5500 | nan | nan | nan | nan |
| 0.0067 | 3.3253445176752545 | 5550 | nan | nan | nan | nan |
| 0.0048 | 3.3553025763930497 | 5600 | nan | nan | nan | nan |
| nan | 3.3553025763930497 | 5600 | 0.022567927837371826 | 0.8971162082421242 | 0.860979174278407 | 0.9364196304391019 |
| nan | 3.3553025763930497 | 5600 | nan | nan | nan | nan |


## Framework versions
- Transformers: 2.3.0
- Pytorch: (siehe Umgebung)
- Datasets: (siehe Umgebung)
- Tokenizers: (siehe Umgebung)
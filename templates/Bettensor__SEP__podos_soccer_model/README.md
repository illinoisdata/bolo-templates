---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
{}
---

# Podos v1 Baseline

Podos is a small baseline transformer model for soccer match prediction.

## Model Details

### Model Description

- **Developed by:** Bettensor | Nickel5
- **Model type:** PyTorch Transformer
- **Parameters** 276K parameters

## Uses

Podos predicts soccer match outcomes based on 23 input parameters including sportsbook odds, recent team performance, win/loss streak, and more.
### Direct Use

For direct use, download the source pytorch class, label_encoder (optional), and load the model. <p><code>PodosTransformer.from_pretrained("Bettensor/podos_soccer_model")</code></p>
The label encoder contains the id mappings to all teams the model was trained on. 
Ensure you have Torch installed with:
<p><code>pip install torch</code></p>
scikit-learn version 1.4.2 if you want to use the label_encoder:
<p><code>pip install scikit-learn==1.4.2</code></p>
newer versions of sklearn may work but are untested.

You also need HuggingFace_hub and safetensors, install with:
<p><code>pip install huggingface_hub</code></p>
<p><code>pip install safetensors</code></p>
  
model expects 23 parameters for input, with team names mapped as ids:
- HS - Home shots
- AS - Away shots
- HST - Home shots on target
- AST - Away shots on target
- HC - Home corners
- AC - Away corners
- HO - Home offsides
- AO - Away offsides
- HY - Home yellow card
- AY - Away yellow cards
- HR - Home red cards
- AR - Away red cards
- oddsH - Home win odds
- oddsD - Draw odds
- oddsA - Away win odds
- home_encoded - Home team id
- away_encoded - Away team id
- WinStreakHome - Home win streak
- LossStreakHome - home loss streak
- WinStreakAway - Away win streak
- LossStreakAway - Away loss streak
- HomeTeamForm - Home team recent performance 
- AwayTeamForm - Away team recent performance

The label_encoder currently contains mappings for 569 unique teams

### Downstream Use

Model is available to use with Bettensor at https://github.com/Bettensor/bettensor

## Bias, Risks, and Limitations

podos v1 presents some home team bias, and may provide overconfident scores to its predicted outcome.

### Recommendations/Future work
- reduce bias by encoding home field advantage
- more teams and leagues, especially with more rigorous performance metrics
- Additional layers for larger input size
- team embedding layers
- individual player performance

### Training Data
Model was trained on 100,000 games with 569 individual teams.

- data source: https://www.football-data.co.uk/downloadm.php

## Model Card Authors

qucat | Nickel5

## Model Card Contact
www.nickel5.com
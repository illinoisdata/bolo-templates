---
{}
---

This repo contains an in-house tuned LLaMA-7b based on the [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) dataset, for only research use.

Quantitative evaluation on machine translation and qualitative comparison on general abilities can be found at [alpaca-mt](https://github.com/wxjiao/alpaca-mt).



<div class="max-w-full overflow-auto">
<table>
<tr>
<th colspan="12" align="center">Translation Performance of LLMs on Flores <a style="font-weight:bold" href=https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator>Subsets</a>.
</tr>
<tr align="center" style="font-weight:bold">
<td>Direction</td>
<td colspan="2">De-En</td>
<td colspan="2">En-De</td>
<td colspan="2">Zh-En</td>
<td colspan="2">En-Zh</td>
</tr>
<tr align="center" style="font-weight:bold">
<td>Metric</td>
<td>BLEU</td>
<td>COMET</td>
<td>BLEU</td>
<td>COMET</td>
<td>BLEU</td>
<td>COMET</td>
<td>BLEU</td>
<td>COMET</td>
</tr>
<tr align="center">
<td>Google</td>
<td>45.04</td>
<td>0.8879</td>
<td>41.16</td>
<td>0.8861</td>
<td style="font-weight:bold">31.66</td>
<td style="font-weight:bold">0.8771</td>
<td>43.58</td>
<td style="font-weight:bold">0.8842</td>
</tr>
<tr align="center">
<td>DeepL</td>
<td style="font-weight:bold">49.23</td>
<td style="font-weight:bold">0.8970</td>
<td>41.46</td>
<td>0.8903</td>
<td>31.22</td>
<td>0.8739</td>
<td style="font-weight:bold">44.31</td>
<td>0.8811</td>
</tr>
<tr align="center">
<td>ChatGPT</td>
<td>43.71</td>
<td>0.8910</td>
<td>38.87</td>
<td>0.8814</td>
<td>24.73</td>
<td>0.8581</td>
<td>38.27</td>
<td>0.8699</td>
</tr>
<tr align="center">
<td>GPT-4</td>
<td>46.00</td>
<td>0.8931</td>
<td style="font-weight:bold">45.73</td>
<td style="font-weight:bold">0.8928</td>
<td>28.50</td>
<td>0.8742</td>
<td>42.50</td>
<td>0.8840</td>
</tr>
<tr align="center">
<td>LLaMA-7b</td>
<td>6.96</td>
<td>0.6548</td>
<td>3.64</td>
<td>0.5084</td>
<td>8.95</td>
<td>0.6340</td>
<td>0.10</td>
<td>0.4899</td>
</tr>
<tr align="center">
<td>Alpaca-7b</td>
<td>36.00</td>
<td>0.8737</td>
<td>20.09</td>
<td>0.8003</td>
<td>14.37</td>
<td>0.8069</td>
<td>10.06</td>
<td>0.5604</td>
</tr>
</table>
</div>



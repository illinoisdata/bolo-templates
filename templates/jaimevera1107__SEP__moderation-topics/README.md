---
tags:
- bertopic
library_name: bertopic
pipeline_tag: text-classification
---

# moderation-topics

This is a [BERTopic](https://github.com/MaartenGr/BERTopic) model. 
BERTopic is a flexible and modular topic modeling framework that allows for the generation of easily interpretable topics from large datasets. 

## Usage 

To use this model, please install BERTopic:

```
pip install -U bertopic
```

You can use the model as follows:

```python
from bertopic import BERTopic
topic_model = BERTopic.load("jaimevera1107/moderation-topics")

topic_model.get_topic_info()
```

## Topic overview

* Number of topics: 94
* Number of training documents: 1403

<details>
  <summary>Click here for an overview of all topics.</summary>
  
  | Topic ID | Topic Keywords | Topic Frequency | Label | 
|----------|----------------|-----------------|-------| 
| 0 | suicide - nssi - tendency - recent - self | 40 | 0_suicide_nssi_tendency_recent | 
| 1 | exposed - minimal - sexualized - possessing - performs | 33 | 1_exposed_minimal_sexualized_possessing | 
| 2 | drug - reference - purposes - substances - substance | 32 | 2_drug_reference_purposes_substances | 
| 3 | regulated - consumption - tobacco - relate - associate | 31 | 3_regulated_consumption_tobacco_relate | 
| 4 | male - region - pubic - exposure - nipple | 31 | 4_male_region_pubic_exposure | 
| 5 | testing - wildlife - endangered - poaching - hunting | 31 | 5_testing_wildlife_endangered_poaching | 
| 6 | nudity - fine - implied - documentaries - indigenous | 30 | 6_nudity_fine_implied_documentaries | 
| 7 | text - language - pickup - textual - texts | 28 | 7_text_language_pickup_textual | 
| 8 | fighting - incitement - violent - reactive - event | 27 | 8_fighting_incitement_violent_reactive | 
| 9 | hate - ideology - hateful - based - disability | 27 | 9_hate_ideology_hateful_based | 
| 10 | sensual - pleasure - demonstration - objectification - dialogue | 26 | 10_sensual_pleasure_demonstration_objectification | 
| 11 | detailing - stimulation - fetishism - allusion - adults | 26 | 11_detailing_stimulation_fetishism_allusion | 
| 12 | pornography - vulgarity - website - tapes - softcore | 26 | 12_pornography_vulgarity_website_tapes | 
| 13 | lead - highly - is - imitable - professionals | 25 | 13_lead_highly_is_imitable | 
| 14 | brand - code - csam - qr - multiple | 25 | 14_brand_code_csam_qr | 
| 15 | expressions - dance - performing - performances - express | 24 | 15_expressions_dance_performing_performances | 
| 16 | intellectual - copyright - copyrighted - stolen - cover | 24 | 16_intellectual_copyright_copyrighted_stolen | 
| 17 | slur - slurs - designation - remarks - status | 24 | 17_slur_slurs_designation_remarks | 
| 18 | undressing - striptease - process - panties - voyeuristic | 23 | 18_undressing_striptease_process_panties | 
| 19 | workplace - peeping - upskirting - tom - coercion | 23 | 19_workplace_peeping_upskirting_tom | 
| 20 | hostility - degradation - statement - discriminatory - characteristics | 23 | 20_hostility_degradation_statement_discriminatory | 
| 21 | low - quality - organic - host - grow | 22 | 21_low_quality_organic_host | 
| 22 | terrorist - terrorism - recruitment - organizations - international | 21 | 22_terrorist_terrorism_recruitment_organizations | 
| 23 | spam - jump - makeup - scary - scare | 20 | 23_spam_jump_makeup_scary | 
| 24 | firearms - ammunition - explosive - explosives - weapons | 20 | 24_firearms_ammunition_explosive_explosives | 
| 25 | culturally - appropriate - wear - protected - not | 19 | 25_culturally_appropriate_wear_protected | 
| 26 | disturbing - cannibalism - disgusting - coverage - anatomy | 18 | 26_disturbing_cannibalism_disgusting_coverage | 
| 27 | homicide - mutilated - death - accident - torture | 18 | 27_homicide_mutilated_death_accident | 
| 28 | privacy - invasion - surveillance - espionage - confidential | 18 | 28_privacy_invasion_surveillance_espionage | 
| 29 | age - requirement - signals - identifiers - admission | 18 | 29_age_requirement_signals_identifiers | 
| 30 | framing - gaze - angles - piercings - camera | 17 | 30_framing_gaze_angles_piercings | 
| 31 | stalking - doxing - lists - encourage - addresses | 17 | 31_stalking_doxing_lists_encourage | 
| 32 | damage - destruction - property - arson - vandalism | 17 | 32_damage_destruction_property_arson | 
| 33 | eating - disorders - disorder - eat - loss | 16 | 33_eating_disorders_disorder_eat | 
| 34 | bullying - statements - cyberbullying - vulnerable - users | 16 | 34_bullying_statements_cyberbullying_vulnerable | 
| 35 | scams - frauds - scamming - schemes - fraudulent | 16 | 35_scams_frauds_scamming_schemes | 
| 36 | criminal - crime - criminals - gang - burglary | 15 | 36_criminal_crime_criminals_gang | 
| 37 | identifiable - data - personally - reveal - others | 15 | 37_identifiable_data_personally_reveal | 
| 38 | work - sex - prostitution - workers - escort | 15 | 38_work_sex_prostitution_workers | 
| 39 | conspiracy - theories - disinformation - baseless - current | 14 | 39_conspiracy_theories_disinformation_baseless | 
| 40 | consensual - recording - blackmail - intention - displaying | 14 | 40_consensual_recording_blackmail_intention | 
| 41 | child - featuring - pedophilic - defense - intimate | 14 | 41_child_featuring_pedophilic_defense | 
| 42 | polarization - opposing - social - incite - deepen | 14 | 42_polarization_opposing_social_incite | 
| 43 | pedophilia - grooming - normalization - predators - normalizing | 14 | 43_pedophilia_grooming_normalization_predators | 
| 44 | platforms - direction - ads - third - party | 14 | 44_platforms_direction_ads_third | 
| 45 | products - items - enhancement - grafitication - demonstrations | 13 | 45_products_items_enhancement_grafitication | 
| 46 | possession - consuming - drinking - tobacco - smoking | 13 | 46_possession_consuming_drinking_tobacco | 
| 47 | credible - threats - menacing - aggressive - plans | 12 | 47_credible_threats_menacing_aggressive | 
| 48 | hacking - malware - phishing - ransomware - hacks | 12 | 48_hacking_malware_phishing_ransomware | 
| 49 | proxy - lgbtq - bully - harassment - trolling | 12 | 49_proxy_lgbtq_bully_harassment | 
| 50 | going - live - 13 - 18 - u18 | 12 | 50_going_live_13_18 | 
| 51 | unintentionally - genitalia - animals - pornographic - bestiality | 12 | 51_unintentionally_genitalia_animals_pornographic | 
| 52 | artificial - traffic - way - methods - generate | 12 | 52_artificial_traffic_way_methods | 
| 53 | slaughter - mutilation - humans - dead - animal | 12 | 53_slaughter_mutilation_humans_dead | 
| 54 | goods - gangs - organized - counterfeit - illicit | 11 | 54_goods_gangs_organized_counterfeit | 
| 55 | gambling - betting - cheating - game - devices | 11 | 55_gambling_betting_cheating_game | 
| 56 | trafficking - forced - coerced - traded - function | 11 | 56_trafficking_forced_coerced_traded | 
| 57 | unsolicited - messages - favors - requests - advances | 11 | 57_unsolicited_messages_favors_requests | 
| 58 | blood - gore - shock - bloodshed - value | 11 | 58_blood_gore_shock_bloodshed | 
| 59 | victim - abduction - vehicle - motor - glorification | 11 | 59_victim_abduction_vehicle_motor | 
| 60 | inappropriate - kiss - sexualizes - objectifies - towards | 10 | 60_inappropriate_kiss_sexualizes_objectifies | 
| 61 | toddlers - infants - unintentional - touch - abdomen | 10 | 61_toddlers_infants_unintentional_touch | 
| 62 | traditional - traditions - sacred - cultural - misappropriation | 10 | 62_traditional_traditions_sacred_cultural | 
| 63 | nuclear - weapon - peaceful - advocating - energy | 9 | 63_nuclear_weapon_peaceful_advocating | 
| 64 | exploiting - child - marriage - exploitation - labor | 9 | 64_exploiting_child_marriage_exploitation | 
| 65 | impersonation - famous - figure - slandering - profiles | 9 | 65_impersonation_famous_figure_slandering | 
| 66 | defamation - someones - defamatory - allegations - businesses | 9 | 66_defamation_someones_defamatory_allegations | 
| 67 | recipes - creating - may - tools - instructions | 9 | 67_recipes_creating_may_tools | 
| 68 | election - interference - campaigns - misinformation - political | 9 | 68_election_interference_campaigns_misinformation | 
| 69 | claims - expertise - apocalypse - authority - media | 9 | 69_claims_expertise_apocalypse_authority | 
| 70 | featuring - nude - partial - implied - depictions | 8 | 70_featuring_nude_partial_implied | 
| 71 | operations - police - military - enforcement - law | 8 | 71_operations_police_military_enforcement | 
| 72 | tax - laundering - crimes - money - ponzi | 8 | 72_tax_laundering_crimes_money | 
| 73 | cosmetic - surgery - procedures - diy - unlicensed | 8 | 73_cosmetic_surgery_procedures_diy | 
| 74 | subject - optical - innuendos - illusion - suggestive | 8 | 74_subject_optical_innuendos_illusion | 
| 75 | bodies - fantasy - lifeless - accident - fictional | 8 | 75_bodies_fantasy_lifeless_accident | 
| 76 | controversial - constructive - politics - issues - discussion | 7 | 76_controversial_constructive_politics_issues | 
| 77 | kissing - lip - only - greeting - as | 7 | 77_kissing_lip_only_greeting | 
| 78 | pirated - plagiarism - incites - glorifies - first | 7 | 78_pirated_plagiarism_incites_glorifies | 
| 79 | mental - conditions - health - mocks - stigmatization | 7 | 79_mental_conditions_health_mocks | 
| 80 | daredevil - reckless - precautions - risking - caution | 7 | 80_daredevil_reckless_precautions_risking | 
| 81 | pranks - intentions - cybersecurity - harmful - targeted | 7 | 81_pranks_intentions_cybersecurity_harmful | 
| 82 | dark - web - underground - marketplaces - glorifies | 6 | 82_dark_web_underground_marketplaces | 
| 83 | vax - anti - medical - false - misinformation | 6 | 83_vax_anti_medical_false | 
| 84 | sports - danger - adventures - stunts - professional | 6 | 84_sports_danger_adventures_stunts | 
| 85 | environmental - pollution - experiments - ecosystems - natural | 6 | 85_environmental_pollution_experiments_ecosystems | 
| 86 | incest - incestuous - taboo - themes - discussion | 5 | 86_incest_incestuous_taboo_themes | 
| 87 | neglect - child - endangerment - abuse - physical | 5 | 87_neglect_child_endangerment_abuse | 
| 88 | radicalization - extremist - extremism - views - propaganda | 5 | 88_radicalization_extremist_extremism_views | 
| 89 | waste - bodily - excretion - unsanitary - images | 5 | 89_waste_bodily_excretion_unsanitary | 
| 90 | emotional - psychological - mind - gaslighting - relationships | 5 | 90_emotional_psychological_mind_gaslighting | 
| 91 | solicitation - offer - request - prostitution - act | 5 | 91_solicitation_offer_request_prostitution | 
| 92 | elderly - elders - elder - neglect - against | 5 | 92_elderly_elders_elder_neglect | 
| 93 | education - terms - term - relating - general | 4 | 93_education_terms_term_relating |
  
</details>

## Training hyperparameters

* calculate_probabilities: False
* language: english
* low_memory: False
* min_topic_size: 10
* n_gram_range: (1, 1)
* nr_topics: None
* seed_topic_list: None
* top_n_words: 10
* verbose: False

## Framework versions

* Numpy: 1.23.5
* HDBSCAN: 0.8.33
* UMAP: 0.5.4
* Pandas: 1.5.3
* Scikit-Learn: 1.2.2
* Sentence-transformers: 2.2.2
* Transformers: 4.24.0
* Numba: 0.58.1
* Plotly: 5.15.0
* Python: 3.10.12
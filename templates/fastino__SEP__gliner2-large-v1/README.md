---
library_name: gliner2
---
## Model Description

GLiNER2 extends the original GLiNER architecture to support multi-task information extraction with a schema-driven interface. This large model offers improved performance on challenging extraction tasks while maintaining efficient CPU-based inference.

**Key Features:**
- Multi-task capability: NER, classification, and structured extraction
- Schema-driven interface with field types and constraints
- Enhanced accuracy for complex and ambiguous extraction scenarios
- CPU-first design for inference without GPU requirements
- 100% local processing with zero external dependencies

## Installation

```bash
pip install gliner2
```

## Usage

### Entity Extraction

```python
from gliner2 import GLiNER2

# Load the model
extractor = GLiNER2.from_pretrained("fastino/gliner2-large-v1")

# Extract entities with descriptions for higher precision
text = "Patient received 400mg ibuprofen for severe headache at 2 PM."
result = extractor.extract_entities(
    text,
    {
        "medication": "Names of drugs, medications, or pharmaceutical substances",
        "dosage": "Specific amounts like '400mg', '2 tablets', or '5ml'",
        "symptom": "Medical symptoms, conditions, or patient complaints",
        "time": "Time references like '2 PM', 'morning', or 'after lunch'"
    }
)

print(result)
# Output: {'entities': {'medication': ['ibuprofen'], 'dosage': ['400mg'], 'symptom': ['severe headache'], 'time': ['2 PM']}}
```

### Text Classification

```python
# Single-label classification
result = extractor.classify_text(
    "This laptop has amazing performance but terrible battery life!",
    {"sentiment": ["positive", "negative", "neutral"]}
)
print(result)
# Output: {'sentiment': 'negative'}

# Multi-label classification
result = extractor.classify_text(
    "Great camera quality, decent performance, but poor battery life.",
    {
        "aspects": {
            "labels": ["camera", "performance", "battery", "display", "price"],
            "multi_label": True,
            "cls_threshold": 0.4
        }
    }
)
print(result)
# Output: {'aspects': ['camera', 'performance', 'battery']}
```

### Structured Data Extraction

```python
# Financial document processing
text = """
Transaction Report: Goldman Sachs processed a $2.5M equity trade for Tesla Inc. 
on March 15, 2024. Commission: $1,250. Status: Completed.
"""

result = extractor.extract_json(
    text,
    {
        "transaction": [
            "broker::str::Financial institution or brokerage firm",
            "amount::str::Transaction amount with currency",
            "security::str::Stock, bond, or financial instrument",
            "date::str::Transaction date",
            "commission::str::Fees or commission charged",
            "status::str::Transaction status",
            "type::[equity|bond|option|future|forex]::str::Type of financial instrument"
        ]
    }
)

print(result)
# Output: {
#     'transaction': [{
#         'broker': 'Goldman Sachs',
#         'amount': '$2.5M',
#         'security': 'Tesla Inc.',
#         'date': 'March 15, 2024',
#         'commission': '$1,250',
#         'status': 'Completed',
#         'type': 'equity'
#     }]
# }
```

### Multi-Task Schema Composition

```python
# Comprehensive legal contract analysis
contract_text = """
Service Agreement between TechCorp LLC and DataSystems Inc., effective January 1, 2024.
Monthly fee: $15,000. Contract term: 24 months with automatic renewal.
Termination clause: 30-day written notice required.
"""

schema = (extractor.create_schema()
    .entities(["company", "date", "duration", "fee"])
    .classification("contract_type", ["service", "employment", "nda", "partnership"])
    .structure("contract_terms")
        .field("parties", dtype="list")
        .field("effective_date", dtype="str")
        .field("monthly_fee", dtype="str")
        .field("term_length", dtype="str")
        .field("renewal", dtype="str", choices=["automatic", "manual", "none"])
        .field("termination_notice", dtype="str")
)

results = extractor.extract(contract_text, schema)

print(results)
# Output: {
#     'entities': {
#         'company': ['TechCorp LLC', 'DataSystems Inc.'],
#         'date': ['January 1, 2024'],
#         'duration': ['24 months'],
#         'fee': ['$15,000']
#     },
#     'contract_type': 'service',
#     'contract_terms': [{
#         'parties': ['TechCorp LLC', 'DataSystems Inc.'],
#         'effective_date': 'January 1, 2024',
#         'monthly_fee': '$15,000',
#         'term_length': '24 months',
#         'renewal': 'automatic',
#         'termination_notice': '30-day written notice'
#     }]
# }
```

## Model Details

- **Model Type:** Bidirectional Transformer Encoder (BERT-based)
- **Parameters:** 340M
- **Input:** Text sequences
- **Output:** Entities, classifications, and structured data
- **Architecture:** Based on GLiNER with multi-task extensions (large variant)
- **Training Data:** Multi-domain datasets for NER, classification, and structured extraction

## Performance

This large model provides:
- Enhanced accuracy on complex extraction tasks
- Better performance on ambiguous or difficult cases
- Improved handling of specialized domains (medical, legal, financial)
- Efficient CPU inference (GPU optional for faster processing)
- Superior multi-task performance

## Use Cases

The large model excels in:
- Medical information extraction
- Legal document analysis
- Financial document processing
- Complex multi-entity scenarios
- High-precision extraction requirements
- Domain-specific applications

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{zaratiana2025gliner2efficientmultitaskinformation,
      title={GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface}, 
      author={Urchade Zaratiana and Gil Pasternak and Oliver Boyd and George Hurn-Maloney and Ash Lewis},
      year={2025},
      eprint={2507.18546},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.18546}, 
}
```

## License

This project is licensed under the Apache License 2.0.

## Links

- **Repository:** https://github.com/fastino-ai/GLiNER2
- **Paper:** https://arxiv.org/abs/2507.18546
- **Organization:** [Fastino AI](https://fastino.ai)
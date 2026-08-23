# Reality Prose Adversarial Tests

Criterion [V3-2]: detected AND exit-nonzero AND summary blocked.

| mutant | detected | exit nonzero | summary blocked | verdict |
|---|---|---|---|---|
| remove-load-bearing-file | True | True | True | PASS |
| rename-file | True | True | True | PASS |
| add-unreferenced-file | True | True | True | PASS |
| duplicate-file | True | True | True | PASS |
| file-with-known-dependency | True | True | True | PASS |
| remove-from-scan-path | True | True | True | PASS |
| reintroduce-filename-typo | True | True | True | PASS |
| only-short-forms-file | True | True | True | PASS |
| only-ontology-refs-file | True | True | True | PASS |
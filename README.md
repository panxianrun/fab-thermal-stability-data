# Fab thermal stability study: supporting data

This repository contains the datasets and model evaluation outputs supporting the Fab thermal stability study.

## Files and provenance

| Path | Contents |
| --- | --- |
| `raw/fab_tm_483.csv` | 483 Fab VH/VL pairs and measured Tm; source copy: `data_483_tm2.CSV`. |
| `raw/igg_tm2_193.csv` | 193 external full-length IgG VH/VL pairs and Tm2; source copy: `raw_193_data.CSV`. |
| `processed/fab_binary_320.csv` | 320 Fab samples retained after excluding the middle tertile (162 low, 158 high). |
| `processed/igg_binary_129.csv` | 129 external samples retained after external-set tertile labeling (65 low, 64 high). |
| `processed/igg_binary_99_label_conflicts_removed.csv` | 99 external samples (45 low, 54 high) after excluding 30 overlapping sequences with discordant labels. |
| `processed/fab_labeling.json` | Fab thresholds (68.0 and 72.0 °C), counts and labeling protocol. |
| `processed/igg_labeling_full.json`, `processed/igg_labeling_dedup403.json` | External-set tertile thresholds (81.52 and 83.935 °C), with 129 labeled rows before filtering and 99 afterward. |
| `processed/fab_split_indices.npz` | Fixed 60/20/20 split indices for the 320-row Fab table; indices depend on its original row order. |
| `processed/external_overlap_report.json`, `processed/external_overlap_detail.csv` | Audit of overlap between the 320-row Fab and 129-row external tables. |
| `processed/fab_cdr_sequences_320.csv` | IMGT CDR alignment table used for sequence-logo analysis. |
| `results/traditional/*_metrics.json` | Internal test metrics and test labels/probabilities for traditional classifiers and four PLM embeddings. |
| `results/finetune/*_metrics.json` | Internal fine-tuning aggregate metrics for all four PLMs. The AntiBERTy file records `mode: full`. |
| `results/deep_mlp/*_metrics.json` | Internal Deep MLP aggregate metrics for all four PLMs; AntiBERTa2 fixed-split test ROC-AUC is 0.877810. |
| `results/external/*_99_metrics.json` | 99-sample external metrics for fine-tuned models and RF/XGBoost. |
| `results/robustness/antiberta2_500_splits.csv`, `results/robustness/antiberta2_500_splits_summary.json` | Per-run and summary metrics for 500 repeated splits. |
| `features/antiberta2_fab_320.npz`, `features/antiberta2_igg_99.npz` | AntiBERTa2 embeddings, labels and sample IDs for the Fab and filtered external datasets. IDs and labels match the processed CSVs in row order. |

The external dataset uses **its own** tertile thresholds, distinct from the Fab thresholds. Of 52 overlapping external sequences, 30 have discordant labels and were removed; **22 overlapping sequences remain in the 99-row table**. The external set is therefore not sequence-independent of the Fab set.

## Relationship to manuscript figures

- Figure 1 is a workflow diagram.
- Figure 2: raw/processed Fab data and `fab_cdr_sequences_320.csv` support the distributions, labels, CDR logos and sequence-length analysis.
- Figure 3: internal traditional, fine-tuning and Deep MLP aggregate metrics for all four PLMs are present.
- Figure 4: the 500-run CSV and summary are present and agree with the manuscript mean test ROC-AUC of about 0.795.
- Figure 5: the external dataset tables, available 99-sample model metrics and AntiBERTa2 embeddings are provided in `processed/`, `results/external/` and `features/`.

`SHA256SUMS.txt` records file hashes. Run `python verify_data.py` to check data integrity.

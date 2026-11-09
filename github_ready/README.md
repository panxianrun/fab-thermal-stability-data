# Fab thermal stability study: supporting data

This folder is a **staged data package**, organized from `I:\Tm2\文章\数据` and two local analysis tables. It is not yet a complete, publication-ready release. See **Missing evidence** below before publishing it.

## Files and provenance

| Path | Contents |
| --- | --- |
| `raw/fab_tm_483.csv` | 483 Fab VH/VL pairs and measured Tm; source copy: `data_483_tm2.CSV`. |
| `raw/igg_tm2_193.csv` | 193 external full-length IgG VH/VL pairs and Tm2; source copy: `raw_193_data.CSV`. |
| `processed/fab_binary_320.csv` | 320 Fab samples retained after excluding the middle tertile (162 low, 158 high). |
| `processed/igg_binary_129.csv` | 129 external samples retained after external-set tertile labeling (65 low, 64 high). |
| `processed/igg_binary_99_label_conflicts_removed.csv` | Server's `external_193/dedup403/data_193_binary.csv`: 99 external samples (45 low, 54 high). It matches the independently reconstructed 99-row table in every row. |
| `processed/fab_labeling.json` | Fab thresholds (68.0 and 72.0 °C), counts and labeling protocol. |
| `processed/igg_labeling_full.json`, `processed/igg_labeling_dedup403.json` | Server metadata for external-set local tertile thresholds (81.52 and 83.935 °C), 129 rows before overlap filtering and 99 rows afterward. |
| `processed/fab_split_indices.npz` | Fixed 60/20/20 split indices for the 320-row Fab table; indices depend on its original row order. |
| `processed/external_overlap_report.json`, `processed/external_overlap_detail.csv` | Audit of overlap between the 320-row Fab and 129-row external tables. |
| `processed/fab_cdr_sequences_320.csv` | IMGT CDR alignment table used for sequence-logo analysis. |
| `results/traditional/*_metrics.json` | Internal test metrics and test labels/probabilities for traditional classifiers and four PLM embeddings. |
| `results/finetune/*_metrics.json` | Internal fine-tuning aggregate metrics for all four PLMs. The AntiBERTy file records `mode: full`. |
| `results/deep_mlp/*_metrics.json` | Internal Deep MLP aggregate metrics for all four PLMs; AntiBERTa2 fixed-split test ROC-AUC is 0.877810. |
| `results/external/*_99_metrics.json` | Candidate 99-sample external metrics for fine-tuned models and RF/XGBoost. Their accuracy values have denominator 99; confirm which server run produced them before release. |
| `results/robustness/antiberta2_500_splits.csv`, `results/robustness/antiberta2_500_splits_summary.json` | Per-run and summary metrics for 500 repeated splits. |
| `features/antiberta2_fab_320.npz`, `features/antiberta2_igg_99.npz` | AntiBERTa2 embeddings, labels and sample IDs for the Fab and filtered external datasets. IDs and labels match the processed CSVs in row order. |

The external dataset uses **its own** tertile thresholds, distinct from the Fab thresholds. Of 52 overlapping external sequences, 30 have discordant labels and were removed; **22 overlapping sequences remain in the 99-row table**. The external set is therefore not sequence-independent of the Fab set.

## Relationship to manuscript figures

- Figure 1 is a workflow diagram.
- Figure 2: raw/processed Fab data and `fab_cdr_sequences_320.csv` support the distributions, labels, CDR logos and sequence-length analysis.
- Figure 3: internal traditional, fine-tuning and Deep MLP aggregate metrics for all four PLMs are present.
- Figure 4: the 500-run CSV and summary are present and agree with the manuscript mean test ROC-AUC of about 0.795.
- Figure 5: AntiBERTa2 embeddings for panels b and c are present. The reported external results for **ESM2–ExtraTrees, IgBERT–LR and AntiBERTa2–Deep MLP** are absent: the external traditional JSON contains only RF/XGBoost, and no Deep MLP external JSON was produced. The internal AntiBERTy fine-tuning metrics are for `full`, while the external plotting script prefers `AntiBERTy-partial`; check that the comparison uses the same model. The server's `dedup403/results/` JSON files are byte-for-byte identical to `full/results/` and their accuracies have denominator **129**, despite the `dedup403` input CSV and feature file each containing **99** rows. These 129-sample JSONs were not included in this package. The older local 99-sample JSONs in this package still need run provenance verified.

## Missing evidence before publication

1. Confirm the origin of the older local 99-sample JSONs, or regenerate them from the server's 99-row input. Recalculation is unnecessary if the original run and input can be verified. The server's current `dedup403/results/` files are duplicates of `full/results/` and describe 129 samples; do not combine them with the 99-sample figure or table.
2. Figure 5's caption names external ESM2–ExtraTrees, IgBERT–LR and AntiBERTa2–Deep MLP evaluations that are absent. Either evaluate those models or revise the figure and caption to show only the methods actually evaluated. If internal and external best results are selected separately, describe them as separate selections, not the transfer of one fitted model.
3. Confirm that the candidate 99-sample JSON metrics were calculated from the server's `dedup403` input and that the AntiBERTy model version matches the internal result. The 99-row input table and feature IDs/labels have already been verified.
4. Confirm reuse terms and cite the original AbPROP and GDPa1 data sources before making the raw CSVs public. Include the analysis code and environment in the eventual repository; this folder contains data only.

`SHA256SUMS.txt` records hashes for the staged files. Run `python verify_data.py` after any edits.

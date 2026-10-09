# Plagiarism Self-Check: Thesis_2_revised.docx

Date: 9 October 2026. Checked text: the Abstract and Chapters 1–7, 41,805 words. The reference list, contents pages and captions-only lists were excluded.

## Summary

| Check | Tool | Result |
|---|---|---|
| Verbatim phrase overlap with the thesis's own sources | Word 8-gram shingle matching (Python) | **0.24%** of words (100 of 41,805) are in matching passages. All passages are 8–15 words long and are definitions, method names or standard phrases. |
| Fingerprint similarity (MOSS-style winnowing) | **copydetect** 0.5 (open source, MIT licence) | Highest similarities are in the Abstract: **4.9%** vs. Gunasekara & Saarela (2025) and **3.1%** vs. Salih et al. (2025). Both are driven by the expanded names of SHAP and LIME. Every chapter-to-source pair is below 2%. |
| Close paraphrase | Sentence-level TF-IDF cosine similarity (scikit-learn) | **0 sentences** at similarity ≥ 0.5. The highest score is 0.48. The 9 sentences between 0.35 and 0.48 are reviewed below. |
| Web exact-phrase search | 10 randomly sampled 12-word windows (Chapters 1, 2, 3 and 6) | **0 of 10** found anywhere on the web. |

**Conclusion:** No sign of copied or lightly paraphrased text from the sources that could be checked. Three short passages are worth tightening (Section 3).

## 1. What was compared

The comparison corpus was built from the thesis's own 116 references, since these are the texts a thesis is most likely to borrow from.

- **Open-access full texts (Unpaywall API):** 41 sources. These come from publisher, NeurIPS, PMLR, JMLR, arXiv and EDM PDFs.
- **Abstracts only (Crossref, or a publisher page):** 24 further sources.
- **Total corpus:** 65 of 116 sources, with 16,604 sentences.
- **Not available:** 51 sources. They are paywalled, or the publisher site blocks automated download (for example the Elsevier, Springer and IEEE sites).

## 2. Controls (to show the tools detect copying)

| Control text | copydetect | 8-gram overlap | TF-IDF paraphrase |
|---|---|---|---|
| 80 words pasted verbatim from Wilkinson et al. (2016) | Detected (0.846) | Detected (80 words) | n/a |
| 6 sentences from Wilkinson et al. (2016) with every common word swapped (data→information, the→this, …) | Not detected | Not detected | **Detected (6 of 6, score 1.0)** |

copydetect only works on prose after the text is normalised (lowercase, single spaces, line-break hyphens removed) and its code filter is disabled. The run reported here used those settings.

## 3. Passages worth tightening

| Where | Thesis text | Source | Recommendation |
|---|---|---|---|
| Ch. 1, §1.1 | "LA is defined as the measurement, collection, analysis, and reporting of data about learners and their contexts to understand and optimise learning (Siemens & Long, 2011)." | The standard LAK 2011 definition, quoted widely (it also appears in Chen & Cui, 2020, and Miteva & Stefanova, 2022) | This is near-verbatim but has no quotation marks. Chapter 2 does quote it correctly. Either add quotation marks or paraphrase it. |
| Ch. 2, §2.4 | "…this involvement is mainly at the exploratory or problem-definition stage, with little input beyond it…" | Kaliisa et al. (2023): "this is mainly at the exploratory/problem definition stage, with little input beyond this stage" | A close paraphrase, though it is cited. Reword it, or quote the source directly. |
| Ch. 2, §2.3 | "…deployed for trials at a higher education institution…" | Susnjak et al. (2022), identical 8-word phrase | Minor. Reword if you want to be safe. |

The other matches are not concerns:

- **Method names:** "SHapley Additive exPlanations (SHAP) and Local Interpretable Model-agnostic Explanations (LIME)".
- **TAM constructs:** "perceived usefulness and perceived ease of use".
- **Common wording:** "early identification of students at risk of failing".
- **Variable list:** the OULAD variable list ("gender, region, highest education, IMD band, age band").
- **Signposting** between sections and titles cited in running text.

## 4. Limitations

- **Not equivalent to Turnitin or iThenticate.** Those services compare against billions of web pages, paywalled journals and previously submitted theses. No open-source tool has such an index.
  - About 44% of the thesis's sources (51 of 116) could not be obtained, so text borrowed from them would not be caught here. That includes much of Chapter 2's literature.
  - Earlier student theses and essays were not checked.
  - Your university's Turnitin check remains the authoritative one.
- **Web check is a sample.** The web search covered 10 sampled windows, not the whole thesis. The search tool may also not enforce exact matching strictly.
- **AI-generated text is not detected.** This check cannot tell whether text was written by an AI. It also does not flag text copied from the author's own earlier drafts.

## Files

- `copydetect_report.html`: copydetect's interactive report (chapters vs. sources).
- `overlap.json`: every matched 8-gram passage with its source.
- `paraphrase.json`: sentence pairs with TF-IDF similarity ≥ 0.35.
- `scripts/`: the corpus builder and the two checks, so the run can be repeated.

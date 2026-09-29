# Thesis_2 revision notes (first correction pass)

File: `Thesis_2_revised.docx`. The supervisor's tracked changes are accepted and all 107 supervisor comments are kept in place so they can be resolved in Google Docs. There are no em dashes. The file passes docx schema validation.

## Decisions taken with the author
- **RF vs XGBoost (C2, C62–C65, C88):** Option 2. XGBoost is kept, and Chapter 3 now states that recall is the primary criterion for choosing the prototype model, with F1-score used for comparative reporting. Chapters 1 and 3–7 were aligned to this.
- **Systematic review (C3, C20, C22–C24):** Option B. "Systematic literature review" becomes "structured review of relevant literature". Other authors' systematic reviews are unchanged.

## How each group of comments was handled
| Comments | What was done |
|---|---|
| C1, C9, C56, C72 (early-warning) | The retrospective-classification limitation is now stated in the Abstract, Ch1 (1.1, 1.6), Ch3 (3.8), Ch4 (4.6), Ch5 (5.2), Ch6 (6.1, new 6.11 paragraph) and Ch7. The supervisor's wording is used for 4.6. |
| C4, RQ3 | The supervisor's reworded RQ3 is used everywhere RQ3 appears (1.4, 4.12, 5.11, 6.5, 6.12, 7.3.3). "Intepretation" typo fixed. |
| C5, C50, C51 | Section 3.9 uses the supervisor's text: "the evaluation plan proposed subgroup performance and fairness assessment… not completed". "Pseudonymised" became "anonymised" (Kuzilek et al., 2017 use "anonymised"). |
| C6, C25, C69, C89 | Option B: stability and fidelity checks are described as proposed safeguards that were not completed (2.3, 3.5, 4.7, 5.10, 6.11, 7.2, using the supervisor's text for 7.2). |
| C7, C12–C14, C21, C52, C71, C78, C84, C95, C100–C103 | Chapters 5–7 are now proper headings ("CHAPTER 5/6/7"). Section 6.12 is no longer skipped. Every chapter and back-matter section starts on a new page. The ToC is rebuilt as an automatic field with all 7 chapters. Figures are renumbered in order (Ch3: 3.1↔3.2; Ch4: 4.1–4.9, with the duplicate 4.2 removed). The List of Figures and List of Tables are rebuilt with page numbers, and "Structure of the Thesis" now says six chapters. |
| C8 | The abstract is on one page (single spacing, 11.5 pt). |
| C10, C11, C15, C16, C17, C18, C19, C26, C27 | The supervisor's wording is used where it was given. OULAD is described as "one of the most widely used benchmarks" with 3 references from the folder. The problem statement is reframed as a design/technical problem. Absolute claims become "the literature reviewed … did not identify". |
| C28, C36, C37, C39, C40, C44, C49, C60 | Chapter 3 now describes the final method (four-fold GroupKFold, fixed XGBoost configuration, no resampling or tuning). A new subsection **3.4.1 Planned but Not Implemented Methodological Extensions** lists SMOTE, class weighting, Bayesian optimisation, calibration, trajectory features, secondary metrics and five-fold CV. Their literature moved to the end of 2.2. Future tense became past tense. Implementation detail (feature dictionary, manifests, nightly batch) now sits only in Chapter 4. A new opening paragraph states what each chapter covers. |
| C29, C30, C31, C32, C33, C73 | A framework hierarchy paragraph (DSRM > CommonKADS > TAM > Kaliisa checklist). **Table 3.1** covers all six CommonKADS models, plus an explicit Organisation Model paragraph. The supervisor's TAM sentence is added. The literature-based Agent Model is acknowledged in Ch3. |
| C34 | **Table 3.2** (role-based dashboard design) is filled from the thesis content and placed in 3.6 next to the role briefs. |
| C38, C41, C42, C43, C45, C46, C47, C48, C53, C55, C57, C58, C59, C61 | The supervisor's replacement sentences are used where given. Claims that cannot be demonstrated (heuristic iterations, CI/tests, Figma, lockfile, archival deposit) are softened. "Deployed system" became "working prototype". The unit "32,593 student-module-presentation observations" is used throughout. It is stated that SHAP was computed on the final fitted model across all rows and is not fold-specific. Ch4 captions now say "Screenshot from the prototype development". The heading is now "4.11 Prototype Deployment Topology". |
| C54 | The duplicate Figure 4.2 caption is deleted. |
| C66, C67, C68, C70, C79, C80, C81, C82 | The supervisor's wording is used (collinearity only as "one possible explanation", now citing Salih et al., 2024). The weak third RQ3 point is recast as external context or qualified. "Non-trivial false-positive rate (15.5%)" replaces "manageable". |
| C74 | The three-level evidence model (demonstrated / supported by design / not empirically established) is introduced in 1.6 and 3.8 and used in Ch6 and 7.3.3. |
| C75 | **Figure 6.1** (Prediction → Explanation → Human interpretation → Intervention) is added with the explanation the supervisor requested. |
| C76, C77 | **Table 6.1** (transferability) uses the supervisor's rows, plus a "feature importance rankings" row. |
| C83, C85–C94 | Chapter 7 is aligned with the Chapter 6 qualifications. Students are removed and the three staff roles restored. The supervisor's sentences are used for C89 and C94. RF's higher F1 is reconciled. 7.5 now has 3 first-tier items: early-warning evaluation at weeks 2/4/6/8, calibration, and fairness. |
| C96, C97, C98, C99 | 28 uncited references removed (all 14 the supervisor listed, plus 14 others). Waterson (2014) and Jivet et al. (2021) claims were removed or replaced with the verified Kaliisa et al. (2023). APA fixes: page ranges, "edn."/Harvard entries, Nnadi's authors, "Salih/Nnadi et al.", Chen ordering, and volume numbers from the folder PDFs. |
| C104, C105, C106 | Appendix A deleted. The new **Appendix A** holds reproducibility details. **Appendix B** holds feature definitions (Table B.1, with the 24 input columns taken from the model in this repo) plus the existing rankings. |

## Corrections found while verifying against the supplied materials
- **Wang (2025):** reports **96.9% on OULAD** and 98.8% on the UCI dataset. The thesis said 98.8% on OULAD; corrected in 5 places.
- **Cabral et al. (2025):** contain no "fewer than 15%" figure. Replaced with what the review does say (XAI components are absent from most dashboards).
- **Susnjak et al. (2022):** the dashboard is learner-facing and never named "SensEnablr". Corrected in 2.3 and 2.4.
- **Kostopoulos et al. (2024):** a review, not an empirical demonstration. Wording softened in 1.2, 4.8 and 6.3.
- **Gunasekara & Saarela (2025):** do not use the phrase "complementary strengths". The supervisor's softer wording is applied consistently.
- **Salih et al. (2024):** say SHAP has a *higher computing time* than LIME. They do not say "TreeSHAP cacheable / LIME inexpensive per query".
- **Data preparation (Ch3):** said ordinal encoding and stratified splits. Chapter 5 and the model show one-hot encoding and GroupKFold, so Chapter 3 now matches.
- **Duplicated paragraphs removed:** start of 2.5 (a copy of 2.4) and the second Canvas paragraph in 4.10.2.

## Supervisor tracked changes not accepted literally
- **"studentVle" → "studentValue":** rejected. The OULAD table is `studentVle` (Kuzilek et al., 2017) and the correct name also appears in Table 4.1.
- **"Behavioural" → "Behavioral" (5.9):** kept as British spelling, to match the rest of the thesis.
- **Deleted paragraph mark at the end of 7.4:** would have merged the 7.5 heading into the paragraph, so it was not applied.
- **Instruction insertions** ("Maybe include a table here", "For example:", "Add a table", "This would make…"): implemented as Tables 3.1, 3.2 and 6.1 rather than kept as text.
- **"Put a reminder to add the paper here when its published" (1.5):** removed from the text. **Please add your paper reference here once it is published.**

## Needs your manual review (not guessed)
1. **Missing references, now added (verified on the web from publisher/indexing pages):** Gunning & Aha (2019), Chatti et al. (2012), Viberg et al. (2018), Larrabee Sønderlund et al. (2019), Aljohani et al. (2019), Conati et al. (2021), Wachter et al. (2018), Kouki et al. (2020), Sedrakyan et al. (2020), Bodily & Verbert (2017), Miteva & Stefanova (2022). In-text spellings were corrected to match: Thüs, Bälter, Järvelä, Larrabee Sønderlund, and "Hassan et al." became "Hassan". "Leitner et al. (2022)" could not be found anywhere; the claim matches Leitner, Ebner & Ebner (2019), already listed and cited for the same point in Chapter 4, so the year was corrected to 2019. **The list now has 117 references.**
2. **Still unresolved:**
   - **Rodríguez-Ortiz et al. (2022, J. Intelligent & Fuzzy Systems, DOI 10.3233/JIFS-211603):** no indexed record exists for this DOI or title. **It very likely does not exist.** It is the only support for the CommonKADS-in-education claim in 3.1 and 6.4. Replace it with a real source or remove those sentences.
   - **Alharbi & Janarthanan:** the paper exists but has a third author (D. Midhunchakkaravarthy), and sources disagree on the year (2024 vs 2026). The volume and DOI could not be confirmed.
   - **Li, Wong & Chan (2020):** a 2024 journal version exists (Int. J. Innovation and Learning, 36(5)), apparently with Liu rather than Chan as an author. Please confirm which version you used.
   - **Adadi & Berrada (2018):** the latency claim was removed as unverifiable.
3. **2025/2026 references:** no 2026 papers were in the folder. The OULAD claim now cites Gunasekara & Saarela (2025), Jin et al. (2024), Wang (2025) and Kuzilek et al. (2017).
4. **Appendix A (yellow highlights):** Python version, hardware, Git commit, model artefact ID and the other package versions are not recorded anywhere in the materials. Please fill these in.
5. **Appendix B:** calculation entries marked "(inferred)" come from feature names, because the feature-engineering code was not supplied. The model includes a `withdrew_before_start` feature that the thesis text never mentions. Please check how it is derived and whether it relates too closely to the at-risk label.
6. **Removed claims you may wish to restore if true:** Figma prototyping; Git version control; the use-case, ER and sequence diagrams (now described as "not reproduced in this thesis"); unit tests and CI (now described as planned).
7. **SHAP population:** the text now says the final model was fitted on all 32,593 observations. This follows from Sections 4.7 and 5.6 together; please confirm.
8. **Missing-value handling:** Chapter 3 says indicator encoding, but Table 4.1 says imputation. Left unchanged; please confirm which is correct.
9. **Page numbers:** computed from a LibreOffice rendering (117 pages). In Google Docs, refresh the Table of Contents with its update button. Google Docs cannot generate lists of figures or tables automatically, so check the LoF/LoT page numbers after upload.

## Unused literature-folder papers
Not cited, to avoid adding new arguments: Leichtmann et al. (2023), Embarak & Hawarna (2024, RADAR), Ben George et al. (2025, JISEM), Adelodun et al. (2025), Park & Jo (2015). Vlachogianni & Tselios (2022) is in the folder but was removed, as the supervisor directed (no SUS study was conducted).

## Chapter 4 updated to the working prototype (second pass)
The earlier Chapter 4 described a deployment that was never built: Cloudflare Pages, a Cloudflare Worker with Workers KV and a nightly cron, Render hosting, an LTI 1.3 launch into Moodle through Cloudflare Tunnel, and mock-up LMS screenshots. It now describes the system in `xai-dashboard/`, which was run and tested end to end in Docker.
- **Text:**
  - **4.1 introduction:** the reference to hosting providers was removed.
  - **Table 4.1:** the edge/gateway, LTI/jose, hosting and LMS rows were replaced with the real components: gunicorn, the `local_xairisk` Moodle plugin, the Canvas External URL embed, LMS data synchronisation, Moodle 5.2, and Docker Compose. The typo "libjay" was also corrected to "lbjay".
  - **4.8:** the Worker-based role check was replaced by the real design. The dashboard's own JWT login is used for direct and Canvas access. The Moodle plugin checks Moodle capabilities, then calls the API with a shared service key.
  - **4.10.1 Moodle:** now describes the native plugin; the courses, users and enrolments loaded (22, 28,785 and 32,593); and the cross-role and cross-course access tests.
  - **4.10.2 Canvas:** the SIS import of the 22 courses and the dashboard module added to each.
  - **4.11 Prototype Deployment Topology:** now describes a single Docker Compose deployment, cached cohort results and the frame-ancestors policy.
  - **4.12 Summary:** the list of languages was updated.
- **Figures:** all are screenshots or diagrams of the running prototype, and every caption keeps "Screenshot from the prototype development" (comment 59). Nothing else in Chapter 4 was mocked up.
  - **4.1:** a new architecture diagram.
  - **4.4 to 4.7:** the dashboard served by the Docker container. The instructor view was changed to show SHAP and LIME side by side, as the thesis describes.
  - **4.8:** the Moodle plugin inside course FFF-2014J.
  - **4.9:** the dashboard embedded in Canvas course FFF-2014J.
- **Abbreviations:** CDN, JWKS and KV were removed because they are no longer used; SIS was added.
- **Unchanged:** all 107 comments are still anchored, there are no em dashes, and the validator output is identical to the previous version's.

**Needs your decision: the model numbers do not match.** The figures now show the rebuilt model's out-of-fold results, but Chapters 4 to 6, the abstract and Figure 4.3 still report the numbers from your original run. The data and class counts are identical (17,208 at risk, 15,385 not at risk); only the fitted model differs slightly.

| Metric | Thesis text | Rebuilt prototype (shown in Figures 4.6 and 4.7) |
|---|---|---|
| Accuracy | 0.8804 (88.0%) | 0.8774 |
| F1 | 0.890 | 0.8867 |
| Recall | 0.9125 (15,702 of 17,208) | 0.9085 (15,634) |
| AUC | 0.964 | 0.9624 |

Either update the numbers throughout to the rebuilt model, or state in 4.6 that the screenshots come from a re-run of the pipeline whose results differ slightly from those reported.

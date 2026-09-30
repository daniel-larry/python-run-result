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
2. **Unresolved references, now resolved** (checked on Crossref, OpenAlex and the publisher sites):
   - **Rodríguez-Ortiz et al. (2022): removed, because it does not exist.**
     - DOI 10.3233/JIFS-211603 was never issued, and no database has the title.
     - The Section 3.1 paragraph that rested only on this source was removed.
     - The comparison sentence in 6.4 and the reference entry were removed too.
   - **Alharbi & Janarthanan: replaced.**
     - The article appeared only on lettersinbiomath.org, which issues no DOIs. The registered *Letters in Biomathematics* (ISSN 2373-7867) has issued none since 2021, which suggests the site is a hijacked or cloned journal.
     - The site no longer lists the article.
     - It was replaced by **Hooshyar & Yang (2024), *IEEE Access*, 12, 137472–137490, doi:10.1109/ACCESS.2024.3463948**, a peer-reviewed comparison of SHAP and LIME in education. The wording in 5.8 and 6.3 follows its abstract.
   - **Li, Wong & Chan: corrected.** It is a 2023 Springer chapter (pp. 119–128, doi:10.1007/978-981-99-8255-4_11), not a 2020 university report.
   - Adadi & Berrada (2018): the latency claim was removed earlier as unverifiable.
3. **2025/2026 references:** no 2026 papers were in the folder. The OULAD claim now cites Gunasekara & Saarela (2025), Jin et al. (2024), Wang (2025) and Kuzilek et al. (2017).
4. **Appendix A:** now completed from the Docker image (see "Chapter 4 updated to the working prototype" below).
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

**Results updated to the prototype's model.** All results were recomputed from the model run in Docker (model version `xgb-20260929-112741`). The values were replaced throughout:
- the abstract;
- Chapter 4: Section 4.6 and Figure 4.3;
- Chapter 5: Tables 5.1 to 5.5, Figures 5.1 to 5.5, and the text;
- Chapters 6 and 7;
- Appendices A and B.

| Metric | Before | Now |
|---|---|---|
| Accuracy | 0.8804 | 0.8774 |
| Precision | 0.8678 | 0.8659 |
| Recall | 0.9125 | 0.9085 |
| F1 | 0.8896 | 0.8867 |
| AUC | 0.9642 | 0.9624 |
| Confusion matrix (TN, FP / FN, TP) | 12,994, 2,391 / 1,506, 15,702 | 12,963, 2,422 / 1,574, 15,634 |
| Random Forest F1 | 0.9010 | 0.8976 (still the highest F1; XGBoost still has the highest recall) |
| SHAP/LIME top-5 overlap | 0.595 (sd 0.192) | 0.635 (sd 0.197) |

**Statements whose meaning changed, not only their numbers.** Please read these:
- **The 28-day click window:** whether it outranks total clicks is now reported as a **robustness check** (Section 5.7), and the result is that the order **cannot be settled from a single model**.
  - The two features are near-duplicates, with a Spearman correlation of 0.98.
  - In 8 refits of the model with different random seeds (`xai-dashboard/ml/seed_stability.py`), the 28-day window ranked higher in 4 of them.
  - Their combined importance stays stable, between 0.57 and 0.69.
  - Sections 5.6, 5.12, 6.2, 6.3 and Appendix A were updated to match. The measured correlation also supports the collinearity explanation for the 28-day window's counter-intuitive sign.
- **Second-ranked SHAP feature:** now active days (0.709), not mean score. n_assessments_submitted leads by more than four times rather than three.
- **SHAP and LIME agreement:** they now share 7 of their top 10 features instead of 8. The features on which they differ are listed in 5.6.
- **Counts:** 59 transformed features, not 60; the feature table has 28 columns, not 29.
- **Removed as no longer true:**
  - "raw OULAD CSV files were not available" (5.10);
  - "newer library versions" (5.7, 6.2, 6.4);
  - "tested LTI" integration (6.4);
  - pyarrow/parquet (Table 4.1): the pipeline writes CSV.
- **Appendix A:** Python, package versions, hardware, commit and model identifier are now filled in from the Docker image. The yellow placeholders are gone.

**Figure 4.7** now shows both authentication paths:
- (a) Moodle's login page, after which Moodle supplies the role and course;
- (b) the dashboard sign-in inside a Canvas course.

In Figures 4.7(b) and 4.9, Canvas's notice for plain-HTTP embeds ("You are trying to launch insecure content…") was hidden when the screenshots were taken. The 2017 Canvas image shows it for every `http://` link, and it would disappear with HTTPS.

## Compliance check against all 107 comments (final pass)
Each comment's anchored text and each thesis-wide concern was checked against the current document. Three leftovers were fixed:
- **C36:** Chapter 3 no longer points to "scheduled scoring" in Chapter 4, since the nightly job was part of the removed hosted setup.
- **C90:** Section 3.2 no longer claims the design is "improving usability". It now states that usability was not measured.
- **C53:** Section 4.3 now says "prototype codebase" and "prototype pipeline" instead of "production" and "productionisation".

Everything else was confirmed in place:
- **Structure:**
  - every chapter and back-matter section starts on a new page;
  - the ToC includes Chapters 6 and 7 (with 6.12 and 7.5), References and Appendices;
  - the lists of figures and tables and their page numbers are regenerated.
- **Words removed or limited:**
  - "systematic" is used only for other authors' reviews;
  - "early warning" appears only as a stated limitation or as future work;
  - SMOTE, TPE, calibration and five-fold CV appear only in Chapter 2, Section 3.4.1 and Chapter 5's comparison;
  - "pseudonymised", "student records", "manageable" and the student-facing view are gone.
- **Statements now in the text:**
  - the TAM design-lens sentence;
  - fairness and stability described as "not completed";
  - the three mandatory future-work items;
  - the working-prototype wording.
- **References:** consistent APA; the unused ones (Creswell, Braun & Clarke, etc.) removed; Jivet (2021) replaced by Kaliisa, Jivet & Prinsloo (2023); Waterson (2014) removed.

Still open: your own paper reference in Section 1.5, to add once it is published. The three previously unverified references are now resolved (see item 2 above).

## Grammarly wording pass (merged onto the intact document)

The Grammarly export itself was not used as the document. It had been made from an earlier version, and the export
removed the 107 comments, the footer and page numbers, list numbering, the TOC field, the page size and margins,
most page breaks, and the header rows of Tables 3.1, 3.2, 6.1, A.1 and B.1. Grammarly's wording changes were
instead applied onto the current thesis, which keeps all of those.

- Applied: Grammarly's rewrites in 203 paragraphs (concision, hyphenation such as decision-making and
  well-validated, artefact, active phrasing without a personal pronoun).
- Not applied, to keep the thesis voice: 30 paragraphs where Grammarly rewrote into the first person ("We
  specified...", "we ran...").
- Not applied, because the paragraph was corrected after the version sent to Grammarly: 7 paragraphs (the
  Rodríguez-Ortiz, Alharbi and Li reference fixes, "productionisation" and "scheduled scoring").
- Not applied: 1 rewrite that began "Figure 3.2 illustrates...", which would have been listed as a figure caption.
- Grammarly slips corrected: "administrators-", "proposedrole-aware", "However,methodological", "works,,",
  "the the", "level,,", "ad" for "and"; US spellings "toward" and "counterintuitive" kept British.
- Meaning slips corrected: "the authors did not test it" (the untested condition belongs to this study, so it now
  reads "this study did not test it"), and a comma removed in "plausible and the underlying prediction is wrong".

## Chapter 1 plain-language pass (27 flagged sentences)

Accepted as proposed: 4, 6, 7, 9, 13, 14, 15, 19, 20, 21, 22, 23, 24, 25, 26.

Accepted with a change:
- 1: keeps "guided by" the CommonKADS knowledge engineering methodology.
- 2: keeps "for student risk prediction in higher education", so the contribution stays specific.
- 3: keeps "and divergence". The 0.635 SHAP/LIME overlap is a divergence finding. Also keeps trust,
  interpretation and decision quality as what future studies would test.
- 5: the proposed second sentence repeated the one after it, so the two were merged. The Kuzilek et al. (2017)
  citation is kept.
- 6: the Rebelo Marcolino et al. (2025) citation is kept.
- 8: keeps the point that a prediction affects both the student and the professional judgement of whoever acts on it.
- 10, 11: the citations are kept. Sentence 11 still says "few domain-specific frameworks", which is what Al-Ansari
  (2024) supports. The proposed "few studies use" would be a different claim.
- 12: keeps "future research with practitioners should address these questions".
- 16 (RQ2): keeps "can be specified". The proposed "can support" would claim an effect that was never tested
  (supervisor comment 4). Updated identically in Chapters 1, 6 and 7.
- 18: keeps "LMS-integrated" (the prototype runs inside Moodle and Canvas) and "differentiates".
- 27: "sets out the study's limitations", to avoid "discusses ... discusses".

Not applied:
- 17 (RQ3): the "proposedrole-aware" typo was already fixed. The rewrite dropped "technical" from "technical
  potential", which was added to answer supervisor comment 4, and RQ3 is restated verbatim in Chapters 6 and 7.

## "Systematic" dropped from the study's own claims

- RQ1 now asks how SHAP and LIME "can be integrated", in Chapters 1, 6 and 7.
- Section 6.12 no longer describes the integration as "systematic". Section 3.3 now says "an explicit analysis" of each
  role's knowledge needs.
- The word stays where it names cited systematic reviews (Jin et al., Albreiki et al., Viberg et al. and others), and
  in "systematic disparities" (Baker and Hawn). Those are accurate descriptions of other work.

## Chapter 2 plain-language pass (46 flagged sentences)

Accepted as proposed: 3, 4, 5, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27, 28, 30, 33, 34, 35, 36,
37, 38, 39, 42, 43, 44, 45, 46. Nos. 13, 24, 35, 39 and 40 also soften absolute claims ("dominant", "all", "none",
"not conceptualised", "original"), in line with supervisor comment 27.

Accepted with a change:
- 1: "Technical, methodological, and evaluation work", as in the original. The proposed "dashboard design" changed
  what the five gaps are.
- 2: "designs ... against a common knowledge engineering specification". The next sentence already says the study
  brings these areas together, so "brings together" would have repeated it.
- 6: grammar ("has given less attention to", not "has received less attention to").
- 9, 31: the proposal covered only the first half of each sentence. The second half ("and that models which
  optimize ...", "and they call for designs ...") is kept.
- 10: Chatti et al. is a learning analytics reference model, not a dashboard model. It now reads "a central design
  concern" rather than "part of dashboard design".
- 12: keeps "This is the central premise of the study."
- 23: split as proposed. "Did not systematically address" (Gunning and Aha) became "did not address in depth".
- 29: "these earlier reviews", which is what the sentence refers to.
- 32: keeps the knowledge each role brings, the point that links this passage to CommonKADS.
- 40, 41: citations kept: Schreiber et al. (2000); Al-Ansari (2024) and Kim et al. (2024).

Not applied:
- 19, 21: "refinements" kept. SMOTE, Bayesian optimisation, calibration and trajectory features are techniques, not
  "issues". The proposal for 21 also used em dashes, which the thesis does not use.

## Chapter 3 plain-language pass (46 flagged sentences)

Not in the thesis (items 10-15 and 17-23): these quoted sentences do not occur in the current document or in the
Grammarly export ("deliberately layered", "independently testable", "not simply a matter of convenience",
"like-for-like", "fixed-configuration approach", "cross-method checking" and so on). Nothing was changed for them.
Item 9 is also not the current wording: the thesis says the agent characterisations are "a well-sourced hypothesis
about the three roles rather than a documented account of them", which is already plain, so it is kept. Item 16 is
in Chapter 4 (Section 4.6) and was applied there.

Accepted as proposed: 5, 7, 24, 26, 28, 29, 30, 31, 33, 34, 35, 37, 39, 42, 44, 46.

Accepted with a change:
- 1: keeps that the design problem "is a knowledge engineering problem", the justification for CommonKADS.
- 2, 3, 4: citations kept: Schreiber et al. (2000), Studer et al. (1998).
- 6: citations kept (Tsai & Gaševic; Leitner et al.; Kaliisa et al.), plus the pointer to the following paragraph.
- 8, 32, 36, 40: the proposal covered only part of each sentence, so the rest is kept (the CommonKADS
  expectation, the list of planned tests, what an early-warning evaluation would need, and the pointer to
  Chapter 7).
- 16: keeps that the leakage check raises an assertion error. This is true of the code
  (xai-dashboard/ml/data_layer.py). The cross-reference is corrected to Section 3.3, where the windows are described.
- 25: keeps the Molenaar and Knoop-van Campen (2019) citation.
- 27: keeps all four Nielsen heuristics. The proposal dropped one without reason.
- 38: the proposal merged two separate checks. Reproducing the metrics from the model artefact and comparing the
  implementation with the planned method are kept as two steps.
- 41: keeps the section reference and that no primary data were collected from any group.
- 43: keeps "even when overall accuracy is high", which is the point of Yu et al. (2020).
- 45: keeps "only" in "TAM is used only as a design lens". The thesis states elsewhere that TAM is not evaluated.

## Plain-language pass on Chapters 4 to 6 (self-flagged), plus the rest of the second flag list

Method, following the author's flag lists: sentences of about 50 words or more; stock phrasing ("surfaces",
"foregrounds", "genuine", "positioned", "What the X is ...", "substantive", "consequential"); and abstract nouns used
where a verb would do. Long sentences were split, and stock words were replaced with plain ones ("shows",
"reveals", "emphasises"). No number, citation or hedge was changed. About 60 edits.

- Second flag list: items 3 (TAM paragraph), 4 (Lundberg/Ribeiro, 5.8), 5 (partial agreement, 6.x), 6 ("positioned
  on the side of that argument"), 7 (design science paragraph), 8 ("what learning analytics is for"), 16 (Chapter 1
  limitations sentence), 18 ("normative argument") and 19 ("hierarchical") applied. Items 1, 2 and 9 to 15 were
  already done in the previous passes.
- Item 7: the new wording says the study "also draws on" design science. It no longer says "additionally informed
  by", which conflicted with the next paragraph naming DSRM as the overarching methodology.
- Item 4: keeps that the 0.635 overlap is not a finding specific to student data.
- Chapter 4: 20 edits (opening, OULAD scope, layering, Colab, the Miller sentence, which had a grammar slip, model
  manifest, local explanation service, service-key authentication, role header, reasoning trail, LMS integration,
  Sculley, chapter summary).
- Chapter 5: 16 edits (accuracy under mild imbalance, confusion matrix caution, per-presentation reporting,
  literature comparison paragraphs, 5.9 to 5.12 summaries).
- Chapter 6: 22 edits (operating point, reasoning trail, CommonKADS reflection, practitioner-response paragraph,
  "positioned" sentence, Nigeria transfer, and the 92-word summary sentence, now four sentences).

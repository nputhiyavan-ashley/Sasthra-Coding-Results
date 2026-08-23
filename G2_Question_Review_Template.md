# G2 Coding Round — Per-Question Review Template

Use this template whenever asked to **"Evaluate Question Qxx following this document."**
It operationalizes the "Scoring Policy" tab of `G2_Coding_Results_Template.xlsx`. Total = 100 points across 5 weighted criteria.

---

## 0. Setup

- **Question ID:** (Qxx — look up the exact entry in Section 9, Question Bank Reference)
- **Candidate ID:**
- **Repository link/path:**
- Confirm the repository maps to this exact question. If the question mapping is unclear, stop and flag for human review (do not evaluate against a different question).

---

## 1. Functional correctness — /45

**Evidence to check:** visible and hidden test results, output comparison, runtime status, ability to build/run the code as submitted.

- Full marks: all essential behaviour and mandatory edge cases (from the question's "Mandatory Edge Cases" column) pass, and the code runs/builds without secrets or inaccessible services.
- Partial marks: award proportionally by behaviour-weighted hidden tests; distinguish core logic failures from formatting-only failures; minor recoverable packaging gap (e.g., missing dependency declaration inferable from imports).
- Zero / major concern: no runnable core solution, hardcoded sample output, unrelated implementation, or code that does not run/build.
- **Automatic cap:** if the repo is not runnable for a student-caused reason, cap this score at ≤10.
- An external API or rich UI is never required unless the question explicitly says so.
- **Escalate to human review if:** environment ambiguity, unsupported language, operating-system/dependency mismatch, or a disputed expected result.
- **Do not** raise a `missing_repository_docs` (or similar documentation-related) review flag or deduct score for absent README/AI_USAGE/documentation files — documentation is out of scope for this evaluation.

**Score:** ___ / 45   **Evidence/notes:**

---

## 2. Problem interpretation — /10

**Evidence to check:** implementation behaviour, input/output handling.

- Full marks: solves the supplied problem with no conflicting assumptions.
- Partial marks: minor gap that does not change the core result.
- Zero / major concern: solves a materially different problem or ignores a critical rule.
- No automatic cap.
- **Escalate to human review if:** the question wording could reasonably support more than one interpretation.

**Score:** ___ / 10   **Evidence/notes:**

---

## 3. Algorithm and data structures — /15

**Evidence to check:** source code, complexity explanation, observed behaviour at boundary input sizes.

- Full marks: appropriate structure and complexity for stated constraints.
- Partial marks: correct but less efficient, still viable for moderate input.
- Zero / major concern: clearly non-viable brute force or no meaningful algorithm.
- Do not require one "preferred" implementation when alternative approaches satisfy the constraints.
- **Escalate to human review if:** AI/reviewer is uncertain about language-specific complexity or library behaviour.

**Score:** ___ / 15   **Evidence/notes:**

---

## 4. Testing and edge cases — /15

**Evidence to check:** student tests mapped to sample, normal, boundary, and mandatory edge cases.

- Full marks: tests cover sample plus all stated mandatory edge cases with meaningful assertions.
- Partial marks: sample plus at least two meaningful non-sample cases.
- Zero / major concern: no tests, or tests that don't exercise the implementation.
- Test *quantity* alone is not credit-worthy — behavioural coverage is required.
- **Escalate to human review if:** tests cannot execute due to a framework or environment issue.

**Score:** ___ / 15   **Evidence/notes:**

---

## 5. Code quality (student level) — /15

**Evidence to check:** naming, decomposition, duplication, comments where needed, basic error handling.

- Full marks: readable, reasonably modular and maintainable for a 30-minute student exercise.
- Partial marks: mostly understandable with some monolithic or repetitive code.
- Zero / major concern: obfuscated, largely unexplained, or structurally unusable code.
- Style must never override correctness; language idioms may differ.
- **Escalate to human review if:** confidence is low or the style judgement appears subjective.

**Score:** ___ / 15   **Evidence/notes:**

---

## 6. Total and interpretation

**Total score:** ___ / 100  *(sum of sections 1–5; must not exceed 100)*

| Band | Meaning | Guardrail |
|---|---|---|
| 85–100 | Strong technical submission | Proceed to human interview or ownership check; do not auto-hire. |
| 70–84 | Meets expected campus standard | Proceed based on overall hiring process and human review. |
| 55–69 | Partial evidence | Review failed behaviours and learning potential in a human discussion. |
| Below 55 | Insufficient evidence in submission | Do not make a final rejection solely where execution or environment confidence is low. |

---

## 7. Overall confidence and flags

- **Confidence:** High / Medium / Low
- **Review flags (if any):** e.g., environment ambiguity, disputed expected result, subjective style judgement, integrity concern.
- A total score is a recommendation input, not a final hiring decision. Any review flag or Low confidence requires human sign-off before a decision is made.

---

## 8. Structured JSON output (required)

Per the AI Judge Specification's "Structured result" stage, every evaluation must return one JSON object in the schema below, followed by the short evaluator summary from Section 6/7. The **field names/shape come from the AI Judge Specification**; the **caps/weights come from the Scoring Policy** (5 criteria, sum 100) — `ai_transparency_ownership` is kept as a field (AI use is permitted and must not reduce score) but is **not separately weighted**, so its cap is 0 and it is always reported as 0.

`question_complexity` is the `Low`/`Medium`/`High` rating assigned to the given `question_id` in the **Question Bank Reference (Section 9)**, based on algorithmic/data-structure difficulty. Copy the value as-is from Section 9; do not re-derive it.

`overall_negative_summary` is a short (1–3 sentence) prose summary consolidating the submission's key weaknesses/negatives across all criteria (distinct from the bullet-point `improvements` list — this is a narrative overview, not action items).

`ai_used` is a best-effort signal ("Yes"/"No") on whether the submission appears AI-generated rather than hand-written, with `ai_used_reason` giving the concrete indicators observed. This does **not** feed into or reduce `criterion_scores`/`total_score` (AI use is permitted per policy) — it is reported purely for transparency. Base the judgement on observable signals such as: unusually polished/idiomatic code inconsistent with a 30-minute student exercise or the candidate's other code in the same repo; boilerplate patterns typical of LLM output (e.g., excessive docstrings/comments explaining trivial lines, verbose type hints/try-except blocks not otherwise used); naming/style inconsistent across files; comments referencing an AI assistant; or a solution that is unusually optimal/idiomatic relative to the stated constraints. If signals are inconclusive, report `"No"` (do not guess) and state that evidence was inconclusive in `ai_used_reason`. **Escalate to human review if:** signals are strong but ambiguous (mark `ai_used: "Yes"` and add an `ai_usage_suspected` review flag rather than silently upgrading/downgrading the score).

`last_commit_datetime` is the timestamp of the most recent commit in the candidate's repository at the time of evaluation, taken directly from version control (e.g., `git log -1 --format=%cI`), in ISO 8601 format (`YYYY-MM-DDTHH:MM:SS±HH:MM`) including timezone where available. Report `"Unknown"` if the repository has no commit history or the timestamp cannot be read — do not estimate or guess a value.

```json
{
  "question_id": "Qxx",
  "question_complexity": "Medium",
  "repository_status": "runnable|partially_runnable|not_runnable",
  "test_summary": {"visible_passed": 0, "visible_failed": 0, "hidden_passed": 0, "hidden_failed": 0},
  "criterion_scores": {
    "functional_correctness": 0,
    "problem_interpretation": 0,
    "algorithm_data_structures": 0,
    "testing_edge_cases": 0,
    "code_quality": 0,
    "ai_transparency_ownership": 0
  },
  "total_score": 0,
  "evidence": [{"criterion": "", "file": "", "lines": "", "observation": ""}],
  "strengths": [],
  "improvements": [],
  "overall_negative_summary": "",
  "ai_used": "Yes|No",
  "ai_used_reason": "",
  "last_commit_datetime": "",
  "confidence": "High|Medium|Low",
  "review_flags": []
}
```

Caps (Scoring Policy weights): `functional_correctness <= 45`, `problem_interpretation <= 10`, `algorithm_data_structures <= 15`, `testing_edge_cases <= 15`, `code_quality <= 15`, `ai_transparency_ownership = 0` (always). `total_score` must equal the sum of `criterion_scores` and must not exceed 100.

---

## 9. Question Bank Reference (Q01–Q30)

Question bank sourced directly from the PDF files in `03 - Coding Round (G2)/Coding_Questions/` (one PDF per question, filename carries the question number). This single document is enough to prompt and evaluate. Expected deliverables for every question: source code and tests (dependency file if needed) — documentation is not required and is not evaluated.

Format per question: `ID | Title | Complexity: <value>` then Problem / Input / Output / Example / Constraints / Edge Cases / AI Focus. **Complexity** here is `Low`/`Medium`/`High`, assigned per question based on algorithmic/data-structure difficulty. It must be copied as-is into the `question_complexity` field of the JSON output (Section 8) for the corresponding `question_id`, not re-derived by the evaluator.

**Q01 | Top 3 Most Frequent Words | Complexity: Low | Repo Folder: 127156026_ASHLEY**
Read a line of text and return the top 3 most frequent alphabetic words (case-insensitive) with their counts. Ties broken alphabetically; ignore digits/punctuation/special characters. Input: one line of text (<=100,000 chars). Output: up to three `word:count` lines, lowercase, sorted by frequency desc then alphabetically. Example: `Data science uses data; science finds insight.` → `data:2`/`science:2`/`finds:1`. Edge cases: fewer than 3 unique words; ties; mixed case/punctuation. AI focus: tokenization, normalization, frequency map, deterministic sort.

**Q02 | Second Highest Distinct Value | Complexity: Low | Repo Folder: 127156150_ASHLEY**
Find the second highest distinct integer in a list and its first zero-based index, without sorting the full list. Return NA if fewer than two distinct values exist. Input: n, then n space-separated integers. Output: `value index` or `NA`. Example: `6`/`4 8 2 8 6 4` → `6 4`. Constraints: 1<=n<=100,000; values -1,000,000..1,000,000. Edge cases: duplicates of second-highest; all equal; negatives. AI focus: single-pass tracking of top-2 distinct values with first index.

**Q03 | Employee Record Deduplication | Complexity: Medium | Repo Folder: 127179066_ASHLEY**
Process `id,name,score,updated_at` records; keep only the latest valid record (0<=score<=100) per id; discard invalid scores; output retained records sorted by updated_at ascending. Input: n then n CSV records. Output: retained CSV records, or nothing if none valid. Example: `5` records → `1,Ana,90,12`/`3,Cia,75,13`/`2,Ben,88,14`. Constraints: n<=100,000. Edge cases: all records for an id invalid; duplicate updated_at; no valid records. AI focus: validation, per-id "keep latest valid", stable sort by timestamp.

**Q04 | Department Score Summary | Complexity: Low | Repo Folder: 127156062_ASHLEY, 127179036_ASHLEY**
Group `department,score` records by department; compute average (2 decimals) and max per department; sort by average desc then department name asc. Input: n then n records. Output: `department:average:max` lines. Example: `5` records → `AI:85.00:90`/`CSE:75.00:80`/`DS:75.00:75`. Constraints: n<=100,000; 0<=score<=100. Edge cases: tied averages; decimal scores; single-record department. AI focus: grouping, rounding, multi-key sort.

**Q05 | Password Strength Validator | Complexity: Low | Repo Folder: 127156116_ASHLEY**
Validate a password against 6 rules (length>=8, uppercase, lowercase, digit, special char, no spaces); output VALID/INVALID with failed rule list (in table order) and score 0-6. Input: one password line (<=1,000 chars). Output: `VALID score:6` or `INVALID:rule1,rule2,... score:n`. Example: `Campus25` → `INVALID:special score:5`. Edge cases: multiple failures; embedded spaces; empty input. AI focus: rule evaluation order, stable failure listing, scoring.

**Q06 | Sliding Window Average and Maximum | Complexity: Medium | Repo Folder: 127179065_ASHLEY**
For n numbers and window size k, output average (2 decimals) and maximum for every complete window of size k, sliding one position at a time. Input: `n k` then n numbers. Output: `average,max` per window (n-k+1 lines). Example: `5 3`/`2 4 6 8 10` → `4.00,6`/`6.00,8`/`8.00,10`. Constraints: 1<=k<=n<=100,000. Edge cases: k=1; k=n; negative/decimal values. AI focus: sliding window with O(n) max maintenance (e.g., deque), numeric precision.

**Q07 | Bracket Balance Validator | Complexity: Medium | Repo Folder: 127156067_ASHLEY**
Validate balance/nesting of `()`, `[]`, `{}`, ignoring all other characters; return BALANCED or ERROR:index for the first error (unmatched close, wrong type, or leftover open). Input: one text line (<=100,000 chars). Output: `BALANCED` or `ERROR:index`. Example: `a[(b+c)]` → `BALANCED`; `]abc` → `ERROR:0`. Edge cases: wrong-type closing; leftover opening bracket; multiple errors (report first). AI focus: stack-based matching, precise error-index reporting.

**Q08 | CSV Data Quality Report | Complexity: Medium | Repo Folder: 127179056_ASHLEY**
For a CSV table with header, compute per-column missing count and valid percentage (2 decimals). Missing = empty string, exact `NULL`, or missing trailing field in a short row. Input: header line then data rows. Output: `column:missing:valid_percentage` per column in header order. Example: `id,name,score`/3 rows → `id:0:100.00`/`name:1:66.67`/`score:1:66.67`. Constraints: <=100 columns, <=100,000 rows; no quoted commas. Edge cases: short rows; whitespace-only vs empty; fully-missing column. AI focus: ragged-row handling, missing-value rules, percentage rounding.

**Q09 | Earliest Second-Occurrence Distance | Complexity: Low | Repo Folder: 127156063_ASHLEY**
Find the value whose second occurrence appears earliest in the sequence; output that value and the distance (index difference) between its first and second occurrence; NONE if no repeats. Input: n then n integers. Output: `value distance` or `NONE`. Example: `7`/`5 1 3 4 3 5 6` → `3 2`. Constraints: n<=100,000. Edge cases: no repeats; multiple candidates competing on earliest second occurrence. AI focus: first-seen index map, comparison by second-occurrence index (not distance).

**Q10 | Daily Event Type Counter | Complexity: Medium | Repo Folder: 127156063_ASHLEY**
Parse ISO 8601 timestamps (`YYYY-MM-DDTHH:MM:SS`), extract date, group by (date, event type), count occurrences; sort by date asc then event type asc. Input: n then `timestamp,event` records. Output: `date,event,count` lines. Example: 4 records → `2026-08-20,login,2`/`2026-08-20,view,1`/`2026-08-21,login,1`. Constraints: n<=100,000. Edge cases: unsorted input; events spanning multiple years; same date/event repeated. AI focus: date extraction, two-key grouping and sort.

**Q11 | Two Sum with Deterministic Tie-Break | Complexity: Low | Repo Folder: 127156105_ASHLEY**
Find two distinct indices i<j where array[i]+array[j]=target; among multiple valid pairs choose smallest j, then smallest i; NONE if none exists. Input: `n target` then n integers. Output: `i j` or `NONE`. Example: `5 9`/`2 7 4 5 1` → `0 1`. Constraints: 2<=n<=100,000. Edge cases: multiple valid pairs with different j; no valid pair; duplicate values. AI focus: hashmap of value→earliest index, deterministic tie-break logic.

**Q12 | Merge Overlapping Intervals | Complexity: Medium | Repo Folder: No Repository Sent**
Merge intervals that overlap or touch (share an endpoint) into a minimal set of non-overlapping intervals, sorted by start. Input: n then n `start end` pairs. Output: merged `start end` lines sorted by start. Example: `4` intervals → `1 6`/`8 12`. Constraints: n<=100,000; start<=end. Edge cases: touching intervals; fully nested intervals; no overlaps at all. AI focus: sort-then-sweep merge, inclusive-touching boundary logic.

**Q13 | Flatten Nested JSON | Complexity: Medium | Repo Folder: 127179051_ASHLEY**
Flatten a nested JSON object using dot-separated keys; preserve arrays as values (do not flatten array contents); sort output keys lexicographically; empty nested objects vanish. Input: one line of JSON. Output: one line of flattened, compact JSON. Example: `{"user":{"name":"Ana"},"active":true}` → `{"active":true,"user.name":"Ana"}`. Constraints: max nesting depth 20; keys contain no dots. Edge cases: null values; empty object; deeply nested keys. AI focus: recursive flattening, key sorting, JSON serialization correctness.

**Q14 | IQR Outlier Detection | Complexity: High | Repo Folder: 127156074_ASHLEY**
Compute Q1/Q3 via median-of-halves (excluding overall median when n is odd), IQR=Q3-Q1, and flag values outside [Q1-1.5·IQR, Q3+1.5·IQR]; output outliers in original input order; NONE if none. Input: n then n numbers. Output: space-separated outlier values, or `NONE`. Example: `8`/`10 12 11 13 12 14 100 9` → `100`. Constraints: 4<=n<=10,000. Edge cases: odd-length arrays; repeated outlier values; no outliers. AI focus: correct median-of-halves quartile method, boundary math, order-preserving output.

**Q15 | Matrix Border Sum | Complexity: Low | Repo Folder: 127156011_ASHLEY**
Sum all border cells (first/last row, first/last column) of an r×c matrix, counting each cell (including corners) exactly once. Input: `r c` then r rows of c integers. Output: single integer sum. Example: `3 4` matrix → `65`. Constraints: 1<=r,c<=1,000. Edge cases: 1×1 matrix; single row or single column. AI focus: correct perimeter iteration without double-counting corners.

**Q16 | Top K Error Code Analyzer | Complexity: Medium | Repo Folder: 127156132_Ashley**
Filter log records to ERROR-level entries only, count frequency per error code, return top K codes by count desc then code asc. Input: `n k` then n `timestamp,level,error_code` records. Output: up to k `error_code:count` lines. Example: `5 2` records → `E02:2`/`E01:1`. Constraints: 1<=n<=100,000; 1<=k<=n. Edge cases: tied frequencies; no ERROR records; fewer unique codes than k. AI focus: case-sensitive filter, frequency map, multi-key sort with top-k truncation.

**Q17 | Shortest Path in Undirected Graph | Complexity: Medium | Repo Folder: 127156082_ASHLEY**
Given an undirected graph (n nodes, m edges, possibly with duplicates/self-loops), find the minimum number of edges from source to destination; -1 if unreachable. Input: `n m`, m edges, then `source destination`. Output: single integer. Example: 5 nodes/4 edges → `2`. Constraints: n,m<=50,000. Edge cases: disconnected components; duplicate edges; source==destination. AI focus: BFS shortest path, adjacency list construction, handling duplicate/self-loop edges.

**Q18 | Matrix Column Min-Max Normalization | Complexity: Low | Repo Folder: 127156096_ASHLEY**
Scale each column of a numeric matrix independently to [0,1] via min-max; constant columns (max=min) output 0.0000 for all rows; round to exactly 4 decimals. Input: `r c` then r rows. Output: r lines of c normalized values (4 decimals). Example: 3×2 matrix with one constant column → per-row normalized output. Constraints: 1<=r<=10,000; 1<=c<=100. Edge cases: constant column; negative values; single row. AI focus: per-column min/max computation, fixed-precision formatting.

**Q19 | Employee Records Multi-Key Sort | Complexity: Low | Repo Folder: 127156027_ASHLEY**
Sort `name,department,score` records by department asc, then score desc, then name asc; preserve original record format. Input: n then n records. Output: n sorted records. Example: 4 records → sorted by department, then score desc, then name. Constraints: n<=100,000; 0<=score<=100. Edge cases: full ties across all three keys; decimal scores. AI focus: stable composite-key comparator (mixed ascending/descending directions).

**Q20 | Minimum Coin Change | Complexity: High | Repo Folder: 127156113_Ashley**
Given n coin denominations (reusable unlimited times) and a target, find the minimum number of coins to make the target exactly; -1 if impossible. Input: `n target` then n denominations. Output: single integer. Example: `3 11`/`1 5 6` → `2`. Constraints: 1<=n<=100; 0<=target<=10,000; 1<=coin<=10,000. Edge cases: target=0; unreachable target; duplicate denominations. AI focus: unbounded-coin DP, impossible-case handling.

**Q21 | Consecutive Values Run Detector | Complexity: Medium | Repo Folder: Sent via email**
Given timestamped values, a threshold, and minimum run length k, find all maximal runs of consecutive values strictly greater than threshold with length>=k; output each qualifying run as `start,end,length`; NONE if none. Input: `n k threshold` then n `timestamp,value` records. Output: run lines, or `NONE`. Example: `6 2 80` records → `t2,t3,2`/`t5,t6,2`. Constraints: n<=100,000; 1<=k<=n. Edge cases: run at start/end of data; run exactly length k; no qualifying run. AI focus: single-pass run tracking, correct run-closing logic at boundaries and end of input.

**Q22 | Customer Data Cleaning Pipeline | Complexity: Medium | Repo Folder: 127156039_ASHLEY**
Trim whitespace from all fields, lowercase emails, reject records with empty id or invalid email (exactly one `@` with non-empty parts on both sides), keep latest valid record per id, output cleaned records plus quality metrics. Input: n then `id,name,email` records. Output: cleaned records, then `input:n`/`valid:count`/`rejected:count`/`duplicates_removed:count`. Example: 4 records → 2 cleaned + metrics block. Constraints: n<=20,000; no quoted commas. Edge cases: multiple valid duplicates for same id; invalid then valid duplicate; empty id after trim. AI focus: ordered validation/normalization pipeline, correct metric definitions (rejected vs duplicates_removed).

**Q23 | Longest Consecutive Sequence | Complexity: Medium | Repo Folder: 127156021_ASHLEY**
Find the length of the longest run of consecutive integers (e.g., 1,2,3,4) present in an unsorted list; numbers need not be adjacent in the input; duplicates ignored. Input: n then n integers. Output: single integer length. Example: `6`/`100 4 200 1 3 2` → `4`. Constraints: n<=50,000. Edge cases: duplicates; negative numbers; all-unique single-length sequences. AI focus: O(n) approach using a value set and sequence-start detection (avoid O(n log n) sort as the only solution... though sorting is acceptable for correctness, efficient set-based approach is preferred).

**Q24 | Graph Connected Components Analysis | Complexity: Medium | Repo Folder: 127156072_ASHLEY**
Given an undirected graph (n nodes, m edges, with possible self-loops/duplicates), find the number of connected components and the size of each, sorted descending. Input: `n m` then m edges. Output: component count, then space-separated sizes descending. Example: `6 3` edges → `3`/`3 2 1`. Constraints: n,m<=50,000. Edge cases: isolated nodes; self-loops; fully connected graph. AI focus: DFS/BFS or union-find for component discovery, correct handling of isolated nodes.

**Q25 | LRU Cache Implementation | Complexity: High | Repo Folder: 127156149_ASHLEY**
Implement a fixed-capacity LRU cache supporting GET (return value or -1, marks key as most-recently-used) and PUT (insert/update, evicts least-recently-used at capacity). Input: `capacity q` then q commands (`GET key` / `PUT key value`). Output: one line per GET. Example: capacity 2, 6 ops → `10`/`-1`/`30`. Constraints: capacity<=1,000; q<=10,000. Edge cases: capacity=1; updating existing key (no eviction); repeated GET on same key. AI focus: O(1) get/put via hashmap + doubly-linked-list (or equivalent), correct recency updates on both operations.

**Q26 | JSON Record Filter with Compound Conditions | Complexity: Medium | Repo Folder: 127156103_ASHLEY**
Filter flat JSON records against exactly two AND-joined conditions supporting `=, !=, >, >=, <, <=` (numeric) and `=, !=` (string, case-sensitive); output matching records in original order. Input: n then n flat JSON lines, then a filter expression line. Output: matching JSON lines in original order, or nothing. Example: 3 records + `score >= 80 AND name != Ana` → 1 matching record. Constraints: n<=5,000; JSON is flat (no nesting/arrays). Edge cases: numeric vs string field type dispatch; boundary comparisons (>=, <=); no matches. AI focus: simple filter-expression parsing, correct operator/type dispatch, AND-only compound logic.

**Q27 | Binary Tree Level Sum Calculator | Complexity: Medium | Repo Folder: 127156040_ASHLEY**
Given a binary tree in level-order array form with `null` markers (child at 2i+1/2i+2), compute the sum of node values at each non-empty level. Input: one line of space-separated values/`null`. Output: one sum per non-empty level, root to leaves. Example: `1 2 3 null 4 5 6` → `1`/`5`/`15`. Constraints: 0<=total_nodes<=50,000. Edge cases: empty tree (no output); single node; levels with mixed null/value entries. AI focus: level-order tree reconstruction from array indices, correct null-skipping and level-sum aggregation.

**Q28 | Longest Substring Without Repeating Characters | Complexity: Medium | Repo Folder: 127156100_ASHLEY**
Find the longest substring (case-sensitive) with all-unique characters; return its length and 0-based starting index; ties broken by smallest starting index. Input: one line (string, may be empty). Output: `length start_index`. Example: `abcabcbb` → `3 0`. Constraints: 0<=length<=100,000. Edge cases: empty string; all-identical characters; multiple substrings tied for max length. AI focus: sliding window with last-seen-index map, O(n) complexity, tie-break by earliest start.

**Q29 | Minimum Meeting Rooms | Complexity: Medium | Repo Folder: 127156017_ASHLEY**
Given n meeting intervals `[start, end)`, find the minimum number of rooms needed so no two meetings in the same room overlap; a meeting ending at t does not conflict with one starting at t. Input: n then n `start end` pairs. Output: single integer. Example: 4 meetings → `2`. Constraints: n<=100,000; 0<=start<end<=1,000,000. Edge cases: all meetings overlapping; meetings touching exactly at boundaries; single meeting. AI focus: event-sorting or min-heap sweep, correct end-before-start-at-same-time tie handling.

**Q30 | Linked List Cycle Entry Detection | Complexity: High | Repo Folder: Sent via email**
Given an array-based singly linked list (`next[i]`, `-1` = null) and a head index, detect whether a cycle exists and return the 0-based index where it begins; -1 if none. Input: `n head` then n next-pointers. Output: single integer (cycle entry index or -1). Example: `5 0`/`1 2 3 1 -1` → `1`. Constraints: n<=100,000; 0<=head<n. Edge cases: self-loop (node points to itself); head node inside the cycle; no cycle (list terminates at -1). AI focus: Floyd's cycle detection (tortoise-and-hare) or visited-set approach, correct entry-point calculation.

---

## Ground rules for every evaluation

1. Evaluate only the submitted artefacts against the exact question and this policy. Do not infer personality, intelligence, intent, demographic attributes, institution quality, or employability.
2. AI tool use by the candidate is permitted and must not reduce the score. Do not treat AI-generated-code detectors as proof of misconduct — flag integrity concerns for human review instead.
3. Cite specific repository file paths and line ranges for qualitative observations (algorithm, code quality).
4. Do not create new criteria or alter the weights above.
5. Record the final result for this question in the Evaluator Scorecard tab: Candidate ID, Question ID, the five scores (Functional Correctness/45, Interpretation/10, Algorithm/15, Testing/15, Code Quality/15), Total/100, AI Confidence, and Human Review Notes.

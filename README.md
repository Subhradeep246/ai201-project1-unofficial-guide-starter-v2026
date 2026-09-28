# The Unofficial Guide

**Subhradeep Acharjee — `campus_life` corpus**

---

# Unit 1

## What This Does

I used the `campus_life` corpus to build a guide that answers practical
questions students might have about campus. The 88 posts cover things like
dining halls, housing, classes, transportation, and study spaces. When someone
asks a question, the program finds the most relevant posts and uses them to
write an answer with a source. If the question is not covered by the corpus,
the program says it does not have enough information instead of guessing.

## Chunking Strategy

**Chunk size:** 600 characters (a ceiling; each source post remains one chunk)
**Overlap:** 0 characters

I noticed that these documents are already very short. They average 317
characters, and even the longest one is only 549 characters. Most of them also
cover one topic from beginning to end, so splitting them would separate a fact
from useful context such as the post title. I decided to keep each post as one
chunk. I set the size to 600 characters so the longest post fits, and I used no
overlap because it would only repeat the same information.

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:** Is the housing lottery completely random, and when are numbers released?

**Answer:**

```
No, the housing lottery is not completely random; rising sophomores get a random number, but juniors and seniors are ordered by accumulated credit hours first with random tie-breaks. Numbers are released the second week of March. (Source: admin_housing_lottery.txt)

Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, dining_the_atrium_followup.txt, housing_morrow_house.txt
```

**My relevance cutoff:** `0.65`

There was a clear difference between the two groups of questions. The five
questions that the corpus could answer had distances between 0.2101 and
0.4296. The five unrelated questions had distances between 0.8246 and 0.9340.
I chose 0.65 because it sits comfortably in the gap between those groups.

| Question | In corpus? | Best distance |
|---|---|---|
| Is the housing lottery completely random, and when are numbers released? | Yes | 0.2441 |
| Which two orientation sessions are most worth attending? | Yes | 0.3653 |
| How long is the lunch wait at Kestrel Commons, and when is it shorter? | Yes | 0.2101 |
| How far ahead can group study rooms be booked, and what is the weekly limit? | Yes | 0.2066 |
| How often does the campus shuttle run on weekdays and weekends? | Yes | 0.4296 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

## How I Used AI

**1.** My first set of test questions included exam deadlines, general
academic resources, and sports facilities. I asked Codex to check whether the
corpus actually covered them. It pointed out that those answers were not in
the documents, so I replaced them with more specific questions about the
housing lottery, orientation, dining, study rooms, and the shuttle. I opened
the source files afterward and checked each expected answer myself.

**2.** I also asked Codex to help me understand whether the starter chunk size
made sense for this corpus. It calculated that the 88 documents average 317
characters and that the longest is 549. Based on that, I kept each post as a
single chunk and removed the overlap. I then checked five printed samples and
verified that all 88 chunks matched the complete original posts.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

## Run Log — Before

Produced by `python run_eval.py --label before`. Raw answers:
`results/run_2026-09-27_2101_before.md` from `run_eval.py::main`.
Retrieval is `store.py::search`. Chunks are `chunker.py::split_documents`.

I scored each criterion against the target in `criteria.md`, by reading the
answers and retrieved sources. `scorer.py` is stricter than criterion 5
(RapidFuzz 95 treats `your transcript` / `unofficial transcripts` as misses),
so I did not copy its pass/fail column into this table.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks preserve complete posts | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answers include the expected factual detail | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Criterion 1, 3, and 4 are the same in every column because retrieval, the
gate, and chunking do not change between runs. Criterion 3 is one
deterministic pass, copied into all three columns as the assignment asks.

### Criterion 1 — one run of retrieved sources

Produced by `store.py::search`. The answering file is in the top 5 for every
question. Distances from run 1 of `results/run_2026-09-27_2101_before.md`:

```
CS 210 exams          0.299  course_cs_210_exams.txt, course_cs_210.txt, ...
Withdrawal            0.294  admin_add_drop_deadline.txt, admin_withdrawal_deadline.txt, ...
Pass/fail             0.251  admin_pass_fail_option.txt, admin_add_drop_deadline.txt, ...
Transcripts           0.250  admin_transcript_requests.txt, admin_add_drop_deadline.txt, ...
Morrow House laundry  0.246  housing_morrow_house_laundry.txt, housing_old_brewhouse_laundry.txt, ...
```

The withdrawal answer lives in `admin_withdrawal_deadline.txt`, which came
back **second**. Rank 1 was `admin_add_drop_deadline.txt`, which is about
dropping, not withdrawing.

### Criterion 2 — source named in the answer

Produced by `generate.py::answer_from_chunks`. Run 1, pass/fail question:

```
You can declare a course as pass/fail as late as week eight. A pass requires
a grade of C- or better, and the usage limits are a maximum of two per year
and eight across a degree (admin_pass_fail_option.txt).
```

All 15 answers in the before log name at least one `.txt` filename.

### Criterion 3 — out-of-scope gate

Produced by `run_eval.py::check_out_of_scope` and `gate.py::check`, cutoff 0.65:

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

The refusal text from `gate.py` is: `I don't have enough information about that.`

### Criterion 4 — sampled chunks

Produced by `python app.py chunks` → `chunker.py::split_documents`. Same five
stride samples as in Unit 1. Each one is a complete post with its title and
no cut-off sentence:

```
admin_add_drop_deadline.txt#0
course_biol_160.txt#0
course_hist_118_workload.txt#0
dining_pellew_dining_hall_followup.txt#0
housing_innisfree_hall.txt#0
```

Example (`admin_add_drop_deadline.txt#0`):

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer
window — through the end of week six — but a drop after week two shows as a W
on your transcript. Nothing anywhere on the registrar's site says this
plainly, and students find out from each other.
```

### Criterion 5 — expected facts in the answer

Produced by `generate.py::answer_from_chunks`. Run 1, transcripts:

```
Official transcripts cost $8 and take three business days electronically or
ten days by post. Unofficial transcripts are free and instant from the
student portal.

Source: admin_transcript_requests.txt
```

`scorer.py` marked this fail because it wanted the phrase `unofficial ones`.
The facts are all present. I counted it as a hit under the original criterion
("minor wording and punctuation differences are allowed").

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | All three runs were 5/5. The answering post was in the retrieved set every time, including withdrawal (rank 2) and laundry (rank 1). Target was 4 of 5. |
| 2 | Every answer names a source | MET | All 15 answers name a retrieved `.txt` file. Target was 5 of 5. |
| 3 | Gate stops out-of-corpus questions | MET | 5 of 5 refused, distances 0.825–0.934, all above 0.65. Target was 4 of 5. |
| 4 | Sampled chunks preserve complete posts | MET | All 5 stride samples are whole posts with titles. Target was 5 of 5. |
| 5 | Answers include the expected factual detail | MET | Reading every answer, all 15 contain the facts in `questions.py`. The two RapidFuzz fails (`unofficial ones` vs `unofficial transcripts`; `the transcript` vs `your transcript`) are wording, which the original criterion allows. Target was 4 of 5. |

## Diagnoses

I missed none of the five targets.

The targets were set low for this corpus. Whole-post chunking means criterion 1
is mostly "did the right filename appear in the top 5?", and 4 of 5 is a
forgiving bar when every in-scope question already sits well under 0.65.
Criterion 5 at 4 of 5 also leaves room for a full miss I did not actually
have.

The weakness that did show up, even though it did not miss a target:

**Retrieval, not generation.** The withdrawal question asks about both the
drop deadline and withdrawal. Semantic search ranked `admin_add_drop_deadline.txt`
first (0.294) and the post that actually answers the question,
`admin_withdrawal_deadline.txt`, second (0.319). The model still wrote the
right answer because the correct chunk was in the prompt, but rank 1 is the
wrong administrative lookalike. If I had written criterion 1 as "the top
result contains the answer," this question would have missed.

A second, smaller pattern: several laundry posts share the same washer count
and the same Tuesday / Sunday wording. Criterion 1 cannot tell Morrow House
apart from Old Brewhouse on those facts. That is a measurement problem as much
as a retrieval problem.

If I had to tighten one target now, I would change criterion 1 to: *for at
least 4 of 5 questions, the top-1 chunk contains the answer.* That is the
check this run would have been close on.

## The Improvement

**What I changed:** Hybrid search in `store.py::search`. Semantic cosine
retrieval and BM25 keyword retrieval are fused with reciprocal rank fusion.
The cosine distances on the returned rows are unchanged, so `gate.py` still
uses the same cutoff.

**Why I picked it:** The withdrawal miss-that-wasn't is a retrieval ranking
problem: the question uses the exact words "course-drop deadline" and
"withdraw," and meaning-only search preferred the drop post. Keyword search
is the Milestone 4 option aimed at exact terms like that.

### Run Log — After

Produced by `python run_eval.py --label after` after the hybrid change.
Raw answers: `results/run_2026-09-27_2106_after.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks preserve complete posts | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answers include the expected factual detail | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

After, withdrawal still retrieves `admin_add_drop_deadline.txt` first and
`admin_withdrawal_deadline.txt` second. Morrow House laundry is still rank 1.
The gate still refuses 5 of 5 at the same distances.

Laundry run 1 after (`generate.py::answer_from_chunks`):

```
At Morrow House, there are eight washers and six dryers. The best time to do
laundry is Tuesday or Wednesday morning, and the worst time is Sunday after
6 pm, when you will have to wait.

Source: housing_morrow_house_laundry.txt
```

`scorer.py` marked this fail (`6pm` vs `6 pm`). The facts are the same. I
still count it as a hit for criterion 5.

**Did it help?** No, not on the failure I pointed it at. I wanted hybrid
search to move `admin_withdrawal_deadline.txt` to rank 1. I checked BM25
alone on that question: it also ranks the drop-deadline post first (score
21.05 vs 19.57), because the question leads with "course-drop deadline."
Fusing two rankings that agree cannot swap them. The criterion table did not
move. I know because I compared ranks and distances before and after, and
because the after gate table is identical.

## What's Still Broken

No original target is still missed. What is still wrong:

1. **Withdrawal ranking.** Top-1 is still the drop-deadline post. Next I
   would try a prompt or query rewrite that asks retrieval for "withdrawal
   deadline," or a simple filter that prefers a filename matching a key noun
   in the question. I stopped after one change because a second retrieval
   tweak would make it impossible to tell what moved the numbers.

2. **Template-duplicate laundry posts.** Several buildings share the same
   washer count and the same best/worst times. A tighter criterion 1 cannot
   be scored from `expects` alone. I would add the building name to `expects`
   or judge by source filename. I stopped because that is a measurement
   change, not the hybrid-search experiment.

3. **The automated scorer is harsher than criterion 5.** I left the RapidFuzz
   threshold where it is. Lowering it to make the eval script print `pass`
   would hide the wording issue instead of recording it.

## What I'd Do Differently

I would rewrite criterion 1 as: *for at least 4 of 5 questions, the top-1
retrieved chunk contains the answer.* "Somewhere in the top 5" was true on
this corpus before I ran anything, so it did not put pressure on ranking.

I would also write criterion 5's expected facts as the exact numbers only
(`week ten`, `$8`, `8 washers`) and judge those by hand, instead of long
phrases that a correct paraphrase can miss in an automated checker.

## How I Used AI (this unit)

I used Cursor to run `run_eval.py`, to print BM25 ranks next to cosine ranks,
and to draft `store.py` hybrid search. I scored every criterion myself by
reading `results/run_2026-09-27_2101_before.md` and
`results/run_2026-09-27_2106_after.md`. When the eval script said the
transcript and laundry answers failed, I checked the RapidFuzz scores and
kept the reading-based verdict. I also asked it why hybrid search might not
move the withdrawal post; the BM25 scores (drop-deadline still first) are
what decided that it had not helped.

# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
My questions cover several different parts of campus life. Four have one main
source, while the Kestrel Commons question can match either the original post
or its follow-up. I chose four out of five because I expect retrieval to work
most of the time, but I do not want to assume it will be perfect.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Every retrieved chunk already includes its source filename, so the system has
the information it needs to cite a source every time. Without that source, a
student would have no easy way to check the answer, so I want all five answers
to include one.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
I will choose the cutoff after comparing the five test questions with five
unrelated questions. I am allowing one miss because common words such as
"student," "course," and "campus" could make an unrelated question look more
relevant than it really is.

---

## 4. Sampled chunks preserve complete posts

All 5 sampled chunks contain one complete source post, including its title,
with no sentence cut off at either end.

**Why this target:**
The documents are short posts, and the longest one is only 549 characters.
Keeping a whole post together preserves its title and surrounding context. If
one of the samples cuts off a sentence, that would show that my chunking choice
is not working as intended.

---

## 5. Answers include the expected factual detail

At least 4 of the 5 test answers contain the expected fact recorded beside the
question in `questions.py` (minor wording and punctuation differences are
allowed).

**Why this target:**
The questions ask for specific times, limits, or session names, so a vague
answer would not be very helpful. I chose four out of five because the model's
wording may vary, even when it receives the correct source, but it should still
get the important fact right most of the time.

> **Revised in unit 2:** Same target — at least 4 of 5 answers contain every
> expected fact from `questions.py`. I score this by reading the answer and
> allowing minor wording (`ten days by post` for `ten by post`, `your
> transcript` for `the transcript`). I do not treat a RapidFuzz score under 95
> as a miss when the fact is clearly there.
>
> **Why revised:** The original criterion already said minor wording is
> allowed, but `scorer.py` at threshold 95 could not measure that the same way
> twice. Two answers that a person would mark correct failed the automated
> check. The target did not change; only the measurement did.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->

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
The five questions ask for facts in different parts of the campus-life corpus.
Four are each answered by one clearly named document, while the Kestrel Commons
question has both an original post and a follow-up that retrieval may rank in
either order. I expect the top five results to cover at least four questions
reliably without assuming retrieval will be perfect.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
The generation prompt receives source metadata with every retrieved chunk, so
naming a source is possible for every answer rather than only for the easiest
questions. A missing source would make the answer hard to verify, so anything
below five out of five is not acceptable.

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
I will set the cutoff from the ten measured best distances in Milestone 4. I am
allowing one miss because short campus posts share broad words such as
"student," "course," and "campus" with unrelated questions, which can make one
out-of-corpus query look closer than it really is.

---

## 4. Sampled chunks preserve complete posts

All 5 sampled chunks contain one complete source post, including its title,
with no sentence cut off at either end.

**Why this target:**
The campus-life documents are short posts (the longest is 549 characters) and
their useful fact usually sits in one sentence. Keeping each post intact
preserves its context and makes a partial sentence in any sampled chunk a sign
that the chunker is doing the wrong thing for this corpus.

---

## 5. Answers include the expected factual detail

At least 4 of the 5 test answers contain the expected fact recorded beside the
question in `questions.py` (minor wording and punctuation differences are
allowed).

**Why this target:**
These questions ask for concrete times, limits, or named sessions, so a fluent
but vague response is not useful. I chose four rather than five because model
wording can vary even when retrieval supplies the correct post, while four of
five still requires accurate coverage across several kinds of campus facts.

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

# a⁵ + b⁵ = c⁵ + d⁵ : no solution below 10³⁴

**Julien Courties, 2026.** Computational result on OEIS sequence [A046881](https://oeis.org/A046881) (*smallest number that is the sum of two positive distinct n-th powers in two different ways*): the term a(5), if it exists, satisfies

> **a(5) > 10³⁴**, that is, no integer N ≤ 10³⁴ can be written as a⁵ + b⁵ = c⁵ + d⁵ with 0 < a < b, 0 < c < d and {a, b} ≠ {c, d}.

Previous bounds: Randy Ekl, 1998 (> 4.01·10³⁰, *Math. Comp.* 67, Table 9); Stuart Gascoigne, 2002 (> 3.26·10³², exhaustive search, reported on Christian Boyer's page *Squares of Cubes*); Julien Courties, Nov. 2020 (> 10³³, comment in A046881). The present search extends the bound by a factor of 10.

**Status.** Computational result, not peer reviewed. A negative result of this kind has no certificate: its credibility rests on the program, on the completeness argument of the method, on the reproducibility information below, and on independent re-runs. The author would welcome any independent verification.

## What was searched, exactly

<!-- TO CONFIRM BY THE AUTHOR before publishing -->
- Equation: a⁵ + b⁵ = c⁵ + d⁵, positive integers, 0 < a < b, 0 < c < d, {a, b} ≠ {c, d}.
- Bound: every sum a⁵ + b⁵ ≤ 10³⁴ was generated (hence b ≤ 6 309 573, since 6 309 573⁵ ≤ 10³⁴ < 6 309 574⁵) and no sum appeared twice.
- Previous search bound: 10³³ (same author, 2020), so the new range is 10³³ < N ≤ 10³⁴.

## Method

<!-- TO BE COMPLETED BY THE AUTHOR: describe the algorithm as it is implemented in src/Taxicab.cpp -->
- Arithmetic: GNU MP (GMP) big integers (a fifth power of a 7-digit number has up to 34 digits; it does not fit in 64 bits, and a sum of two does not fit in 128 bits without care).
- Enumeration: *describe here* (for example, meet-in-the-middle by residues, or the heap/priority-queue merge of all sums in increasing order; say why every pair (a, b) with a⁵ + b⁵ ≤ 10³⁴ is generated exactly once and why two equal sums cannot be missed).
- Filters: *describe here* (for example, congruence filters modulo small primes that discard most candidate pairs before any big-integer arithmetic; say why a filter never discards a true solution).

## Reproducibility

<!-- TO BE COMPLETED BY THE AUTHOR -->
- Program: `src/Taxicab.cpp`, Visual C++ (Visual Studio 2017 or later) with the GMP library; single file.
- Hardware and running time: *CPU, number of cores, wall-clock time, dates of the run*.
- Parameters of the run and command line used: *…*.
- Output produced by the program at the end of the run (the log confirming the range covered and the absence of solutions): `results/run_log.txt` (*to add*).

## Independent checks provided here

- `tools/check_small_bound.py` (Python, standard library): an independent, naive enumeration of all sums of two positive distinct n-th powers up to a bound given on the command line, which reports every repeated sum. It rediscovers 1729 = 1³ + 12³ = 9³ + 10³ and 635 318 657 = 59⁴ + 158⁴ = 133⁴ + 134⁴, and finds no fifth-power solution up to the small bounds it can reach (about 10¹⁶ in a few minutes). It validates the statement being tested, not the 10³⁴ computation itself.
- Re-running `src/Taxicab.cpp` is the only complete check of the claim.

## How to cite

Julien Courties, *a⁵ + b⁵ = c⁵ + d⁵: no solution below 10³⁴*, GitHub repository, 2026. OEIS A046881, comment of Nov. 2020 (bound 10³³) and the present repository (bound 10³⁴).

## AI assistance

<!-- adjust to the facts -->
The search program was written by the author. This repository (documentation, checking script, layout) was prepared with the assistance of Claude (Anthropic). The author takes responsibility for the result.

## Licence

Code: MIT. Data and documentation: CC0.

---

### Résumé en français

Aucun entier N ≤ 10³⁴ n'est somme de deux puissances cinquièmes positives distinctes de deux façons différentes : le terme a(5) de la suite OEIS A046881, s'il existe, dépasse 10³⁴. Bornes précédentes : Ekl 1998 (4,01·10³⁰), Gascoigne 2002 (3,26·10³²), Courties 2020 (10³³, commentaire dans A046881). Résultat calculatoire, non relu par des pairs ; le programme (`src/Taxicab.cpp`, Visual C++ et GMP) et les informations de reproduction sont fournis.

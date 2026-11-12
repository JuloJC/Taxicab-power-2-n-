# a⁵ + b⁵ = c⁵ + d⁵ : no solution up to 10³⁵

**Julien Courties, 2026.** Computational result on OEIS sequence [A046881](https://oeis.org/A046881) (*smallest number that is the sum of two positive distinct n-th powers in two different ways*): the term a(5), if it exists, satisfies

> **a(5) > 10³⁵**, that is, no integer N ≤ 10³⁵ can be written as N = a⁵ + b⁵ = c⁵ + d⁵ with 0 < a < b, 0 < c < d and {a, b} ≠ {c, d}.

| Bound | Who | Year |
|---|---|---|
| a(5) > 4.01·10³⁰ | Randy L. Ekl, *Math. Comp.* 67 (1998), 1309–1315, Table 9 | 1998 |
| a(5) > 3.26·10³² | Stuart Gascoigne, exhaustive search (reported on Christian Boyer's page *Squares of Cubes*) | 2002 |
| a(5) > 10³³ | Julien Courties, comment in A046881 | 2020 |
| a(5) > 10³⁴ | Julien Courties, this repository | 2026 |
| **a(5) > 10³⁵** | **Julien Courties, this repository** | **Nov. 2026** |

The new bound extends the published one (Ekl 1998) by a factor of about **25 000**, and the previous exhaustive search (Gascoigne 2002) by a factor of about 300.

**Status.** Computational result, not peer reviewed. A negative result of this kind has no certificate: its credibility rests on the program, on the completeness argument of the method below, on the reproducibility information, and on independent re-runs. Independent verification is welcome.

## What was searched, exactly

- Equation: a⁵ + b⁵ = c⁵ + d⁵ in positive integers, 0 < a < b, 0 < c < d, {a, b} ≠ {c, d}.
- Range of this run: every pair (a, b) with **4.01·10³⁰ < a⁵ + b⁵ ≤ 10³⁵** was generated, and no sum occurred twice. Sums N ≤ 4.01·10³⁰ are covered by Ekl's published search.
- Size: b ≤ 9 999 999 (since 10 000 000⁵ = 10³⁵ exactly, b = 10⁷ would force a = 0); about **4.7·10¹³ pairs (a, b)** were enumerated.

## Method (program `src/Recherche_a5b5_rapide.cpp`)

- **Exact arithmetic without GMP.** Every fifth power and every sum is computed exactly on 128-bit unsigned integers (`unsigned __int128`, or an equivalent two-word type under Visual C++). The largest sum, 10³⁵, is far below 2¹²⁸ ≈ 3.4·10³⁸: no overflow is possible.
- **Slices.** The range of sums is cut into consecutive slices (N_i, N_(i+1)], each holding about the same number of pairs. Two pairs with the same sum lie in the same slice, so slices can be processed independently. For each a, the values of b whose sum falls in the slice are computed exactly.
- **Meet in the middle, one pass.** Within a slice, all pairs (a, b) are inserted into an open-addressing hash table (8 bytes per slot: a 32-bit fingerprint of the exact sum and the value a), filled by all cores without locks. Two pairs with equal sums have the same key, hence the same probe sequence; since nothing is ever deleted, the second pair necessarily meets the first one: **an equal sum cannot be missed.**
- **No false solution.** A fingerprint already present is only a *candidate*; it is re-checked exactly on 128 bits, and only an exact equality is reported. Coincidences of fingerprints (a few per slice) are rejected and counted; their presence in the log is itself a sign that the detection works.
- **Resume.** Progress is saved after each completed slice (`a5b5_record_progres.txt`); a restarted run continues from the last completed slice, and the program only ever reports the bound up to which the search is *complete*.

## Validation

- **Built-in self-tests** (run at every start; the search does not begin if one fails): rediscovery of 1729 = 1³ + 12³ = 9³ + 10³ and 635 318 657 = 59⁴ + 158⁴ = 133⁴ + 134⁴; number of pairs enumerated equal to a direct count; slice boundaries without loss or duplication.
- **Independent audit (Nov. 2026)**, by compiling the program with an independent test harness:
  - complete list of numbers with two representations as sums of two cubes up to 2·10⁸: 696 numbers, **identical** to a naive independent enumeration;
  - same for fourth powers up to 3·10⁹: identical;
  - adversarial boundary test: 1729 is found in the slice (0, 1729] and not in (1729, 10⁵], and 4104 is found next;
  - resume test: a search split in two through the progress file gives exactly the same solutions as a single run;
  - all of the above repeated with 4 threads (concurrent lock-free insertion): identical results.
- `tools/check_small_bound.py` (Python, standard library): naive independent enumeration for small bounds; rediscovers the known cube and fourth-power solutions. It validates the statement being tested, not the 10³⁵ computation itself.

## Reproducibility

- Program: `src/Recherche_a5b5_rapide.cpp`, single file, Visual C++ (Visual Studio 2017 or later), no external library.
- Command line: `Recherche_a5b5_rapide <start> <end> <threads> <memory in GB>`, here `4.01e30 1e35`.
- Run: about one week of wall-clock time, November 2026, on the author's PC — **[CPU, number of cores, RAM]**.
- Log: `results/run_log_1e35.txt` — final console lines and progress file, ending with *"Recherche COMPLETE pour toutes les sommes N ≤ 1e35"*.

## Remark

A standard heuristic (treating sums of two fifth powers as random integers) predicts a finite expected number of solutions in total, concentrated at small sizes; the expected number above 10³⁵ is of order 10⁻⁷. The conjecture that a(5) does not exist is therefore strongly supported, but a computation can only push the bound.

## How to cite

Julien Courties, *a⁵ + b⁵ = c⁵ + d⁵: no solution up to 10³⁵*, GitHub repository JuloJC/Taxicab-power-2-n-, 2026. See also OEIS A046881.

## AI assistance

The search program was written by the author with the assistance of Claude (Anthropic), which also performed the independent audit described above and prepared this documentation. The author takes responsibility for the result.

## Licence

Code: MIT. Data and documentation: CC0.

---

### Résumé en français

Aucun entier N ≤ 10³⁵ n'est somme de deux puissances cinquièmes positives distinctes de deux façons différentes : le terme a(5) de la suite OEIS A046881, s'il existe, dépasse 10³⁵. Bornes précédentes : Ekl 1998 (4,01·10³⁰), Gascoigne 2002 (3,26·10³²), Courties 2020 (10³³) et 2026 (10³⁴). Environ 4,7·10¹³ couples (a, b) ont été énumérés, en arithmétique exacte sur 128 bits, sans GMP ; le programme a été audité par des contrôles indépendants. Résultat calculatoire, non relu par des pairs.

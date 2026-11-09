#!/usr/bin/env python3
"""Independent naive check: all sums x^n + y^n (0 < x < y) up to BOUND, report every sum obtained in two different ways.
Usage: python3 check_small_bound.py n BOUND      e.g.  python3 check_small_bound.py 3 2000   /  python3 check_small_bound.py 4 1e9  /  python3 check_small_bound.py 5 1e16
Standard library only. This validates the statement (and finds the known solutions for n = 3 and n = 4); it cannot reach 10^34 for n = 5."""
import sys, time
n = int(sys.argv[1]); bound = int(float(sys.argv[2])); t0 = time.time()
ymax = 1
while (ymax + 1) ** n < bound: ymax += 1
seen = {}; found = []
for y in range(2, ymax + 1):
    yn = y ** n
    for x in range(1, y):
        s = x ** n + yn
        if s > bound: break
        if s in seen: found.append((s, seen[s], (x, y)))
        else: seen[s] = (x, y)
print("n = %d, bound = %d, pairs generated = %d, time %.1f s" % (n, bound, len(seen) + len(found), time.time() - t0))
if found:
    for s, p, q in sorted(found): print("  %d = %d^%d + %d^%d = %d^%d + %d^%d" % (s, p[0], n, p[1], n, q[0], n, q[1], n))
else: print("  no sum obtained in two different ways up to the bound")

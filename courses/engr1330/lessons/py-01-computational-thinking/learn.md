## Why it matters

Programming is writing code; **computational thinking** is the approach behind it: breaking a problem down so a
computer can carry out the solution step by step. Exam 1 asks for its vocabulary, and every later unit uses it.

## 1. The four pillars

1. **Decomposition**: split a complex problem into smaller sub-problems (a report → introduction, body, conclusion;
   a panorama → take overlapping photos, then stitch them).
2. **Pattern recognition**: spot what problems have in common so one solution works for all (every uploaded photo
   needs the same metadata, compression and storage steps).
3. **Abstraction** (data representation): keep the characteristics that matter and drop the rest (a student record
   needs ID and name, not shoe size).
4. **Algorithms**: write step-by-step instructions in the right order (fill kettle, boil, pour, add tea bag, steep
   3 minutes, remove bag).

## 2. The computational problem-solving method

1. **Define the problem** explicitly.
2. **Gather information**: inputs, governing equations or principles, required outputs.
3. **Generate and evaluate solutions**: work a small example by hand.
4. **Implement**: turn the method into code.
5. **Verify**: test the code against the hand example, then use it on the real problem.

## 3. From algorithm to program

A **program** is an algorithm written in a syntax the computer understands. Data lives in memory; a **variable**
is a friendly name for a memory location. Example: the mean of five numbers.

```python
nums = [4.0, 8.5, 6.0, 10.0, 1.5]       # inputs (by hand: total 30, mean 6)
mean = sum(nums) / len(nums)            # governing equation: mean = total / count
print("mean:", mean)                     # output, checked against the hand answer
```

```text
mean: 6.0
```

**CCMR** (Copy, Cite, Modify, Run): much of engineering coding adapts an existing solution. Copy it, **cite** the
source, modify it (with comments noting your changes), run it on your problem.

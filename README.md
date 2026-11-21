# ASPHW5

Both programs solve the “Who Is Left?” elimination problem by simulating the rounds on a list of people numbered from `1` to `n`. It prints the number of the person who remains.

# Part 1: Functional Implementation with Haskell

## How to Run

From the repository root, run:

```sh
runghc imperative/whoisleft.hs
```

Enter a positive integer when prompted. For example, with input `10`, the program prints `3`:

```text
10
3
```

## How the Code Works

`numleft :: Int -> [Int]` takes the starting count and returns a list containing the survivor. For `n <= 0`, it returns an empty list so the program can report invalid input instead of entering the elimination loop.

For a positive `n`, `numleft` starts a local recursive function, `go`, with the list `[1..n]` and phase `0`. `go` stops when the list contains one person. Otherwise, it:

1. Uses `zip [1..] xs` to pair every person with their position in the current round.
2. Uses `filter (keep phase)` to retain positions allowed by this round's rule.
3. Uses `map snd` to remove the temporary positions and keep only the person numbers.
4. Advances the phase with `(phase + 1) mod 3`, cycling through phases `0`, `1`, and `2`.

`keep` defines the rule for each phase: phase `0` keeps odd positions, phase `1` keeps even positions, and phase `2` keeps positions not divisible by `3`. Since each round zips the current list with `[1..]`, positions restart at `1` after every elimination.

`main` reads an integer from standard input and calls `numleft`. It prints the remaining number when there is one, or asks for a positive integer when the result is empty.

For input `10`, the successive lists are `[1,3,5,7,9]`, `[3,7]`, `[3,7]`, and `[3]`. The final list has one element, so `3` is printed. The solution simulates the eliminations using list operations rather than a closed-form formula.

## Example Result

![Example result for the functional implementation](imperative/img/result_funct_nonmath.png)
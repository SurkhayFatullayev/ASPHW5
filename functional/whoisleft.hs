numleft :: Int -> [Int]
numleft n
  | n <= 0 = []
  | otherwise = go [1..n] 0
  where
    -- base case
    go [x] _ = [x]

    go xs phase =
    -- we take snd since we need to remap values since their number order becomes wrong after each run
      go (map snd (filter (keep phase) (zip [1..] xs)))
         ((phase + 1) `mod` 3)
         
    -- condition statements for phases
    keep phase (pos, _) =
      case phase of
        0 -> pos `mod` 2 /= 0
        1 -> pos `mod` 2 == 0
        2 -> pos `mod` 3 /= 0

main :: IO ()
main = do
    -- Removed annoying error with head by checking that number provided is positive
    n <- readLn
    case numleft n of
        [remaining] -> print remaining
        _ -> putStrLn "Please enter a positive integer."

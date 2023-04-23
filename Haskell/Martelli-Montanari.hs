module Martelli-Montanari where

import Data.Char
import Data.Either

data Tree = Node String [Tree] | Var String deriving (Show, Eq)

countParens :: Int -> String -> Int
countParens n s = case s of
  (x : xs) -> if x `elem` ")," then countParens (n + 1) xs else n
  _ -> n

varOrNode :: String -> Tree
varOrNode s = if isUpper (head s) then Var s else Node s []

parse :: Integer -> String -> [Tree] -> String -> ([Tree], String)
parse n acc t s = case s of
  (x : xs) -> case x of
    '(' -> parse n "" (t ++ [Node acc (fst w)]) (snd w) where w = parse (n + 1) "" [] xs
    ')' -> (t ++ [varOrNode acc], drop (countParens 0 xs) xs)
    ',' -> parse n "" (t ++ [varOrNode acc]) xs
    _ -> parse n (acc ++ [x]) t xs
  _ -> if acc /= "" then (t ++ [varOrNode acc], "") else (t, "")

maybeToList :: Maybe [a] -> [a]
maybeToList Nothing = []
maybeToList (Just xs) = xs

iter :: [Tree] -> [Tree] -> Maybe [(Tree, Tree)]
iter [] [] = Just []
iter (x : xs) (y : ys) = let k = iter xs ys in if w == Nothing || k == Nothing then Nothing else Just (maybeToList w ++ maybeToList k) where w = check (x, y)
iter _ _ = Nothing

check :: (Tree, Tree) -> Maybe [(Tree, Tree)]
check (Var x, Node y ys) = if checkHelper (Var x) ys then Nothing else Just [(Var x, Node y ys)]
check (Node x xs, Var y) = if checkHelper (Var y) xs then Nothing else Just [(Var y, Node x xs)]
check (Var x, Var y) = if x == y then Just [] else Just [(Var x, Var y)]
check (Node x [], Node y []) = checkNode x y
check (Node x xs, Node y []) = Nothing
check (Node x [], Node y ys) = Nothing
check (Node x xs, Node y ys) = let k = iter xs ys in if w == Nothing || k == Nothing then Nothing else Just (maybeToList k) where w = checkNode x y

checkHelper :: Tree -> [Tree] -> Bool
checkHelper (Var x) y = case y of
  (y : ys) -> case y of
    (Var y) -> (y == x) || checkHelper (Var x) ys
    (Node z zs) -> checkHelper (Var x) zs || checkHelper (Var x) ys
  _ -> False
checkHelper _ _ = False

checkNode :: String -> String -> Maybe [(Tree, Tree)]
checkNode x y = if x == y then Just [] else Nothing

unify :: String -> String -> Maybe [(Tree, Tree)]
unify s1 s2 = iter (fst (parse 0 "" [] s1)) (fst (parse 0 "" [] s2))

reduce :: [(Tree, Tree)] -> [(Tree, Tree)] -> [(Tree, Tree)]
reduce l ret = case l of
  (x : xs) -> if (x `elem` ret) || (fst x == snd x) then reduce xs ret else reduce xs (ret ++ [x])
  _ -> ret

replace :: [(Tree, Tree)] -> [(Tree, Tree)] -> [(Tree, Tree)]
replace l ret = case l of
  (x : xs) -> replace xs (replaceHelper x ret)
  _ -> ret

replaceHelper :: (Tree, Tree) -> [(Tree, Tree)] -> [(Tree, Tree)]
replaceHelper p = map w
  where
    w c
      | fst p == snd c = (fst c, snd p)
      | otherwise = c

applyOnNodes :: [(Tree, Tree)] -> [(Tree, Tree)] -> Maybe [(Tree, Tree)]
applyOnNodes l fl = case l of
  (x : xs) -> case x of
    (Var z, Node y ys) -> if w == Nothing then w else Just (maybeToList w ++ maybeToList (applyOnNodes xs fl)) where w = check (Var z, Node y (iterNodes ys fl))
    _ -> if w == Nothing then w else Just (maybeToList w ++ maybeToList (applyOnNodes xs fl)) where w = check x
  _ -> Just []

iterNodes :: [Tree] -> [(Tree, Tree)] -> [Tree]
iterNodes t l = case t of
  (x : xs) -> case x of
    (Var y) -> [applyHelper x l] ++ iterNodes xs l
    (Node y ys) -> [Node y (iterNodes ys l)] ++ iterNodes xs l
  _ -> []

applyHelper :: Tree -> [(Tree, Tree)] -> Tree
applyHelper t l = case l of
  (x : xs) -> case x of
    (Var y, z) -> if t == Var y then z else applyHelper t xs
    _ -> applyHelper t xs
  _ -> t

repAndRed :: [(Tree, Tree)] -> Maybe [(Tree, Tree)]
repAndRed l = let k = applyOnNodes w w in if k == Nothing then k else if maybeToList k == l then Just l else repAndRed (maybeToList k) where w = reduce (replace l l) []

associateNodes :: [(Tree, Tree)] -> Maybe [(Tree, Tree)]
associateNodes l = case l of
  (x : y : xs) ->
    let k = associateNodes ([y] ++ xs)
     in if fst x /= fst y
          then k
          else case (snd x, snd y) of
            (Node a as, Node b bs) -> if w == Nothing then w else Just (maybeToList w ++ maybeToList (associateNodes (maybeToList w)) ++ maybeToList (associateNodes ([y] ++ xs))) where w = iter as bs
            _ -> k
  (_ : xs) -> associateNodes xs
  _ -> Just []

mm :: String -> String -> Maybe [(Tree, Tree)]
mm s1 s2 = let k = maybeToList (associateNodes (maybeToList w)) in let l = repAndRed (k ++ maybeToList w) in if w == Nothing || l == Nothing then Nothing else Just (maybeToList l) where w = unify s1 s2

main = do
  putStrLn "Hello, World!"

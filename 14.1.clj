(def w 101)
(def h 103)
(def qw (quot w 2))
(def qh (quot h 2))

(def robots(->>
    (slurp (first *command-line-args*))
    (re-seq #"p=(\d+),(\d+) v=(-*\d+),(-*\d+)")
    (map #(subvec % 1 5))
    (map #(vec (map Integer/parseInt %)))
    (map #(
        vector
            (mod (+ (% 0) (* 100 (% 2))) w)
            (mod (+ (% 1) (* 100 (% 3))) h)
    ))
))

(def qlu (count (filter (fn [[x y]] (and (< x qw) (< y qh) )) robots)))
(def qru (count (filter (fn [[x y]] (and (> x qw) (< y qh) )) robots)))
(def qld (count (filter (fn [[x y]] (and (< x qw) (> y qh) )) robots)))
(def qrd (count (filter (fn [[x y]] (and (> x qw) (> y qh) )) robots)))

(println (= (* qlu qru qld qrd) 231782040))

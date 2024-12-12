(def data (slurp "input.txt"))

(def res
    (->>
        (re-seq #"mul\((\d+),(\d+)\)" data)
        (map #(* (Integer/parseInt (nth % 1)) (Integer/parseInt (nth % 2))))
        (reduce +)
    )
)

(println res)

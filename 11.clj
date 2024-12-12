; read 2 integers from input.txt
(defn parse-line [line]
  (mapv #(Integer/parseInt %) (clojure.string/split (clojure.string/trim line) #"\s+")))

(defn read-integers []
  (let [content (slurp "input.txt")
        lines (clojure.string/split-lines content)
        pairs (map parse-line lines)]
    (apply map vector pairs)))

(let [[array1 array2] (read-integers)]
  (println "Array 1:" array1)
  (println "Array 2:" array2)
  (def a1Sorted (sort array1))
  (def a2Sorted (sort array2))
  (println "Array 1 sorted:" a1Sorted)
  (println "Array 2 sorted:" a2Sorted)
  (def diff (map - a1Sorted a2Sorted))
  (def diffAbs (map #(Math/abs %) diff))
  (println "Difference:" diffAbs)
  (def sum (reduce + diffAbs))
  (println sum)
)

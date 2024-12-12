; read 2 integers from input.txt
(defn parse-line [line]
  (mapv #(Integer/parseInt %) (clojure.string/split (clojure.string/trim line) #"\s+")))

(defn read-integers []
  (let [content (slurp "input.txt")
        lines (clojure.string/split-lines content)
        pairs (map parse-line lines)]
    (apply map vector pairs)))

(defn countOfMatches [n array]
  (count (filter (partial = n) array)))


(let [[array1 array2] (read-integers)]
  (println "Array 1:" array1)
  (println "Array 2:" array2)
  (println (reduce + (map #(* % (countOfMatches % array2)) array1)))
)

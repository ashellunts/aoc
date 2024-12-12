; read n integers from input.txt
(defn parse-line [line]
  (mapv #(Integer/parseInt %)
        (clojure.string/split (clojure.string/trim line) #"\s+")))

(defn read-integers []
  (let [content (slurp "input.txt")
        lines (clojure.string/split-lines content)]
    (map parse-line lines)))

(def data (read-integers))

(defn safeIncrease [a b]
	(let
		[diff (- b a)]
    		(and (>= diff 1) (<= diff 3))))

(defn safeReport [input]
	(let
		[
			inputCopyWithoutLastElement (subvec input 1)
			safeI (every? identity (map safeIncrease input inputCopyWithoutLastElement))
			safeD (every? identity (map safeIncrease inputCopyWithoutLastElement input))
		]
		(or safeI safeD)
	)
)

(defn remove_nth [v n]
	(vec (concat (subvec v 0 n) (subvec v (inc n))))
)


(defn almostSafeReport [input]
	(some safeReport
			(map
				#(remove_nth input %)
				(range (count input)))))


(println (count (filter almostSafeReport data)))

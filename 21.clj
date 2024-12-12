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
   [;; tmp (println "Input:" input)
    inputCopyWithoutLastElement (subvec input 1)
            ;; tmp (println "Input copy without last element:" inputCopyWithoutLastElement)
    safeI (every? identity (map safeIncrease input inputCopyWithoutLastElement))
    safeD (every? identity (map safeIncrease inputCopyWithoutLastElement input))]
    (or safeI safeD)))

(println ((frequencies (map safeReport data)) true))

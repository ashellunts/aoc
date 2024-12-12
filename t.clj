(def data (slurp "input.txt"))

(def res
  (->> (re-seq #"mul\((\d+),(\d+)\)|do\(\)|don't\(\)" data)
       (reduce
            (fn [{:keys [enabled sum] :as state} [match & groups]]
                (cond
                    (= match "do()")
                        (assoc state :enabled true)
                    (= match "don't()")
                        (assoc state :enabled false)
                    (and enabled (= (count groups) 2))
                        (update state :sum #(+ % (* (Integer/parseInt (groups 1)) (Integer/parseInt (groups 0)))))
                    :else state)
            )
            {:enabled true :sum 0}
        )
    )
)

(println res)

;; (def data (slurp "input.txt"))

;; (def res
;;   (let [lines (re-seq #"mul\((\d+),(\d+)\)|do\(\)|don't\(\)" data)]
;;     (loop [remaining lines
;;            enabled true
;;            acc 0]
;;       (if (empty? remaining)
;;         acc
;;         (let [
;;                 [_ a b :as match] (first remaining)
;;                 next-enabled (cond
;;                                 (= "do()" (first match)) true
;;                                 (= "don't()" (first match)) false
;;                                 :else enabled)
;;                 result (if (and enabled a b)
;;                        (* (Integer/parseInt a) (Integer/parseInt b))
;;                        0)
;;             ]
;;             (recur (rest remaining) next-enabled (+ acc result)))

;;         ))))
;; (println res)

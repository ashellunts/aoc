(def data (slurp "input.txt"))

(def res
    (->>
        (re-seq #"mul\((\d+),(\d+)\)|do\(\)|don't\(\)" data)
        (reduce
            (fn [state element]
                (let [
                    value (nth element 0)
                    a (nth element 1)
                    b (nth element 2)
                ]
                    (if (= value "do()")
                        {:enabled true, :sum (:sum state)}
                        (if (= value "don't()")
                            {:enabled false, :sum (:sum state)}
                            (if (:enabled state)
                                {
                                    :enabled true,
                                    :sum (+
                                        (:sum state)
                                        (* (Integer/parseInt a) (Integer/parseInt b))
                                    )
                                }
                                state
                            )
                        )
                    )
                )
            )
            {:enabled true, :sum 0}
        )
    )
)

(println res)

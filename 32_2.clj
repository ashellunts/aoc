(def data (slurp "input.txt"))

(def enabled true)

(def res
    (->>
        (re-seq #"mul\((\d+),(\d+)\)|do\(\)|don't\(\)" data)
        (map #(
                let [
                    value (nth % 0)
                    a (nth % 1)
                    b (nth % 2)
                ]
                (if (= "do()" value)
                    (let []
                        (def enabled true)
                        nil
                    )
                    (if (= "don't()" value)
                        (let []
                            (def enabled false)
                            nil
                        )
                        (if enabled
                            (* (Integer/parseInt a) (Integer/parseInt b))
                            nil
                        )
                    )
                )
        ))
        (filter identity)
        (reduce +)
    )
)


(println res)

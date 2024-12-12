(def data (slurp "input.txt"))

(def lines
    (->>
        (clojure.string/split-lines data)
        vec
    )
)

(
    def indexes
    (
        for [
            x (range (count lines))
            y (range (count (lines 0)))
        ]
        [x y]
    )
)

(defn isThereXMASOnPositionOnDirection [a b direction]
    (if (and
            (= (get-in lines [a b]) \X)
            (= (get-in lines [(+ a (get-in direction [0 0])) (+ b (get-in direction [0 1]))]) \M)
            (= (get-in lines [(+ a (get-in direction [1 0])) (+ b (get-in direction [1 1]))]) \A)
            (= (get-in lines [(+ a (get-in direction [2 0])) (+ b (get-in direction [2 1]))]) \S)
        )
        1
        0
    )
)

(def right [[0 1] [0 2] [0 3]] )
(def left [[0 -1] [0 -2] [0 -3]] )
(def up [[-1 0] [-2 0] [-3 0]] )
(def down [[1 0] [2 0] [3 0]] )

(def downRight [[1 1] [2 2] [3 3]] )
(def downLeft [[1 -1] [2 -2] [3 -3]] )
(def upRight [[-1 1] [-2 2] [-3 3]] )
(def upLeft [[-1 -1] [-2 -2] [-3 -3]] )

(defn isThereXMASOnPosition [[a b]]
    (+
        (isThereXMASOnPositionOnDirection a b left)
        (isThereXMASOnPositionOnDirection a b right)
        (isThereXMASOnPositionOnDirection a b up)
        (isThereXMASOnPositionOnDirection a b down)
        (isThereXMASOnPositionOnDirection a b downRight)
        (isThereXMASOnPositionOnDirection a b downLeft)
        (isThereXMASOnPositionOnDirection a b upRight)
        (isThereXMASOnPositionOnDirection a b upLeft)
    )
)

(println
    (->>
        (map isThereXMASOnPosition indexes)
        (reduce +)
    )
)

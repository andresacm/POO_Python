#lang racket

(define (F n)

    (if (= n 1)
    
        1
        (+ (/ 1.0 n) (F (- n 1)))

    )

)

(F 5)
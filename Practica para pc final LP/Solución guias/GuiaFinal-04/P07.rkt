#lang racket

(define l '(1 2 3 4 5))


(define (F l a b)

    (filter (lambda (x) (and (> x a) (< x b))) l)

)

(F l 3 5)


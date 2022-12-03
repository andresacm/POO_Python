#lang racket

(define (I x y z)

    (* (+ (* 12 x) (* 15 y)) (+ x y z))

)

(I 1 1 1)
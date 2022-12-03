#lang racket

;5 a.
(define l '(1 2 3 4 5))

(define (F x)

    (+ (+ x 2) (* 2 x))

)

(map F l)

;5 b.
(define funcion (lambda (x) (* 2 x)))
(funcion 2)
#lang racket

(define l '(1 2 3 14 5))

(define (digitos n)

    (+ (truncate (log n 10)) 1)

)

(map digitos l)
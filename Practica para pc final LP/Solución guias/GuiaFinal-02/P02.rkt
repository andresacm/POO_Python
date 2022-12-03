#lang racket

(define (G x y) 
    (+ (* 2 x) (* 3 y) 5)
)

(display (G 2 6))
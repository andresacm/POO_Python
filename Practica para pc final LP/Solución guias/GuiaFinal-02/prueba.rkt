#lang racket

(define (F x) (+ (* 2 x) 3))

;Funciones anonimas
(define my-function (lambda (x) (+ (* 2 x) 3)))
(my-function 4)


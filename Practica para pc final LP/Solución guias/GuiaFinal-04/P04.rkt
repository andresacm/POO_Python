#lang racket

(define list '(1 2 3 4 5))

(define (sum-list list)

    (if (eq? list '())
    
        0
        (+ (car list) (sum-list (cdr list)))
    
    )

)

(sum-list list)
#lang racket

(define l '(1 2 3 4 5))

(define (contar l)

    (if (empty? l)
        0
        (+ 1 (contar (cdr l)))
    
    )

)

(contar l)


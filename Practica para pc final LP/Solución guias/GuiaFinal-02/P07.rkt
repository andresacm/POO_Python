#lang racket

(define L '(1 2 9 4 5))

(define (Maximo L)

    (if (empty? L)
    
        0
        (max (car L) (Maximo (cdr L)))

    )

)

(define (Minimo L)

    (if (eq? (length L) 1)
    
        (car L)
        (min (car L) (Minimo (cdr L)))

    )

)

(Maximo L)
(Minimo L)



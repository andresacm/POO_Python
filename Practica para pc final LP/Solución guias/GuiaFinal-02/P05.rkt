#lang racket

(define lista '(1 2 3 4 5))

(define (sumElementos lista)

    (if (empty? lista)
        0
        (+ (car lista) (sumElementos (cdr lista)))
    )
)

(define (prom lista)

    (/ (sumElementos lista) (length lista))

)

(prom lista)


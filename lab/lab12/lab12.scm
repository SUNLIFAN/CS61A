; Lab 14: Final Review

(define (compose-all funcs)
   (define (composed x)
      (if (null? funcs)
          x
          ((compose-all (cdr funcs)) ((car funcs) x)) 
      )
   )
   composed
)
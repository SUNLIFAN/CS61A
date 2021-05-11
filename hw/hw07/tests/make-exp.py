test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          16
          # locked
          scm> (make-exp 'x 1)
          x
          # locked
          scm> (make-exp 'x 0)
          1
          # locked
          scm> x^2
          (^ x 2)
          # locked
          scm> (first-operand x^2)
          x
          # locked
          scm> (second-operand x^2)
          2
          # locked
          scm> (exp? x^2) ; #t or #f
          #t
          # locked
          scm> (exp? 1)
          #f
          # locked
          scm> (exp? 'x)
          #f
          # locked
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}

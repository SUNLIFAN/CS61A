test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define a '(1))
          a
          # locked
          scm> a
          (1)
          # locked
          scm> (define b (cons 2 a))
          b
          # locked
          scm> b
          (2 1)
          # locked
          scm> (define c (list 3 b))
          c
          # locked
          scm> c
          (3 (2 1))
          # locked
          scm> (car c)
          3
          # locked
          scm> (cdr c)
          ((2 1))
          # locked
          scm> (car (car (cdr c)))
          2
          # locked
          scm> (cdr (car (cdr c)))
          (1)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> lst  ; type out exactly how Scheme would print the list
          ((1) 2 (3 4) 5)
          # locked
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}

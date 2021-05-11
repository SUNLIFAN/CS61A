test = {
  'name': 'make-adder',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add-two 2)
          4
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (add-two 3)
          5
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (add-three 3)
          6
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (add-three 9)
          12
          # locked
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define add-two (make-adder 2))
      scm> (define add-three (make-adder 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}

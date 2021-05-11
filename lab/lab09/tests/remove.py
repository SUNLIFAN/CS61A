test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (remove 3 nil)
          ()
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (remove 2 '(1 3 2))
          (1 3)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (remove 1 '(1 3 2))
          (3 2)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (remove 42 '(1 3 2))
          (1 3 2)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (remove 3 '(1 3 3 7))
          (1 7)
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

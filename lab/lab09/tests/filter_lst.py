test = {
  'name': 'filter-lst',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(1 2 3 4))
          (2 4)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(1 3 5))
          (1 3 5)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter-lst odd? '(2 4 6 1))
          (1)
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter-lst even? '(3))
          ()
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (filter-lst odd? nil)
          ()
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

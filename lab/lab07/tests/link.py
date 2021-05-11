test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(1000)
          >>> link.first
          1000
          # locked
          >>> link.rest is Link.empty
          True
          # locked
          >>> link = Link(1000, 2000)
          Error
          # locked
          >>> link = Link(1000, Link())
          Error
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          1
          # locked
          >>> link.rest.first
          2
          # locked
          >>> link.rest.rest.rest is Link.empty
          True
          # locked
          >>> link.first = 9001
          >>> link.first
          9001
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          3
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          1
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          1
          # locked
          >>> link2.rest.first
          2
          # locked
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab07 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link                  # Look at the __repr__ method of Link
          Link(5, Link(6, Link(7)))
          # locked
          >>> print(link)          # Look at the __str__ method of Link
          <5 6 7>
          # locked
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}

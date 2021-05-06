test = {
  'name': 'List Indexing',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [1, 3, [5, 7], 9] # Write the expression that indexes into x to output the 7
          x[2][1]
          # locked
          >>> x = [[3, [5, 7], 9]] # Write the expression that indexes into x to output the 7
          x[0][1][1]
          # locked
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4]
          Error
          # locked
          >>> lst[3][0]
          84
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

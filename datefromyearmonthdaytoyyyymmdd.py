def test(date):
  date=date.split(' ')
  day=''.join(c for c in date[0] if c.isdigit())
  monthmap={
            'jan': '01',
            'feb': '02',
            'mar': '03',
            'apr': '04',
            'may': '05',
            'jun': '06',
            'jul': '07',
            'aug': '08',
            'sep': '09', 
            'oct': '10',
            'nov': '11',
            'dec': '12'
    }
  Month=monthmap[date[1].lower()]

  return str(date[2])+'-'+Month+'-'+day.zfill(2)
test('7th Apr 1944')

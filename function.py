#def get_summ(one, two, delimiter='&'):
#    summ = '{} {} {}'.format(one, delimiter, two)
#    b = summ.upper()
#    return b 

#print(get_summ('Learn', 'Python'))


def format_price(price):
    price = abs(float(price))
    price_ = 'Цена: {} руб.'.format(price)
    return price_

d = format_price('56.24')
print(d)
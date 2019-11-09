# 전체 합 구하기
print(sum(0.1 for i in range(10)) == 1.0)
# False

from decimal import Decimal
print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
# True


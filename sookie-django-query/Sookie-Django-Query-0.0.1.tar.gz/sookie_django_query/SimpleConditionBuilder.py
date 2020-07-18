from sookie_django_query.CommonExpressBuilder import CommonExpressBuilder
from sookie_django_query.SimpleCondition import SimpleCondition


class SimpleConditionBuilder(CommonExpressBuilder):
    """
    数据结构：['>', 'aaa', 111]
    """
    def build(self, expression: SimpleCondition, params={}):
        operator = expression.getOperator()
        column = expression.getColumn()
        value = expression.getValue()
        self.addParams(value)

        return column + " " + operator + " " + "%s"

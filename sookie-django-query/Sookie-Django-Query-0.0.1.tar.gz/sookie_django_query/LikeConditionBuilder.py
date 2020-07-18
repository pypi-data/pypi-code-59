from sookie_django_query.CommonExpressBuilder import CommonExpressBuilder
from sookie_django_query.Handler import Handler
from sookie_django_query.LikeCondition import LikeCondition


class LikeConditionBuilder(CommonExpressBuilder):

    def build(self, expression: LikeCondition, params={}):
        operator = Handler.strToUpper(expression.getOperator())
        column = expression.getColumn()
        values = expression.getValue()
        escape = expression.escapingReplacements()

        if not values:
            return "0=1"

        self.addParams(values)

        return column + " " + operator + " " + "%s"

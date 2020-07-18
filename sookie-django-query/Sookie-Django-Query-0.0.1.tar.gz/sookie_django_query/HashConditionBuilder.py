from sookie_django_query.CommonExpressBuilder import CommonExpressBuilder
from sookie_django_query.HashCondition import HashCondition


class HashConditionBuilder(CommonExpressBuilder):
    def build(self, expression: HashCondition, params={}):
        """
        :param expression:
        :param params:
        :return:
        """
        hashExpression = expression.getHash()

        parts = self.buildExpressions(hashExpression)

        return parts[0] if len(parts) == 1 else "(" + ") AND (".join(parts) + ")"

    def buildExpressions(self, values: dict):
        parts = []

        for key, value in values.items():
            expression = key + " = %s"
            self.addParams(value)
            parts.append(expression)

        return parts


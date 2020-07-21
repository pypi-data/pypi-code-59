PLAN_TASK_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "departure_time": {
            "format": "date-time",
            "type": "string",
            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
        },
        "detail": {
            "default": true,
            "type": "boolean",
            "x-description-ru": "\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0443\u0442\u0438."
        },
        "geo_provider": {
            "maxLength": 256,
            "minLength": 1,
            "type": "string",
            "x-description-ru": "\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a \u0433\u0435\u043e\u0434\u0430\u043d\u043d\u044b\u0445."
        },
        "result_timezone": {
            "default": 0,
            "format": "int32",
            "maximum": 12,
            "minimum": -12,
            "type": "integer",
            "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0437\u043e\u043d\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0440\u0430\u0441\u0447\u0435\u0442\u0430."
        },
        "transport_type": {
            "default": "CAR",
            "enum": [
                "CAR",
                "TRUCK",
                "CAR_GT",
                "TUK_TUK",
                "BICYCLE",
                "PEDESTRIAN",
                "PUBLIC_TRANSPORT"
            ],
            "nullable": false,
            "type": "string",
            "x-description-ru": "\u0422\u0438\u043f\u044b \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430:\n  * `CAR` - \u043b\u0435\u0433\u043a\u043e\u0432\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\n  * `TRUCK` - \u0433\u0440\u0443\u0437\u043e\u0432\u043e\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\n  * `CAR_GT` - \u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044c\n  * `TUK_TUK` - \u043c\u043e\u0442\u043e\u0440\u0438\u043a\u0448\u0430\n  * `BICYCLE` - \u0432\u0435\u043b\u043e\u0441\u0438\u043f\u0435\u0434\n  * `PEDESTRIAN` - \u043f\u0435\u0448\u0435\u0445\u043e\u0434      \n  * `PUBLIC_TRANSPORT` - \u043e\u0431\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\n"
        },
        "waypoints": {
            "items": {
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                    "duration": {
                        "default": 0,
                        "format": "int32",
                        "maximum": 43800,
                        "minimum": 0,
                        "type": "integer",
                        "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430 \u0442\u043e\u0447\u043a\u0435 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                    },
                    "latitude": {
                        "format": "double",
                        "maximum": 90,
                        "minimum": -90,
                        "type": "number",
                        "x-description-ru": "\u0428\u0438\u0440\u043e\u0442\u0430 \u0432 \u0433\u0440\u0430\u0434\u0443\u0441\u0430\u0445."
                    },
                    "longitude": {
                        "format": "double",
                        "maximum": 180,
                        "minimum": -180,
                        "type": "number",
                        "x-description-ru": "\u0414\u043e\u043b\u0433\u043e\u0442\u0430 \u0432 \u0433\u0440\u0430\u0434\u0443\u0441\u0430\u0445."
                    }
                },
                "required": [
                    "latitude",
                    "longitude"
                ],
                "type": "object",
                "x-description-ru": "\u0413\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0442\u043e\u0447\u043a\u0430."
            },
            "maxItems": 9000,
            "minItems": 2,
            "type": "array",
            "uniqueItems": false,
            "x-description-ru": "\u041c\u0430\u0441\u0441\u0438\u0432 \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0442\u043e\u0447\u0435\u043a, \u043c\u0435\u0436\u0434\u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0430."
        }
    },
    "required": [
        "waypoints"
    ],
    "type": "object",
    "x-description-ru": "\u0417\u0430\u0434\u0430\u0447\u0430 \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u043f\u0443\u0442\u0438 \u0438\u043b\u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043c\u0430\u0442\u0440\u0438\u0446\u044b, \u043f\u0440\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0432\u044b\u0435\u0437\u0434\u0430 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043f\u0440\u043e\u0431\u043a\u0438."
}'''
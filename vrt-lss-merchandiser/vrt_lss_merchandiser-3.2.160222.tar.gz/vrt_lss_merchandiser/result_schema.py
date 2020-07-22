PLAN_RESULT_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "info": {
            "additionalProperties": false,
            "nullable": false,
            "properties": {
                "planning_time": {
                    "format": "int32",
                    "maximum": 2880,
                    "minimum": 0,
                    "type": "integer",
                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                },
                "result_version": {
                    "format": "int32",
                    "maximum": 1000000,
                    "minimum": 0,
                    "type": "integer",
                    "x-description-ru": "\u0412\u0435\u0440\u0441\u0438\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f."
                },
                "status": {
                    "enum": [
                        "WAITING",
                        "IN_PROGRESS",
                        "FINISHED_IN_TIME",
                        "FINISHED_OUT_OF_TIME",
                        "CANCELED",
                        "FAILED"
                    ],
                    "type": "string",
                    "x-description-ru": "\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:\n  * `WAITING` - \u0440\u0430\u0441\u0447\u0435\u0442 \u043e\u0436\u0438\u0434\u0430\u0435\u0442 \u0437\u0430\u043f\u0443\u0441\u043a\u0430.\n  * `IN_PROGRESS` - \u0440\u0430\u0441\u0447\u0435\u0442 \u0432 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u0435.\n  * `FINISHED_IN_TIME` - \u0440\u0430\u0441\u0447\u0435\u0442 \u0437\u0430\u0432\u0435\u0440\u0448\u0438\u043b\u0441\u044f \u0440\u0430\u043d\u044c\u0448\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043d\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435.\n  * `FINISHED_OUT_OF_TIME` - \u0440\u0430\u0441\u0447\u0435\u0442 \u0437\u0430\u0432\u0435\u0440\u0448\u0438\u043b\u0441\u044f, \u0442\u0430\u043a \u043a\u0430\u043a \u0437\u0430\u043a\u043e\u043d\u0447\u0438\u043b\u043e\u0441\u044c \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435.\n  * `CANCELED` - \u0440\u0430\u0441\u0447\u0435\u0442 \u0431\u044b\u043b \u043e\u0442\u043c\u0435\u043d\u0435\u043d.\n  * `FAILED` - \u0440\u0430\u0441\u0447\u0435\u0442 \u0437\u0430\u0432\u0435\u0440\u0448\u0438\u043b\u0441\u044f \u0441 \u043e\u0448\u0438\u0431\u043a\u043e\u0439.\n"
                },
                "waiting_time": {
                    "format": "int32",
                    "maximum": 2880,
                    "minimum": 0,
                    "type": "integer",
                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043a \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044e, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                }
            },
            "required": [
                "status"
            ],
            "type": "object",
            "x-description-ru": "\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438."
        },
        "progress": {
            "format": "int32",
            "maximum": 100,
            "minimum": 0,
            "type": "integer",
            "x-description-ru": "\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445. \u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u043e\u0442\u0440\u0430\u0436\u0430\u0435\u0442 \u0442\u0435\u043a\u0443\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u044b\u0445 \u0448\u0430\u0433\u043e\u0432.\n"
        },
        "statistics": {
            "additionalProperties": false,
            "nullable": true,
            "properties": {
                "total_statistics": {
                    "additionalProperties": false,
                    "nullable": true,
                    "properties": {
                        "capacity_utilization": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "capacity_x": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                },
                                "capacity_y": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                },
                                "capacity_z": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                },
                                "mass": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                },
                                "volume": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                }
                            },
                            "type": "object",
                            "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                        },
                        "cost": {
                            "format": "double",
                            "minimum": 0,
                            "type": "number",
                            "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u044b\u0435 \u0437\u0430\u0442\u0440\u0430\u0442\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0441\u0447\u0438\u0442\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u0431\u0430\u0437\u0435 \u0442\u0430\u0440\u0438\u0444\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 \u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430. \u0421\u0443\u043c\u043c\u0430\u0440\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0440\u0438 \u044d\u0442\u043e\u043c \u0440\u0430\u0432\u043d\u0430 \u0440\u0430\u0437\u043d\u0438\u0446\u0435 \u043c\u0435\u0436\u0434\u0443 \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u044b\u043c \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435\u043c (reward) \u0438 \u0440\u0430\u0441\u0445\u043e\u0434\u0430\u043c\u0438 (cost).\n"
                        },
                        "measurements": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "arriving_time": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434/\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434/\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                },
                                "departure_time": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u0434\u044c\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0439. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043e\u0442\u0434\u044c\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                },
                                "distance": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u043f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0439\u0441\u0430/\u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0439\u0441\u043e\u0432, \u0432 \u043c\u0435\u0442\u0440\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                },
                                "driving_time": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0432\u043e\u0436\u0434\u0435\u043d\u0438\u044f, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                },
                                "time_window": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "from": {
                                            "format": "date-time",
                                            "type": "string",
                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                        },
                                        "to": {
                                            "format": "date-time",
                                            "type": "string",
                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                        }
                                    },
                                    "required": [
                                        "from",
                                        "to"
                                    ],
                                    "type": "object",
                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                },
                                "total_time": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443/\u0440\u0435\u0439\u0441/\u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0439\u0441\u043e\u0432, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.        \u0421\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0438\u0437 driving_time + waiting_time + working_time + arriving_time + departure_time. \n"
                                },
                                "waiting_time": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043f\u043e \u0432\u0441\u0435\u043c \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.\n"
                                },
                                "working_time": {
                                    "format": "int32",
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u0432\u0441\u0435\u0445 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0432\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0432 \u0440\u0435\u0439\u0441. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043d\u0435\u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                }
                            },
                            "required": [
                                "driving_time",
                                "waiting_time",
                                "working_time",
                                "arriving_time",
                                "departure_time",
                                "total_time",
                                "distance"
                            ],
                            "type": "object",
                            "x-description-ru": "\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0432\u0440\u0435\u043c\u0435\u043d \u0438 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0439 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0445 \u0440\u0435\u0439\u0441\u043e\u0432 \u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u0446\u0435\u043b\u043e\u043c.\n  * `time_window` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0435\u0439\u0441\u0430, \u0434\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043e\u0442 \u043d\u0430\u0447\u0430\u043b\u0430 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u043a \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043e\u0442\u044a\u0435\u0437\u0434\u0430 \u0441 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438.\n"
                        },
                        "orders_count": {
                            "format": "int32",
                            "maximum": 9000,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                        },
                        "performers_count": {
                            "format": "int32",
                            "maximum": 9000,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439, \u0437\u0430\u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                        },
                        "reward": {
                            "format": "double",
                            "minimum": 0,
                            "type": "number",
                            "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                        }
                    },
                    "required": [
                        "cost",
                        "reward",
                        "measurements",
                        "orders_count",
                        "performers_count"
                    ],
                    "type": "object",
                    "x-description-ru": "\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u043b\u0438\u0431\u043e \u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0439\u0441\u043e\u0432.\n  * `capacity_utilization` - \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u043f\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0443 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u043a \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u043f\u043e \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0443.\n"
                },
                "trips_statistics": {
                    "items": {
                        "additionalProperties": false,
                        "nullable": true,
                        "properties": {
                            "max_load": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "capacity": {
                                        "additionalProperties": false,
                                        "nullable": true,
                                        "properties": {
                                            "capacity_x": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                            },
                                            "capacity_y": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                            },
                                            "capacity_z": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                            },
                                            "mass": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                            },
                                            "volume": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                            }
                                        },
                                        "type": "object",
                                        "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                                    },
                                    "count": {
                                        "format": "int32",
                                        "minimum": 0,
                                        "type": "integer",
                                        "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                    }
                                },
                                "required": [
                                    "count",
                                    "capacity"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                            },
                            "statistics": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "capacity_utilization": {
                                        "additionalProperties": false,
                                        "nullable": true,
                                        "properties": {
                                            "capacity_x": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                            },
                                            "capacity_y": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                            },
                                            "capacity_z": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                            },
                                            "mass": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                            },
                                            "volume": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                            }
                                        },
                                        "type": "object",
                                        "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                                    },
                                    "cost": {
                                        "format": "double",
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u044b\u0435 \u0437\u0430\u0442\u0440\u0430\u0442\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0441\u0447\u0438\u0442\u0430\u044e\u0442\u0441\u044f \u043d\u0430 \u0431\u0430\u0437\u0435 \u0442\u0430\u0440\u0438\u0444\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 \u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430. \u0421\u0443\u043c\u043c\u0430\u0440\u043d\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0440\u0438 \u044d\u0442\u043e\u043c \u0440\u0430\u0432\u043d\u0430 \u0440\u0430\u0437\u043d\u0438\u0446\u0435 \u043c\u0435\u0436\u0434\u0443 \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u044b\u043c \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435\u043c (reward) \u0438 \u0440\u0430\u0441\u0445\u043e\u0434\u0430\u043c\u0438 (cost).\n"
                                    },
                                    "measurements": {
                                        "additionalProperties": false,
                                        "nullable": true,
                                        "properties": {
                                            "arriving_time": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434/\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434/\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                            },
                                            "departure_time": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u0434\u044c\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0439. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043e\u0442\u0434\u044c\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                            },
                                            "distance": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u043f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0439\u0441\u0430/\u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0439\u0441\u043e\u0432, \u0432 \u043c\u0435\u0442\u0440\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                            },
                                            "driving_time": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0432\u043e\u0436\u0434\u0435\u043d\u0438\u044f, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                            },
                                            "time_window": {
                                                "additionalProperties": false,
                                                "properties": {
                                                    "from": {
                                                        "format": "date-time",
                                                        "type": "string",
                                                        "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                    },
                                                    "to": {
                                                        "format": "date-time",
                                                        "type": "string",
                                                        "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                    }
                                                },
                                                "required": [
                                                    "from",
                                                    "to"
                                                ],
                                                "type": "object",
                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                            },
                                            "total_time": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443/\u0440\u0435\u0439\u0441/\u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0439\u0441\u043e\u0432, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.        \u0421\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0438\u0437 driving_time + waiting_time + working_time + arriving_time + departure_time. \n"
                                            },
                                            "waiting_time": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043f\u043e \u0432\u0441\u0435\u043c \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.\n"
                                            },
                                            "working_time": {
                                                "format": "int32",
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u0432\u0441\u0435\u0445 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0432\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0432 \u0440\u0435\u0439\u0441. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043d\u0435\u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                            }
                                        },
                                        "required": [
                                            "driving_time",
                                            "waiting_time",
                                            "working_time",
                                            "arriving_time",
                                            "departure_time",
                                            "total_time",
                                            "distance"
                                        ],
                                        "type": "object",
                                        "x-description-ru": "\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0432\u0440\u0435\u043c\u0435\u043d \u0438 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0439 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0445 \u0440\u0435\u0439\u0441\u043e\u0432 \u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u0446\u0435\u043b\u043e\u043c.\n  * `time_window` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0435\u0439\u0441\u0430, \u0434\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043e\u0442 \u043d\u0430\u0447\u0430\u043b\u0430 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u043a \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043e\u0442\u044a\u0435\u0437\u0434\u0430 \u0441 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438.\n"
                                    },
                                    "orders_count": {
                                        "format": "int32",
                                        "maximum": 9000,
                                        "minimum": 0,
                                        "type": "integer",
                                        "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                    },
                                    "performers_count": {
                                        "format": "int32",
                                        "maximum": 9000,
                                        "minimum": 0,
                                        "type": "integer",
                                        "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439, \u0437\u0430\u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0432 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0438 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                    },
                                    "reward": {
                                        "format": "double",
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                    }
                                },
                                "required": [
                                    "cost",
                                    "reward",
                                    "measurements",
                                    "orders_count",
                                    "performers_count"
                                ],
                                "type": "object",
                                "x-description-ru": "\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043e\u0434\u043d\u043e\u043c\u0443 \u043b\u0438\u0431\u043e \u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0439\u0441\u043e\u0432.\n  * `capacity_utilization` - \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u043f\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0443 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u043a \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u043f\u043e \u0434\u0430\u043d\u043d\u043e\u043c\u0443 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0443.\n"
                            },
                            "stop_statistics": {
                                "items": {
                                    "additionalProperties": false,
                                    "nullable": true,
                                    "properties": {
                                        "current_load": {
                                            "additionalProperties": false,
                                            "nullable": true,
                                            "properties": {
                                                "capacity": {
                                                    "additionalProperties": false,
                                                    "nullable": true,
                                                    "properties": {
                                                        "capacity_x": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                                        },
                                                        "capacity_y": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                                        },
                                                        "capacity_z": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                                        },
                                                        "mass": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                                        },
                                                        "volume": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                                        }
                                                    },
                                                    "type": "object",
                                                    "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                                                },
                                                "count": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                                }
                                            },
                                            "required": [
                                                "count",
                                                "capacity"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                        },
                                        "demand_ids": {
                                            "items": {
                                                "maxLength": 1024,
                                                "minLength": 1,
                                                "type": "string",
                                                "x-description-ru": "\u0418\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u044f\u0432\u043a\u0438, \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0441\u044f \u043f\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0439 \u0444\u043e\u0440\u043c\u0443\u043b\u0435: \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430 + '#' + \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u044f\u0432\u043a\u0438.\n"
                                            },
                                            "type": "array",
                                            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u0437\u0430\u044f\u0432\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u043d\u0430 \u044d\u0442\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435."
                                        },
                                        "download": {
                                            "additionalProperties": false,
                                            "nullable": true,
                                            "properties": {
                                                "capacity": {
                                                    "additionalProperties": false,
                                                    "nullable": true,
                                                    "properties": {
                                                        "capacity_x": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                                        },
                                                        "capacity_y": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                                        },
                                                        "capacity_z": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                                        },
                                                        "mass": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                                        },
                                                        "volume": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                                        }
                                                    },
                                                    "type": "object",
                                                    "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                                                },
                                                "count": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                                }
                                            },
                                            "required": [
                                                "count",
                                                "capacity"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                        },
                                        "location": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "arrival_duration": {
                                                    "default": 0,
                                                    "format": "int32",
                                                    "maximum": 1440,
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434 (\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443) \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                                },
                                                "departure_duration": {
                                                    "default": 0,
                                                    "format": "int32",
                                                    "maximum": 1440,
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u044a\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
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
                                            "x-description-ru": "\u041b\u043e\u043a\u0430\u0446\u0438\u044f, \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435."
                                        },
                                        "location_key": {
                                            "maxLength": 1024,
                                            "minLength": 1,
                                            "type": "string",
                                            "x-description-ru": "\u041a\u043b\u044e\u0447 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u0434\u043b\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0437\u043d\u044b\u0445 \u043b\u043e\u043a\u0430\u0446\u0438\u0439 \u0441 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u043c\u0438 \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u043c\u0438 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430\u043c\u0438."
                                        },
                                        "measurements": {
                                            "additionalProperties": false,
                                            "nullable": true,
                                            "properties": {
                                                "arriving_time": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434/\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434/\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                                },
                                                "departure_time": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u0434\u044c\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0439. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043e\u0442\u0434\u044c\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                                },
                                                "distance": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u043f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0439\u0441\u0430/\u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0439\u0441\u043e\u0432, \u0432 \u043c\u0435\u0442\u0440\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                                },
                                                "driving_time": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0432\u043e\u0436\u0434\u0435\u043d\u0438\u044f, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u0442\u0435\u043a\u0443\u0449\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                                },
                                                "time_window": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object",
                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                },
                                                "total_time": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443/\u0440\u0435\u0439\u0441/\u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0439\u0441\u043e\u0432, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.        \u0421\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0438\u0437 driving_time + waiting_time + working_time + arriving_time + departure_time. \n"
                                                },
                                                "waiting_time": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043f\u043e \u0432\u0441\u0435\u043c \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.\n"
                                                },
                                                "working_time": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u0421\u0443\u043c\u043c\u0430\u0440\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u0432\u0441\u0435\u0445 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0432\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0432 \u0440\u0435\u0439\u0441. \u0414\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u044f, \u0437\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u043d\u0435\u043f\u043e\u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                                                }
                                            },
                                            "required": [
                                                "driving_time",
                                                "waiting_time",
                                                "working_time",
                                                "arriving_time",
                                                "departure_time",
                                                "total_time",
                                                "distance"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0418\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0432\u0440\u0435\u043c\u0435\u043d \u0438 \u0434\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u0439 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0445 \u0440\u0435\u0439\u0441\u043e\u0432 \u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u0446\u0435\u043b\u043e\u043c.\n  * `time_window` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0440\u0435\u0439\u0441\u0430, \u0434\u043b\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043e\u0442 \u043d\u0430\u0447\u0430\u043b\u0430 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u043a \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u0434\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043e\u0442\u044a\u0435\u0437\u0434\u0430 \u0441 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438.\n"
                                        },
                                        "upload": {
                                            "additionalProperties": false,
                                            "nullable": true,
                                            "properties": {
                                                "capacity": {
                                                    "additionalProperties": false,
                                                    "nullable": true,
                                                    "properties": {
                                                        "capacity_x": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                                        },
                                                        "capacity_y": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                                        },
                                                        "capacity_z": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                                        },
                                                        "mass": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                                        },
                                                        "volume": {
                                                            "default": 0,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                                        }
                                                    },
                                                    "type": "object",
                                                    "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                                                },
                                                "count": {
                                                    "format": "int32",
                                                    "minimum": 0,
                                                    "type": "integer",
                                                    "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                                }
                                            },
                                            "required": [
                                                "count",
                                                "capacity"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                        }
                                    },
                                    "required": [
                                        "location",
                                        "measurements"
                                    ],
                                    "type": "object",
                                    "x-description-ru": "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435 \u0432 \u0440\u0435\u0439\u0441\u0435, \u0433\u0434\u0435:\n  * `location` - \u043b\u043e\u043a\u0430\u0446\u0438\u044f, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430.\n  * `upload` - \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0432 \u043c\u0430\u0448\u0438\u043d\u0443 \u043d\u0430 \u044d\u0442\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435.\n  * `download` - \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0437 \u043c\u0430\u0448\u0438\u043d\u044b \u043d\u0430 \u044d\u0442\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435.\n  * `current_load` - \u0442\u0435\u043a\u0443\u0449\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043c\u0430\u0448\u0438\u043d\u044b \u043f\u043e\u0441\u043b\u0435 \u044d\u0442\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435.\n"
                                },
                                "maxItems": 9000,
                                "minItems": 0,
                                "type": "array",
                                "x-description-ru": "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043a\u0430\u0436\u0434\u043e\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435 \u0432 \u0440\u0435\u0439\u0441\u0435."
                            },
                            "total_load": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "capacity": {
                                        "additionalProperties": false,
                                        "nullable": true,
                                        "properties": {
                                            "capacity_x": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (X) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u0433\u0440\u0443\u0437\u043e\u0432 \u0432 \u0448\u0442\u0443\u043a\u0430\u0445 (\u0443 \u0433\u0440\u0443\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0440\u0430\u0432\u0435\u043d \u0435\u0434\u0438\u043d\u0438\u0446\u0435, \u0443 \u043e\u0442\u0441\u0435\u043a\u0430 - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0432\u043c\u0435\u0449\u0430\u0435\u043c\u044b\u0445 \u0433\u0440\u0443\u0437\u043e\u0432).\n"
                                            },
                                            "capacity_y": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Y) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                            },
                                            "capacity_z": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 (Z) \u0434\u043b\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u0438 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0432 \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0445 \u0435\u0434\u0438\u043d\u0438\u0446\u0430\u0445 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f."
                                            },
                                            "mass": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u041c\u0430\u0441\u0441\u0430 \u0432 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445."
                                            },
                                            "volume": {
                                                "default": 0,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u041e\u0431\u044a\u0435\u043c \u0432 \u043a\u0443\u0431\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043c\u0435\u0442\u0440\u0430\u0445."
                                            }
                                        },
                                        "type": "object",
                                        "x-description-ru": "\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u0435\u043c\u043a\u043e\u0441\u0442\u0438 \u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438."
                                    },
                                    "count": {
                                        "format": "int32",
                                        "minimum": 0,
                                        "type": "integer",
                                        "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                    }
                                },
                                "required": [
                                    "count",
                                    "capacity"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                            },
                            "trip_key": {
                                "maxLength": 1024,
                                "minLength": 1,
                                "type": "string",
                                "x-description-ru": "\u041a\u043b\u044e\u0447 \u0440\u0435\u0439\u0441\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                            }
                        },
                        "required": [
                            "trip_key",
                            "statistics",
                            "stop_statistics"
                        ],
                        "type": "object",
                        "x-description-ru": "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u043c\u0443 \u0440\u0435\u0439\u0441\u0443, \u0433\u0434\u0435:\n  * `total_load` - \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043c\u0430\u0448\u0438\u043d\u044b \u0437\u0430 \u0432\u0441\u0435 \u0432\u0440\u0435\u043c\u044f \u0440\u0435\u0439\u0441\u0430.\n  * `max_load` - \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043c\u0430\u0448\u0438\u043d\u044b \u0437\u0430 \u0432\u0441\u0435 \u0432\u0440\u0435\u043c\u044f \u0440\u0435\u0439\u0441\u0430 (\u043f\u043e \u043a\u0430\u0436\u0434\u043e\u043c\u0443 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044e).\n"
                    },
                    "maxItems": 9000,
                    "minItems": 0,
                    "type": "array",
                    "x-description-ru": "\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u043a\u0430\u0436\u0434\u043e\u043c\u0443 \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u043c\u0443 \u0440\u0435\u0439\u0441\u0443 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e."
                }
            },
            "required": [
                "total_statistics",
                "trips_statistics"
            ],
            "type": "object",
            "x-description-ru": "\u041e\u0431\u0449\u0430\u044f \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u043c \u0440\u0435\u0439\u0441\u0430\u043c:\n  * `total_statistics` - \u0441\u0443\u043c\u043c\u0430\u0440\u043d\u0430\u044f \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0432\u0441\u0435\u043c \u0440\u0435\u0439\u0441\u0430\u043c.\n  * `trips_statistics` - \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0438 \u043f\u043e \u043a\u0430\u0436\u0434\u043e\u043c\u0443 \u0440\u0435\u0439\u0441\u0443 \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e.\n"
        },
        "timetable": {
            "additionalProperties": false,
            "properties": {
                "finish_location": {
                    "additionalProperties": false,
                    "properties": {
                        "arrival_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434 (\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443) \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                        },
                        "departure_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u044a\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
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
                    "x-description-ru": "\u041b\u043e\u043a\u0430\u0446\u0438\u044f, \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435."
                },
                "key": {
                    "maxLength": 1024,
                    "minLength": 1,
                    "type": "string",
                    "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440"
                },
                "shifts": {
                    "items": {
                        "additionalProperties": false,
                        "properties": {
                            "availability_time": {
                                "additionalProperties": false,
                                "properties": {
                                    "from": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                    },
                                    "to": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                    }
                                },
                                "required": [
                                    "from",
                                    "to"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                            },
                            "trip": {
                                "additionalProperties": false,
                                "properties": {
                                    "actions": {
                                        "items": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "location_time": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object",
                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                },
                                                "order": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "duration": {
                                                            "format": "double",
                                                            "maximum": 43800,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                                        },
                                                        "facts": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437."
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 0,
                                                            "type": "array",
                                                            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d, \u0432 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0440\u0430\u043d\u0435\u0435 \u0431\u044b\u043b\u0438 \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u044b \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f \u0442\u043e\u0447\u0435\u043a."
                                                        },
                                                        "key": {
                                                            "maxLength": 1024,
                                                            "minLength": 1,
                                                            "type": "string",
                                                            "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                                                        },
                                                        "location": {
                                                            "additionalProperties": false,
                                                            "properties": {
                                                                "arrival_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer",
                                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434 (\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443) \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                                                },
                                                                "departure_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer",
                                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u044a\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
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
                                                            "x-description-ru": "\u041b\u043e\u043a\u0430\u0446\u0438\u044f, \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435."
                                                        },
                                                        "reward": {
                                                            "default": 1000,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0411\u0430\u0437\u043e\u0432\u043e\u0435 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430. \u0418\u0437 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f \u0432\u044b\u0447\u0438\u0442\u0430\u044e\u0442\u0441\u044f \u0448\u0442\u0440\u0430\u0444\u044b \u0437\u0430 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0432\u043e\u0432\u0440\u0435\u043c\u044f.\n"
                                                        },
                                                        "visits": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437."
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 1,
                                                            "type": "array",
                                                            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d, \u0432 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435 \u0442\u043e\u0447\u043a\u0438."
                                                        }
                                                    },
                                                    "required": [
                                                        "key",
                                                        "location",
                                                        "visits",
                                                        "duration",
                                                        "reward"
                                                    ],
                                                    "type": "object",
                                                    "x-description-ru": "\u0417\u0430\u043a\u0430\u0437 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
                                                },
                                                "order_time": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "from": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                        },
                                                        "to": {
                                                            "format": "date-time",
                                                            "type": "string",
                                                            "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                        }
                                                    },
                                                    "required": [
                                                        "from",
                                                        "to"
                                                    ],
                                                    "type": "object",
                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                }
                                            },
                                            "required": [
                                                "order",
                                                "order_time",
                                                "location_time"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n  * `order_time` - \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u043a\u043e\u043d\u0446\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430\u0434 \u0437\u0430\u043a\u0430\u0437\u043e\u043c \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n  * `location_time` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u0435\u043c \u0438 \u043e\u0442\u044a\u0435\u0437\u0434\u043e\u043c \u0441 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 (\u043d\u0435 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0443\u0436\u0435, \u0447\u0435\u043c `order_time`).\n"
                                        },
                                        "maxItems": 1000,
                                        "minItems": 1,
                                        "type": "array",
                                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                                    },
                                    "key": {
                                        "maxLength": 1024,
                                        "minLength": 1,
                                        "type": "string",
                                        "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0435\u0439\u0441\u0430"
                                    },
                                    "trip_time": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "from": {
                                                "format": "date-time",
                                                "type": "string",
                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                            },
                                            "to": {
                                                "format": "date-time",
                                                "type": "string",
                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                            }
                                        },
                                        "required": [
                                            "from",
                                            "to"
                                        ],
                                        "type": "object",
                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                    },
                                    "waitlist": {
                                        "items": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "order": {
                                                    "additionalProperties": false,
                                                    "properties": {
                                                        "duration": {
                                                            "format": "double",
                                                            "maximum": 43800,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                                        },
                                                        "facts": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437."
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 0,
                                                            "type": "array",
                                                            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d, \u0432 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0440\u0430\u043d\u0435\u0435 \u0431\u044b\u043b\u0438 \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u044b \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f \u0442\u043e\u0447\u0435\u043a."
                                                        },
                                                        "key": {
                                                            "maxLength": 1024,
                                                            "minLength": 1,
                                                            "type": "string",
                                                            "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                                                        },
                                                        "location": {
                                                            "additionalProperties": false,
                                                            "properties": {
                                                                "arrival_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer",
                                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434 (\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443) \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                                                },
                                                                "departure_duration": {
                                                                    "default": 0,
                                                                    "format": "int32",
                                                                    "maximum": 1440,
                                                                    "minimum": 0,
                                                                    "type": "integer",
                                                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u044a\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
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
                                                            "x-description-ru": "\u041b\u043e\u043a\u0430\u0446\u0438\u044f, \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435."
                                                        },
                                                        "reward": {
                                                            "default": 1000,
                                                            "format": "double",
                                                            "maximum": 1000000,
                                                            "minimum": 0,
                                                            "type": "number",
                                                            "x-description-ru": "\u0411\u0430\u0437\u043e\u0432\u043e\u0435 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430. \u0418\u0437 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f \u0432\u044b\u0447\u0438\u0442\u0430\u044e\u0442\u0441\u044f \u0448\u0442\u0440\u0430\u0444\u044b \u0437\u0430 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0432\u043e\u0432\u0440\u0435\u043c\u044f.\n"
                                                        },
                                                        "visits": {
                                                            "items": {
                                                                "additionalProperties": false,
                                                                "properties": {
                                                                    "time_window": {
                                                                        "additionalProperties": false,
                                                                        "properties": {
                                                                            "from": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            },
                                                                            "to": {
                                                                                "format": "date-time",
                                                                                "type": "string",
                                                                                "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                                            }
                                                                        },
                                                                        "required": [
                                                                            "from",
                                                                            "to"
                                                                        ],
                                                                        "type": "object",
                                                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                                                    }
                                                                },
                                                                "required": [
                                                                    "time_window"
                                                                ],
                                                                "type": "object",
                                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437."
                                                            },
                                                            "maxItems": 100,
                                                            "minItems": 1,
                                                            "type": "array",
                                                            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d, \u0432 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435 \u0442\u043e\u0447\u043a\u0438."
                                                        }
                                                    },
                                                    "required": [
                                                        "key",
                                                        "location",
                                                        "visits",
                                                        "duration",
                                                        "reward"
                                                    ],
                                                    "type": "object",
                                                    "x-description-ru": "\u0417\u0430\u043a\u0430\u0437 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "maxItems": 1000,
                                        "minItems": 0,
                                        "type": "array",
                                        "x-description-ru": "\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0435 \u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f, \u043d\u043e \u043d\u0435 \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u043a\u0430\u0437\u044b."
                                    }
                                },
                                "required": [
                                    "key",
                                    "trip_time"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0420\u0435\u0439\u0441 - \u044d\u0442\u043e \u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0440\u0430\u0431\u043e\u0442 (`actions`) \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u043c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043c. \u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0435\u0439\u0441\u0430 \u0438 \u0435\u0433\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0432 `trip_time`.\n"
                            },
                            "working_time": {
                                "additionalProperties": false,
                                "properties": {
                                    "from": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                    },
                                    "to": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                    }
                                },
                                "required": [
                                    "from",
                                    "to"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                            }
                        },
                        "required": [
                            "availability_time",
                            "working_time"
                        ],
                        "type": "object",
                        "x-description-ru": "\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u0441\u043c\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f.\n  * `availability_time` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0441\u043c\u0435\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445 \u0438 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c\u0438.\n  * `working_time` - \u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0441\u043c\u0435\u043d\u044b.\n  * `trip` - \u0440\u0435\u0439\u0441, \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0439 \u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f.\n"
                    },
                    "maxItems": 100,
                    "minItems": 1,
                    "type": "array",
                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043c\u0435\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f."
                },
                "start_location": {
                    "additionalProperties": false,
                    "properties": {
                        "arrival_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434 (\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443) \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                        },
                        "departure_duration": {
                            "default": 0,
                            "format": "int32",
                            "maximum": 1440,
                            "minimum": 0,
                            "type": "integer",
                            "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u044a\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
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
                    "x-description-ru": "\u041b\u043e\u043a\u0430\u0446\u0438\u044f, \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435."
                },
                "tariff": {
                    "additionalProperties": false,
                    "properties": {
                        "basic": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "cost_per_meter": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 10000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043d\u0430 \u043e\u0434\u0438\u043d \u043c\u0435\u0442\u0440."
                                },
                                "cost_per_minute": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 10000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u043e\u0434\u043d\u0443 \u043c\u0438\u043d\u0443\u0442\u0443."
                                },
                                "cost_per_shift": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043d\u0430 \u0441\u043c\u0435\u043d\u0443."
                                },
                                "max_length": {
                                    "default": 100000000,
                                    "format": "int32",
                                    "maximum": 100000000,
                                    "minimum": 1,
                                    "type": "integer",
                                    "x-description-ru": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0442\u0430\u0440\u0438\u0444\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445, \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0443\u043b\u044f."
                                },
                                "max_time": {
                                    "default": 43800,
                                    "format": "int32",
                                    "maximum": 43800,
                                    "minimum": 1,
                                    "type": "integer",
                                    "x-description-ru": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0442\u0430\u0440\u0438\u0444\u0430 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445, \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0443\u043b\u044f."
                                }
                            },
                            "required": [
                                "cost_per_shift",
                                "cost_per_meter",
                                "max_length",
                                "cost_per_minute",
                                "max_time"
                            ],
                            "type": "object",
                            "x-description-ru": "\u0422\u0430\u0440\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0441 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u043c."
                        },
                        "extra": {
                            "items": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "cost_per_meter": {
                                        "default": 0,
                                        "format": "double",
                                        "maximum": 10000,
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043d\u0430 \u043e\u0434\u0438\u043d \u043c\u0435\u0442\u0440."
                                    },
                                    "cost_per_minute": {
                                        "default": 0,
                                        "format": "double",
                                        "maximum": 10000,
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430 \u043e\u0434\u043d\u0443 \u043c\u0438\u043d\u0443\u0442\u0443."
                                    },
                                    "cost_per_shift": {
                                        "default": 0,
                                        "format": "double",
                                        "maximum": 1000000,
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0432\u044b\u0445\u043e\u0434\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043d\u0430 \u0441\u043c\u0435\u043d\u0443."
                                    },
                                    "max_length": {
                                        "default": 100000000,
                                        "format": "int32",
                                        "maximum": 100000000,
                                        "minimum": 1,
                                        "type": "integer",
                                        "x-description-ru": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0442\u0430\u0440\u0438\u0444\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445, \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0443\u043b\u044f."
                                    },
                                    "max_time": {
                                        "default": 43800,
                                        "format": "int32",
                                        "maximum": 43800,
                                        "minimum": 1,
                                        "type": "integer",
                                        "x-description-ru": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0442\u0430\u0440\u0438\u0444\u0430 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445, \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0443\u043b\u044f."
                                    }
                                },
                                "required": [
                                    "cost_per_shift",
                                    "cost_per_meter",
                                    "max_length",
                                    "cost_per_minute",
                                    "max_time"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0422\u0430\u0440\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0441 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u043c."
                            },
                            "maxItems": 10,
                            "minItems": 0,
                            "type": "array",
                            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0430\u0440\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u0430\u044f \u0434\u043b\u044f \u0441\u0432\u0435\u0440\u0445\u0443\u0440\u043e\u0447\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u044b.  \u041c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u0432 \u0432\u0438\u0434\u0435 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u0445 \u044d\u0442\u0430\u043f\u043e\u0432: \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u044d\u0442\u0430\u043f\u0430 \u043f\u0435\u0440\u0435\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043c\u043e\u0436\u0435\u0442 \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c\u0441\u044f \u0441\u0432\u043e\u0439 \u0442\u0430\u0440\u0438\u0444 \u043e\u043f\u043b\u0430\u0442\u044b.  \u041a\u0430\u0436\u0434\u044b\u0439 \u044d\u0442\u0430\u043f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u0440\u043e\u0442\u044f\u0436\u0451\u043d\u043d\u043e\u0441\u0442\u044c\u044e \u0438 \u043f\u0440\u043e\u0431\u0435\u0433\u043e\u043c \u043e\u0442 \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0433\u043e (\u043f\u0435\u0440\u0432\u044b\u0439 \u043e\u0442 \u0431\u0430\u0437\u043e\u0432\u043e\u0433\u043e \u0442\u0430\u0440\u0438\u0444\u0430).\n"
                        }
                    },
                    "required": [
                        "basic"
                    ],
                    "type": "object",
                    "x-description-ru": "\u0422\u0430\u0440\u0438\u0444 \u043e\u043f\u043b\u0430\u0442\u044b \u0440\u0430\u0431\u043e\u0442\u044b \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0441 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u043c."
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
                }
            },
            "required": [
                "key",
                "transport_type",
                "shifts",
                "tariff"
            ],
            "type": "object",
            "x-description-ru": "\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c. \u0415\u0441\u043b\u0438 \u0443 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f/\u043a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u043b\u043e\u043a\u0430\u0446\u0438\u044f, \u0440\u0435\u0439\u0441 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0438 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u043f\u0435\u0440\u0432\u043e\u043c/\u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u043c \u0437\u0430\u043a\u0430\u0437\u0435."
        },
        "tracedata": {
            "additionalProperties": false,
            "properties": {
                "code": {
                    "maxLength": 256,
                    "minLength": 3,
                    "type": "string",
                    "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438."
                }
            },
            "required": [
                "code"
            ],
            "type": "object",
            "x-description-ru": "\u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0435 \u0434\u043b\u044f \u0442\u0440\u0430\u0441\u0441\u0438\u0440\u043e\u0432\u043a\u0438 \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432."
        },
        "unplanned_orders": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "order": {
                        "additionalProperties": false,
                        "properties": {
                            "duration": {
                                "format": "double",
                                "maximum": 43800,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043e\u0434\u043d\u043e\u0433\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                            },
                            "facts": {
                                "items": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "time_window": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "from": {
                                                    "format": "date-time",
                                                    "type": "string",
                                                    "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                },
                                                "to": {
                                                    "format": "date-time",
                                                    "type": "string",
                                                    "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                }
                                            },
                                            "required": [
                                                "from",
                                                "to"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                        }
                                    },
                                    "required": [
                                        "time_window"
                                    ],
                                    "type": "object",
                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437."
                                },
                                "maxItems": 100,
                                "minItems": 0,
                                "type": "array",
                                "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d, \u0432 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0440\u0430\u043d\u0435\u0435 \u0431\u044b\u043b\u0438 \u0441\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u044b \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f \u0442\u043e\u0447\u0435\u043a."
                            },
                            "key": {
                                "maxLength": 1024,
                                "minLength": 1,
                                "type": "string",
                                "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                            },
                            "location": {
                                "additionalProperties": false,
                                "properties": {
                                    "arrival_duration": {
                                        "default": 0,
                                        "format": "int32",
                                        "maximum": 1440,
                                        "minimum": 0,
                                        "type": "integer",
                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u044a\u0435\u0437\u0434 (\u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0443) \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                    },
                                    "departure_duration": {
                                        "default": 0,
                                        "format": "int32",
                                        "maximum": 1440,
                                        "minimum": 0,
                                        "type": "integer",
                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043e\u0442\u044a\u0435\u0437\u0434 \u043e\u0442 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
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
                                "x-description-ru": "\u041b\u043e\u043a\u0430\u0446\u0438\u044f, \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435."
                            },
                            "reward": {
                                "default": 1000,
                                "format": "double",
                                "maximum": 1000000,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u0411\u0430\u0437\u043e\u0432\u043e\u0435 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430. \u0418\u0437 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f \u0432\u044b\u0447\u0438\u0442\u0430\u044e\u0442\u0441\u044f \u0448\u0442\u0440\u0430\u0444\u044b \u0437\u0430 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0432\u043e\u0432\u0440\u0435\u043c\u044f.\n"
                            },
                            "visits": {
                                "items": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "time_window": {
                                            "additionalProperties": false,
                                            "properties": {
                                                "from": {
                                                    "format": "date-time",
                                                    "type": "string",
                                                    "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                },
                                                "to": {
                                                    "format": "date-time",
                                                    "type": "string",
                                                    "x-description-ru": "\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                                }
                                            },
                                            "required": [
                                                "from",
                                                "to"
                                            ],
                                            "type": "object",
                                            "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e."
                                        }
                                    },
                                    "required": [
                                        "time_window"
                                    ],
                                    "type": "object",
                                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437."
                                },
                                "maxItems": 100,
                                "minItems": 1,
                                "type": "array",
                                "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d, \u0432 \u043a\u0430\u0436\u0434\u043e\u0435 \u0438\u0437 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435 \u0442\u043e\u0447\u043a\u0438."
                            }
                        },
                        "required": [
                            "key",
                            "location",
                            "visits",
                            "duration",
                            "reward"
                        ],
                        "type": "object",
                        "x-description-ru": "\u0417\u0430\u043a\u0430\u0437 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
                    },
                    "reason": {
                        "type": "string",
                        "x-description-ru": "\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u0430\u044f \u043f\u0440\u0438\u0447\u0438\u043d\u0430, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0437\u0430\u043a\u0430\u0437 \u043d\u0435 \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043b\u0441\u044f."
                    }
                },
                "required": [
                    "order"
                ],
                "type": "object",
                "x-description-ru": "\u041d\u0435\u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437."
            },
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0435\u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
        },
        "validations": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "entity_key": {
                        "maxLength": 1024,
                        "type": "string",
                        "x-description-ru": "\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0446\u0435\u043b\u0435\u0432\u043e\u0439 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0445."
                    },
                    "entity_type": {
                        "maxLength": 1024,
                        "type": "string",
                        "x-description-ru": "\u0422\u0438\u043f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438."
                    },
                    "info": {
                        "type": "string",
                        "x-description-ru": "\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u0438."
                    },
                    "type": {
                        "enum": [
                            "info",
                            "warning",
                            "error"
                        ],
                        "nullable": false,
                        "type": "string",
                        "x-description-ru": "\u0422\u0438\u043f \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u0438: * `info` - \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f * `warning` - \u043f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 * `error` - \u043e\u0448\u0438\u0431\u043a\u0430\n"
                    }
                },
                "required": [
                    "type",
                    "info"
                ],
                "type": "object",
                "x-description-ru": "\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0445."
            },
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u0439."
        }
    },
    "type": "object",
    "x-description-ru": "\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f."
}'''
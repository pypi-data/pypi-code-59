PLAN_TASK_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "delivery_settings": {
            "additionalProperties": false,
            "properties": {
                "restrict_middle_warehouses": {
                    "default": true,
                    "type": "boolean",
                    "x-description-ru": "\u0417\u0430\u043f\u0440\u0435\u0442\u0438\u0442\u044c \u0437\u0430\u0435\u0437\u0436\u0430\u0442\u044c \u0432 \u0441\u0435\u0440\u0435\u0434\u0438\u043d\u0435 \u0440\u0435\u0439\u0441\u0430 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434 - \u0432\u0441\u0435\u0433\u0434\u0430 \u043d\u0430\u0447\u0438\u043d\u0430\u0442\u044c \u0438\\\u0438\u043b\u0438 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0442\u044c \u0440\u0435\u0439\u0441 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435."
                },
                "restrict_multiple_order_types": {
                    "default": false,
                    "type": "boolean",
                    "x-description-ru": "\u0417\u0430\u043f\u0440\u0435\u0442\u0438\u0442\u044c \u0432 \u043e\u0434\u043d\u043e\u043c \u0440\u0435\u0439\u0441\u0435 \u0432\u043e\u0437\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u044b \u0441 \u0442\u0438\u043f\u043e\u043c `PICKUP` \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u043e \u0441 \u0442\u0438\u043f\u043e\u043c `DROP`.\n"
                },
                "restrict_multiple_warehouses": {
                    "default": true,
                    "type": "boolean",
                    "x-description-ru": "\u0417\u0430\u043f\u0440\u0435\u0442\u0438\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e \u0432 \u043e\u0434\u043d\u043e\u043c \u0440\u0435\u0439\u0441\u0435 \u0437\u0430\u0435\u0437\u0436\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435, \u0447\u0435\u043c \u043d\u0430 \u043e\u0434\u0438\u043d \u0441\u043a\u043b\u0430\u0434. \u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u043a\u043e\u0433\u0434\u0430 \u0443 \u0432\u0441\u0435\u0445 \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u043e\u0434\u0438\u043d \u0441\u043a\u043b\u0430\u0434. \u0415\u0441\u043b\u0438 \u0443 \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u0437 \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043e \u0431\u043e\u043b\u044c\u0448\u0435 \u043e\u0434\u043d\u043e\u0433\u043e \u0441\u043a\u043b\u0430\u0434\u0430 \u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0430 \u044d\u0442\u0430 \u043e\u043f\u0446\u0438\u044f, \u0442\u043e \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u044f \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0434\u0430\u0432\u0430\u0442\u044c \u043e\u0448\u0438\u0431\u043a\u0443.\n"
                }
            },
            "type": "object",
            "x-description-ru": "\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f."
        },
        "orders": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "blacklist": {
                        "default": [],
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0417\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u043d\u043e\u0435 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439, \u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0443 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043d\u0435 \u0434\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u043e. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0438 \u0437\u0430\u043a\u0430\u0437\u0430 (\u0440\u0430\u0431\u043e\u0442\u044b).\n"
                    },
                    "cargos": {
                        "items": {
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
                                "height": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0412\u044b\u0441\u043e\u0442\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0432 \u043e\u0442\u0441\u0435\u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                },
                                "key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0433\u0440\u0443\u0437\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                                },
                                "length": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0414\u043b\u0438\u043d\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0432 \u043e\u0442\u0441\u0435\u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                },
                                "max_storage_time": {
                                    "default": 43800,
                                    "format": "int32",
                                    "maximum": 43800,
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043d\u0430 \u0431\u043e\u0440\u0442\u0443, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445.  \u0415\u0441\u043b\u0438 \u043d\u0435 \u0437\u0430\u0434\u0430\u043d\u043e - \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f.\n"
                                },
                                "restrictions": {
                                    "items": {
                                        "maxLength": 256,
                                        "minLength": 1,
                                        "type": "string",
                                        "x-description-ru": "\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043a \u043e\u0442\u0441\u0435\u043a\u0443."
                                    },
                                    "maxItems": 100,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true,
                                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u043e\u0442\u0441\u0435\u043a\u0443, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043c\u043e\u0436\u0435\u0442 \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u0438\u0442\u044c \u0433\u0440\u0443\u0437."
                                },
                                "width": {
                                    "default": 0,
                                    "format": "double",
                                    "maximum": 1000000,
                                    "minimum": 0,
                                    "type": "number",
                                    "x-description-ru": "\u0428\u0438\u0440\u0438\u043d\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0432 \u043e\u0442\u0441\u0435\u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                }
                            },
                            "required": [
                                "key"
                            ],
                            "type": "object",
                            "x-description-ru": "\u0413\u0440\u0443\u0437."
                        },
                        "maxItems": 1000,
                        "minItems": 1,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u0437\u043e\u0432. \u0412\u0441\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0435 \u0433\u0440\u0443\u0437\u044b \u0431\u0435\u0440\u0443\u0442\u0441\u044f \u0438\u0437 \u043e\u0434\u043d\u043e\u0439 \u0442\u043e\u0447\u043a\u0438 \u0438 \u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044e\u0442\u0441\u044f \u043d\u0430 \u0434\u0440\u0443\u0433\u0443\u044e \u0442\u043e\u0447\u043a\u0443 \u043e\u0434\u043d\u0438\u043c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043c \u0437\u0430 \u043e\u0434\u0438\u043d \u0440\u0435\u0439\u0441.\n"
                    },
                    "cost": {
                        "additionalProperties": false,
                        "properties": {
                            "penalty": {
                                "additionalProperties": false,
                                "properties": {
                                    "max_value": {
                                        "default": 0,
                                        "format": "double",
                                        "maximum": 1000000,
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0448\u0442\u0440\u0430\u0444\u0430."
                                    },
                                    "period": {
                                        "default": 60,
                                        "format": "int32",
                                        "maximum": 1440,
                                        "minimum": 1,
                                        "type": "integer",
                                        "x-description-ru": "\u041f\u0435\u0440\u0438\u043e\u0434 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445, \u043f\u043e \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u0438 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u0441\u0443\u043c\u043c\u0430 \u0448\u0442\u0440\u0430\u0444\u0430 \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043d\u0430 `value`."
                                    },
                                    "start_time": {
                                        "format": "date-time",
                                        "type": "string",
                                        "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0433\u043e \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0448\u0442\u0440\u0430\u0444."
                                    },
                                    "value": {
                                        "default": 0,
                                        "format": "double",
                                        "maximum": 1000000,
                                        "minimum": 0,
                                        "type": "number",
                                        "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0448\u0442\u0440\u0430\u0444 \u043a\u0430\u0436\u0434\u044b\u0439 `period`."
                                    }
                                },
                                "required": [
                                    "start_time",
                                    "period",
                                    "value",
                                    "max_value"
                                ],
                                "type": "object",
                                "x-description-ru": "\u0428\u0442\u0440\u0430\u0444 \u0437\u0430 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0432\u043e\u0432\u0440\u0435\u043c\u044f. \u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u0432 \u0432\u0438\u0434\u0435 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 - \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043a\u0430\u0436\u0434\u044b\u0435 period \u043c\u0438\u043d\u0443\u0442 \u043d\u0430 `value` \u043d\u0430\u0447\u0438\u043d\u0430\u044f \u0441 `start_time`. \u0414\u0435\u0439\u0441\u0442\u0432\u0443\u0435\u0442 \u043d\u0430 \u0432\u0441\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u043a\u0430\u0437\u0430.\n"
                            },
                            "reward": {
                                "default": 1000,
                                "format": "double",
                                "maximum": 1000000,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u0411\u0430\u0437\u043e\u0432\u043e\u0435 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430. \u0418\u0437 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f \u0432\u044b\u0447\u0438\u0442\u0430\u044e\u0442\u0441\u044f \u0448\u0442\u0440\u0430\u0444\u044b \u0437\u0430 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0432\u043e\u0432\u0440\u0435\u043c\u044f.\n"
                            }
                        },
                        "required": [
                            "reward"
                        ],
                        "type": "object",
                        "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u044f \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0438 \u0448\u0442\u0440\u0430\u0444\u0430 \u0437\u0430 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u0432\u043e\u0432\u0440\u0435\u043c\u044f."
                    },
                    "customer": {
                        "additionalProperties": false,
                        "properties": {
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
                            "time_windows": {
                                "items": {
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
                                "maxItems": 100,
                                "minItems": 0,
                                "type": "array",
                                "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u043e\u043a\u043e\u043d \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438."
                            }
                        },
                        "required": [
                            "location",
                            "time_windows"
                        ],
                        "type": "object",
                        "x-description-ru": "\u041a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u0430\u044f \u0442\u043e\u0447\u043a\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0440\u0430\u0437\u0432\u043e\u0437\u043a\u0430 \u0438 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442 \u0433\u0440\u0443\u0437\u044b."
                    },
                    "customer_duration": {
                        "default": 0,
                        "format": "double",
                        "maximum": 43800,
                        "minimum": 0,
                        "type": "number",
                        "x-description-ru": "\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0443 \u0432\u0441\u0435\u0445 \u0433\u0440\u0443\u0437\u043e\u0432 \u043e\u0434\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                    },
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u043a\u0430\u0437\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                    },
                    "restrictions": {
                        "default": [],
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0438 \u0437\u0430\u043a\u0430\u0437\u0430 (\u0440\u0430\u0431\u043e\u0442\u044b).\n"
                    },
                    "type": {
                        "default": "DROP",
                        "enum": [
                            "DROP",
                            "PICKUP"
                        ],
                        "nullable": false,
                        "type": "string",
                        "x-description-ru": "\u0422\u0438\u043f \u0437\u0430\u043a\u0430\u0437\u0430:\n  * `DROP` - \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0430 \u0433\u0440\u0443\u0437\u0430 \u0441\u043e \u0441\u043a\u043b\u0430\u0434\u0430 \u043d\u0430 \u0442\u043e\u0447\u043a\u0443\n  * `PICKUP` - \u0437\u0430\u0431\u043e\u0440 \u0433\u0440\u0443\u0437\u0430 \u043d\u0430 \u0442\u043e\u0447\u043a\u0435 \u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u043e\u0439 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\n"
                    },
                    "warehouse_duration": {
                        "default": 0,
                        "format": "double",
                        "maximum": 43800,
                        "minimum": 0,
                        "type": "number",
                        "x-description-ru": "\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u043d\u0430 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0443 \u0432\u0441\u0435\u0445 \u0433\u0440\u0443\u0437\u043e\u0432 \u043e\u0434\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                    },
                    "warehouse_keys": {
                        "items": {
                            "maxLength": 1024,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u041a\u043b\u044e\u0447 \u0441\u043a\u043b\u0430\u0434\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                        },
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u044e\u0447\u0435\u0439 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0445 \u0441\u043a\u043b\u0430\u0434\u043e\u0432 \u0434\u043b\u044f \u0437\u0430\u0431\u043e\u0440\u0430 \u0438\u043b\u0438 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u0433\u0440\u0443\u0437\u0430."
                    }
                },
                "required": [
                    "key",
                    "warehouse_keys",
                    "customer",
                    "cargos"
                ],
                "type": "object",
                "x-description-ru": "\u0417\u0430\u043a\u0430\u0437 \u043d\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0443 \u0433\u0440\u0443\u0437\u0430 \u0432 \u043b\u043e\u043a\u0430\u0446\u0438\u044e \u0438\u043b\u0438 \u0437\u0430\u0431\u043e\u0440 \u0433\u0440\u0443\u0437\u0430 \u0438\u0437 \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043a\u0430\u0437\u043e\u0432"
        },
        "performers": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "box": {
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
                            "features": {
                                "items": {
                                    "maxLength": 256,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043e\u0442\u0441\u0435\u043a\u0430."
                                },
                                "maxItems": 1000,
                                "minItems": 0,
                                "type": "array",
                                "uniqueItems": true,
                                "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u043e\u0442\u0441\u0435\u043a\u0430, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u043e\u043c\u0443 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442\u0441\u044f \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c \u0441 \u0433\u0440\u0443\u0437\u043e\u043c."
                            },
                            "height": {
                                "default": 0,
                                "format": "double",
                                "maximum": 1000000,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u0412\u044b\u0441\u043e\u0442\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445."
                            },
                            "key": {
                                "maxLength": 1024,
                                "minLength": 1,
                                "type": "string",
                                "x-description-ru": "\u041a\u043b\u044e\u0447 \u043e\u0442\u0441\u0435\u043a\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 \u0440\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u044f \u0433\u0440\u0443\u0437\u043e\u0432 \u043f\u043e \u043e\u0442\u0441\u0435\u043a\u0430\u043c."
                            },
                            "length": {
                                "default": 0,
                                "format": "double",
                                "maximum": 1000000,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u0414\u043b\u0438\u043d\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445."
                            },
                            "max_size": {
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
                            "width": {
                                "default": 0,
                                "format": "double",
                                "maximum": 1000000,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u0428\u0438\u0440\u0438\u043d\u0430 \u0432 \u043c\u0435\u0442\u0440\u0430\u0445."
                            }
                        },
                        "required": [
                            "key"
                        ],
                        "type": "object",
                        "x-description-ru": "\u041e\u0442\u0441\u0435\u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0441\u043f\u043e\u0441\u043e\u0431\u0435\u043d \u0432\u043c\u0435\u0449\u0430\u0442\u044c \u0433\u0440\u0443\u0437\u044b. `capacity` - \u0412\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0442\u0441\u0435\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0438\u0432\u0430\u0435\u0442 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0441\u0443\u043c\u043c\u0443 \u043f\u043e \u0432\u0441\u0435\u043c \u043f\u043e\u043b\u044f\u043c capacity \u0443 *\u0432\u0441\u0435\u0445* \u0433\u0440\u0443\u0437\u043e\u0432. `max_size` - \u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u043f\u043e\u043b\u044f\u043c capacity \u0434\u043b\u044f *\u043e\u0434\u043d\u043e\u0433\u043e* \u0433\u0440\u0443\u0437\u0430.\n"
                    },
                    "count": {
                        "default": 1,
                        "format": "int32",
                        "maximum": 5000,
                        "minimum": 1,
                        "type": "integer",
                        "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u0445 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 \u0432 \u0434\u0430\u043d\u043d\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u0435."
                    },
                    "features": {
                        "default": [],
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0441 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438.\n"
                    },
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
                        "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
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
                            "x-description-ru": "\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u0441\u043c\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f.\n  * `availability_time` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0441\u043c\u0435\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445 \u0438 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c\u0438.\n  * `working_time` - \u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0441\u043c\u0435\u043d\u044b.\n"
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
                    "shifts"
                ],
                "type": "object",
                "x-description-ru": "\u0413\u0440\u0443\u043f\u043f\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439.  \u0415\u0441\u043b\u0438 \u0443 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0430 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f/\u043a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u043b\u043e\u043a\u0430\u0446\u0438\u044f, \u0442\u043e \u0440\u0435\u0439\u0441 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u0438 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u043f\u0435\u0440\u0432\u043e\u043c/\u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u043c \u0437\u0430\u043a\u0430\u0437\u0435.\n"
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439, \u0441 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u043c \u0438\u0445 \u0440\u0430\u0431\u043e\u0442\u044b \u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430\u043c\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
        },
        "settings": {
            "additionalProperties": false,
            "nullable": false,
            "properties": {
                "assumptions": {
                    "additionalProperties": false,
                    "nullable": false,
                    "properties": {
                        "disable_capacity": {
                            "default": false,
                            "type": "boolean",
                            "x-description-ru": "\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0443\u0447\u0435\u0442 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0435\u0439. \u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043e `true` - \u0432\u0435\u0441\u044c \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442 \u0432\u043c\u0435\u0449\u0430\u0435\u0442 \u043d\u0435\u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0433\u0440\u0443\u0437\u043e\u0432.\n"
                        },
                        "disable_compatibility": {
                            "default": false,
                            "type": "boolean",
                            "x-description-ru": "\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0443\u0447\u0435\u0442 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0435\u0439. \u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043e true - \u0432\u0441\u0435 \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e \u0441\u043e \u0432\u0441\u0435\u043c.\n"
                        },
                        "expand_shift_time_window": {
                            "default": false,
                            "type": "boolean",
                            "x-description-ru": "\u0420\u0430\u0441\u0448\u0438\u0440\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0434\u043b\u044f \u0441\u043c\u0435\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 \u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430.  \u041b\u0435\u0432\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0435\u0440\u0432\u043e\u0439 \u0441\u043c\u0435\u043d\u044b \u043e\u0434\u043d\u043e\u0439 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0440\u0430\u0441\u0448\u0438\u0440\u044f\u0435\u0442\u0441\u044f \u0434\u043e \u043b\u0435\u0432\u043e\u0439 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430, \u043f\u0440\u0430\u0432\u0430\u044f \u0434\u043e \u043f\u0440\u0430\u0432\u043e\u0439 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0438\u043b\u0438 \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u043e\u043a\u043d\u0430 \u043d\u0430 \u044d\u0442\u0443 \u0436\u0435 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u044c. \u041a\u0430\u0436\u0434\u0430\u044f \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0430\u044f \u0441\u043c\u0435\u043d\u0430 \u0441\u0434\u0432\u0438\u0433\u0430\u0435\u0442 \u043f\u0440\u0430\u0432\u0443\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0434\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0439 \u0441\u043c\u0435\u043d\u044b \u0438\u043b\u0438 \u0434\u043e \u043f\u0440\u0430\u0432\u043e\u0439 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430.\n"
                        },
                        "flight_distance": {
                            "default": false,
                            "type": "boolean",
                            "x-description-ru": "\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u043f\u043e \u043f\u0440\u044f\u043c\u043e\u0439. \u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043e `false` - \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043f\u043e \u0434\u043e\u0440\u043e\u0433\u0430\u043c. \u041f\u0440\u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0438 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 \u0443\u0447\u0435\u0442 \u043f\u0440\u043e\u0431\u043e\u043a (`traffic_jams`) \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0432\u044b\u043a\u043b\u044e\u0447\u0430\u0435\u0442\u0441\u044f.\n"
                        },
                        "same_order_time_window": {
                            "default": false,
                            "type": "boolean",
                            "x-description-ru": "\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u043e\u0432 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0435 (\u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0435) \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0434\u043b\u044f \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0438 \u0437\u0430\u044f\u0432\u043e\u043a. \u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0431\u0435\u0440\u0435\u0442\u0441\u044f \u043e\u0442 \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u0430\u043c\u043e\u0433\u043e \u0440\u0430\u043d\u043d\u0435\u0433\u043e \u0434\u043e \u043a\u043e\u043d\u0446\u0430 \u0441\u0430\u043c\u043e\u0433\u043e \u043f\u043e\u0437\u0434\u043d\u0435\u0433\u043e \u043e\u043a\u043d\u0430 \u0438\u0437 \u0432\u0441\u0435\u0445 \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0438 \u0437\u0430\u044f\u0432\u043e\u043a.\n"
                        },
                        "traffic_jams": {
                            "default": true,
                            "type": "boolean",
                            "x-description-ru": "\u0423\u0447\u0435\u0442 \u043f\u0440\u043e\u0431\u043e\u043a \u043f\u0440\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432."
                        }
                    },
                    "type": "object",
                    "x-description-ru": "\u0414\u043e\u043f\u0443\u0449\u0435\u043d\u0438\u044f \u043f\u0440\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438 - \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0447\u0430\u0441\u0442\u044c \u0431\u0438\u0437\u043d\u0435\u0441-\u043b\u043e\u0433\u0438\u043a\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.\n"
                },
                "capacity_factor": {
                    "default": [],
                    "items": {
                        "additionalProperties": false,
                        "properties": {
                            "capacity": {
                                "default": 1,
                                "format": "double",
                                "maximum": 10,
                                "minimum": 0.1,
                                "type": "number",
                                "x-description-ru": "\u041c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c \u043e\u0431\u044c\u0435\u043c\u0430 \u043e\u0442\u0441\u0435\u043a\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430. \u0423\u043c\u043d\u043e\u0436\u0430\u0435\u0442 \u0432\u0441\u0435 \u043f\u043e\u043b\u044f `capacity` \u0443 \u0432\u0441\u0435\u0445 \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0443 \u0432\u0441\u0435\u0445 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u0432 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u0438\u043f\u0430.\n"
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
                            "transport_type",
                            "capacity"
                        ],
                        "type": "object",
                        "x-description-ru": "\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u0438\u043f\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                    },
                    "maxItems": 7,
                    "minItems": 0,
                    "type": "array",
                    "x-description-ru": "\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                },
                "configuration": {
                    "default": "default",
                    "maxLength": 1000,
                    "minLength": 1,
                    "type": "string",
                    "x-description-ru": "\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f. \u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u0446\u0435\u043b\u044c \u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430. [\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0445](https://docs.veeroute.com/#/lss/scenarios?id=\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f-\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f) \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u0439 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.\n"
                },
                "planning_time": {
                    "default": 20,
                    "format": "int32",
                    "maximum": 2880,
                    "minimum": 1,
                    "type": "integer",
                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. C\u0442\u0430\u0440\u0442 \u043e\u0442\u0441\u0447\u0435\u0442\u0430 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u043e\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440 \u0438 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.\n"
                },
                "precision": {
                    "default": 2,
                    "format": "int32",
                    "maximum": 6,
                    "minimum": 0,
                    "type": "integer",
                    "x-description-ru": "\u0423\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u0438 \u043f\u043e\u043b\u0435\u0439 \u0442\u0438\u043f\u0430 double \u0432 \u043f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u043e\u043c \u043d\u043e\u043c\u0435\u0440\u0435 \u0437\u043d\u0430\u043a\u0430 \u043f\u043e\u0441\u043b\u0435 \u0437\u0430\u043f\u044f\u0442\u043e\u0439. \u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e 2, \u0442.\u0435. \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c 0.01.\n"
                },
                "predict_slots": {
                    "default": 0,
                    "format": "int32",
                    "maximum": 4,
                    "minimum": 0,
                    "type": "integer",
                    "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0442\u043e\u0432 \u0434\u043b\u044f \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d. \u041f\u0440\u0438 \u043d\u0443\u043b\u0435\u0432\u043e\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438 \u043e\u043a\u043e\u043d \u043d\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u0430\u0432\u043b\u0438\u0432\u0430\u044e\u0442\u0441\u044f. \u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435 \u043f\u0440\u043e [\u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d](https://docs.veeroute.com/#/lss/scenarios?id=\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430-\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445-\u043e\u043a\u043e\u043d).\n"
                },
                "result_timezone": {
                    "default": 0,
                    "format": "int32",
                    "maximum": 12,
                    "minimum": -12,
                    "type": "integer",
                    "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u0437\u043e\u043d\u0430, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.\n"
                },
                "result_ttl": {
                    "default": 20,
                    "format": "int32",
                    "maximum": 14400,
                    "minimum": 1,
                    "type": "integer",
                    "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u0436\u0438\u0437\u043d\u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. C\u0442\u0430\u0440\u0442 \u043e\u0442\u0441\u0447\u0435\u0442\u0430 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u043e\u0442 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.\n"
                },
                "routing": {
                    "default": [],
                    "items": {
                        "additionalProperties": false,
                        "properties": {
                            "matrix": {
                                "additionalProperties": false,
                                "nullable": true,
                                "properties": {
                                    "distances": {
                                        "items": {
                                            "items": {
                                                "format": "int64",
                                                "maximum": 10000000,
                                                "minimum": -1,
                                                "type": "integer",
                                                "x-description-ru": "\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 (\u0432 \u043c\u0435\u0442\u0440\u0430\u0445) \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c (\u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445) \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u0442\u043e\u0447\u043a\u0430\u043c\u0438. \u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (-1) \u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442 \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0435\u0437\u0434\u0430 \u043c\u0435\u0436\u0434\u0443 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c\u0438 \u0442\u043e\u0447\u043a\u0430\u043c\u0438.\n"
                                            },
                                            "maxItems": 9000,
                                            "minItems": 2,
                                            "type": "array",
                                            "uniqueItems": false,
                                            "x-description-ru": "\u041b\u0438\u043d\u0438\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0432 \u043c\u0430\u0442\u0440\u0438\u0446\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 (\u0432 \u043c\u0435\u0442\u0440\u0430\u0445) \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0435\u0439 (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445) \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432 \u043c\u0435\u0436\u0434\u0443 \u0442\u043e\u0447\u043a\u0430\u043c\u0438."
                                        },
                                        "maxItems": 9000,
                                        "minItems": 2,
                                        "type": "array",
                                        "uniqueItems": false,
                                        "x-description-ru": "\u0414\u043b\u0438\u043d\u044b \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432 \u043c\u0435\u0436\u0434\u0443 \u0442\u043e\u0447\u043a\u0430\u043c\u0438, \u0432 \u043c\u0435\u0442\u0440\u0430\u0445.         \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u043c\u0430\u0441\u0441\u0438\u0432\u0435 \u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0435\u043d\u044b \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 \u043f\u043e\u0440\u044f\u0434\u043a\u043e\u043c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0435 waypoints. \u041a\u0430\u0436\u0434\u0430\u044f \u0441\u0442\u0440\u043e\u0447\u043a\u0430 \u043c\u0430\u0442\u0440\u0438\u0446\u044b - \u043c\u0430\u0441\u0441\u0438\u0432 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 \u0438\u0437 \u0438\u0441\u043a\u043e\u043c\u043e\u0439 \u0442\u043e\u0447\u043a\u0438 \u0434\u043e \u043a\u0430\u0436\u0434\u043e\u0439 \u0434\u0440\u0443\u0433\u043e\u0439 \u0442\u043e\u0447\u043a\u0438.\n"
                                    },
                                    "durations": {
                                        "items": {
                                            "items": {
                                                "format": "int64",
                                                "maximum": 10000000,
                                                "minimum": -1,
                                                "type": "integer",
                                                "x-description-ru": "\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 (\u0432 \u043c\u0435\u0442\u0440\u0430\u0445) \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c (\u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445) \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u0442\u043e\u0447\u043a\u0430\u043c\u0438. \u041e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 (-1) \u043e\u0437\u043d\u0430\u0447\u0430\u0435\u0442 \u043d\u0435\u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0435\u0437\u0434\u0430 \u043c\u0435\u0436\u0434\u0443 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u043c\u0438 \u0442\u043e\u0447\u043a\u0430\u043c\u0438.\n"
                                            },
                                            "maxItems": 9000,
                                            "minItems": 2,
                                            "type": "array",
                                            "uniqueItems": false,
                                            "x-description-ru": "\u041b\u0438\u043d\u0438\u044f \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439 \u0432 \u043c\u0430\u0442\u0440\u0438\u0446\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 (\u0432 \u043c\u0435\u0442\u0440\u0430\u0445) \u0438\u043b\u0438 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0435\u0439 (\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445) \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432 \u043c\u0435\u0436\u0434\u0443 \u0442\u043e\u0447\u043a\u0430\u043c\u0438."
                                        },
                                        "maxItems": 9000,
                                        "minItems": 2,
                                        "type": "array",
                                        "uniqueItems": false,
                                        "x-description-ru": "\u041c\u0430\u0441\u0441\u0438\u0432 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0435\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u043e\u0432 \u043c\u0435\u0436\u0434\u0443 \u0442\u043e\u0447\u043a\u0430\u043c\u0438, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445. \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 \u043c\u0430\u0441\u0441\u0438\u0432\u0435 \u0443\u043f\u043e\u0440\u044f\u0434\u043e\u0447\u0435\u043d\u044b \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 \u043f\u043e\u0440\u044f\u0434\u043a\u043e\u043c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0435 waypoints. \u041a\u0430\u0436\u0434\u0430\u044f \u0441\u0442\u0440\u043e\u0447\u043a\u0430 \u043c\u0430\u0442\u0440\u0438\u0446\u044b - \u043c\u0430\u0441\u0441\u0438\u0432 \u0432\u0440\u0435\u043c\u0435\u043d \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0439 \u0438\u0437 \u0438\u0441\u043a\u043e\u043c\u043e\u0439 \u0442\u043e\u0447\u043a\u0438 \u0434\u043e \u043a\u0430\u0436\u0434\u043e\u0439 \u0434\u0440\u0443\u0433\u043e\u0439 \u0442\u043e\u0447\u043a\u0438.\n"
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
                                        "x-description-ru": "\u041c\u0430\u0441\u0441\u0438\u0432 \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0442\u043e\u0447\u0435\u043a, \u043c\u0435\u0436\u0434\u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u044b \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0430."
                                    }
                                },
                                "required": [
                                    "waypoints",
                                    "distances",
                                    "durations"
                                ],
                                "type": "object",
                                "x-description-ru": "\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 \u0438 \u0432\u0440\u0435\u043c\u0435\u043d."
                            },
                            "traffic_jams": {
                                "items": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "length_additive": {
                                            "default": 0,
                                            "format": "double",
                                            "maximum": 100000,
                                            "minimum": -100000,
                                            "type": "number",
                                            "x-description-ru": "\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e, \u0432 \u043c\u0435\u0442\u0440\u0430\u0445."
                                        },
                                        "length_multiplier": {
                                            "default": 1,
                                            "format": "double",
                                            "maximum": 100,
                                            "minimum": 0,
                                            "type": "number",
                                            "x-description-ru": "\u041c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u044f."
                                        },
                                        "time_additive": {
                                            "default": 0,
                                            "format": "double",
                                            "maximum": 1440,
                                            "minimum": -1440,
                                            "type": "number",
                                            "x-description-ru": "\u0423\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043d\u0430 \u0434\u0430\u043d\u043d\u043e\u0435 \u0447\u0438\u0441\u043b\u043e, \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                        },
                                        "time_multiplier": {
                                            "default": 1,
                                            "format": "double",
                                            "maximum": 100,
                                            "minimum": 0,
                                            "type": "number",
                                            "x-description-ru": "\u041c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c \u0432\u0440\u0435\u043c\u0435\u043d\u0438."
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
                                        }
                                    },
                                    "required": [
                                        "time_window"
                                    ],
                                    "type": "object",
                                    "x-description-ru": "\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u0438\u0438 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044f \u0432 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a."
                                },
                                "maxItems": 24,
                                "minItems": 0,
                                "type": "array",
                                "x-description-ru": "\u041d\u0430\u0431\u043e\u0440 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u043e\u0432 \u0432\u0440\u0435\u043c\u0435\u043d \u0438 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043a\u0430 \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u043f\u0440\u043e\u0431\u043e\u043a."
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
                            "transport_type",
                            "matrix"
                        ],
                        "type": "object",
                        "x-description-ru": "\u041c\u0430\u0442\u0440\u0438\u0446\u0430 \u0432\u0440\u0435\u043c\u0435\u043d \u0438 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 \u0434\u043b\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0442\u0438\u043f\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                    },
                    "maxItems": 7,
                    "minItems": 0,
                    "type": "array",
                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043c\u0430\u0442\u0440\u0438\u0446 \u0432\u0440\u0435\u043c\u0435\u043d \u0438 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0439 \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0442\u0438\u043f\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430. \u041f\u0440\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u0432\u043d\u0435\u0448\u043d\u0435\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0438\u0437\u0430\u0446\u0438\u0438 \u043d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b `flight_distance`, `traffic_jams`, `transport_factor`.\n"
                },
                "transport_factor": {
                    "default": [],
                    "items": {
                        "additionalProperties": false,
                        "properties": {
                            "speed": {
                                "format": "double",
                                "maximum": 1000,
                                "minimum": 0.1,
                                "type": "number",
                                "x-description-ru": "\u041c\u043d\u043e\u0436\u0438\u0442\u0435\u043b\u044c \u0441\u0440\u0435\u0434\u043d\u0435\u0439 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
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
                            "transport_type",
                            "speed"
                        ],
                        "type": "object",
                        "x-description-ru": "\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u0442\u0438\u043f\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                    },
                    "maxItems": 7,
                    "minItems": 0,
                    "type": "array",
                    "x-description-ru": "\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                }
            },
            "type": "object",
            "x-description-ru": "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f."
        },
        "trips": {
            "items": {
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
                                "order_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u043a\u0430\u0437\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435."
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
                                },
                                "warehouse_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0442\u043e\u0447\u043a\u0438 (\u0441\u043a\u043b\u0430\u0434 \u0438\u043b\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u0430), \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435. \u0415\u0441\u043b\u0438 \u043a\u043b\u044e\u0447 \u0443\u043a\u0430\u0437\u0430\u043d - \u0437\u043d\u0430\u0447\u0438\u0442 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435, \u0435\u0441\u043b\u0438 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d - \u0443 \u043a\u043b\u0438\u0435\u043d\u0442\u0430.\n"
                                }
                            },
                            "required": [
                                "order_key",
                                "order_time",
                                "location_time"
                            ],
                            "type": "object",
                            "x-description-ru": "\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0437\u0430\u043a\u0430\u0437\n  * `order_time` - \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0438 \u043a\u043e\u043d\u0446\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430\u0434 \u0437\u0430\u043a\u0430\u0437\u043e\u043c \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n  * `location_time` - \u0432\u0440\u0435\u043c\u044f \u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438.\n"
                        },
                        "maxItems": 1000,
                        "minItems": 1,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u043d\u0430\u0434 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438."
                    },
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0435\u0439\u0441\u0430."
                    },
                    "performer_key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f."
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
                            "maxLength": 1024,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u043a\u0430\u0437\u0430."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u044e\u0447\u0435\u0439 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0445, \u043d\u043e \u043d\u0435 \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                    }
                },
                "required": [
                    "key",
                    "performer_key",
                    "trip_time"
                ],
                "type": "object",
                "x-description-ru": "\u0420\u0435\u0439\u0441 - \u044d\u0442\u043e \u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 (`actions`) \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u043c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043c. \u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0435\u0439\u0441\u0430 \u0438 \u0435\u0433\u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f \u0443\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0432 `trip_time`.\n"
            },
            "maxItems": 9000,
            "minItems": 0,
            "type": "array",
            "x-description-ru": "\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0440\u0435\u0439\u0441\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0435\u0440\u0435\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c."
        },
        "warehouses": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0441\u043a\u043b\u0430\u0434\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
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
                    "work_windows": {
                        "items": {
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
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d \u0440\u0430\u0431\u043e\u0442\u044b, \u0435\u0441\u043b\u0438 \u043e\u043a\u043d\u0430 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u044b - \u0442\u043e\u0447\u043a\u0430 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u043a\u0440\u0443\u0433\u043b\u043e\u0441\u0443\u0442\u043e\u0447\u043d\u043e."
                    }
                },
                "required": [
                    "key",
                    "location"
                ],
                "type": "object",
                "x-description-ru": "\u0421\u043a\u043b\u0430\u0434\u0441\u043a\u0430\u044f \u0442\u043e\u0447\u043a\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0440\u0430\u0437\u0432\u043e\u0437\u043a\u0430 \u0438 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u044e\u0442 \u0433\u0440\u0443\u0437\u044b."
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043a\u043b\u0430\u0434\u043e\u0432 \u0434\u043b\u044f \u0437\u0430\u0431\u043e\u0440\u0430 \u0438\u043b\u0438 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u0433\u0440\u0443\u0437\u0430."
        }
    },
    "required": [
        "warehouses",
        "orders",
        "performers"
    ],
    "type": "object",
    "x-description-ru": "\u0417\u0430\u0434\u0430\u0447\u0430 \u0434\u043b\u044f \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f."
}'''
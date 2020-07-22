PLAN_TASK_SCHEMA = '''{
    "additionalProperties": false,
    "properties": {
        "hardlinks": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f."
                    },
                    "links": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "entity_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438-\u0446\u0435\u043b\u0438 (\u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0437\u0430\u043a\u0430\u0437\u0430 \u0438\u043b\u0438 \u0441\u043c\u0435\u043d\u044b)."
                                },
                                "type": {
                                    "enum": [
                                        "ORDER",
                                        "SHIFT"
                                    ],
                                    "nullable": false,
                                    "type": "string",
                                    "x-description-ru": "\u0422\u0438\u043f \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438-\u0446\u0435\u043b\u0438, \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u043e\u043c (ORDER) \u0438\u043b\u0438 \u0441\u043c\u0435\u043d\u043e\u0439 (SHIFT)."
                                }
                            },
                            "required": [
                                "type",
                                "entity_key"
                            ],
                            "type": "object",
                            "x-description-ru": "\u042d\u043b\u0435\u043c\u0435\u043d\u0442 \u0433\u0440\u0443\u043f\u043f\u044b \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f."
                        },
                        "maxItems": 1000,
                        "minItems": 2,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0433\u0440\u0443\u043f\u043f\u044b \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f."
                    }
                },
                "required": [
                    "key",
                    "links"
                ],
                "type": "object",
                "x-description-ru": "\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0435 \u0447\u0442\u043e\u0431\u044b \u0441\u0432\u044f\u0437\u0430\u0442\u044c \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0438 \u0432 \u043e\u0434\u043d\u0443 \u0433\u0440\u0443\u043f\u043f\u0443. \u041c\u043e\u0436\u0435\u0442 \u0441\u043e\u0441\u0442\u043e\u044f\u0442\u044c \u0438\u0437 \u0434\u0432\u0443\u0445 \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u0435\u0439 \u0438\u043b\u0438 \u0431\u043e\u043b\u0435\u0435. \u041f\u0440\u0438\u043c\u0435\u0440 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f:\n  * \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043d\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442 (\u0441\u0432\u044f\u0437\u044c \u0441\u043c\u0435\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0438 \u0442\u0440\u0430\u0441\u043f\u043e\u0440\u0442\u0430).\n  * \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430 \u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f (\u0441\u0432\u044f\u0437\u044c \u0437\u0430\u043a\u0430\u0437\u0430 \u0441\u043e \u0441\u043c\u0435\u043d\u043e\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f).\n  * \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u0432 \u043e\u0434\u043d\u043e\u043c \u0440\u0435\u0439\u0441\u0435 (\u0441\u0432\u044f\u0437\u044c \u0437\u0430\u043a\u0430\u0437\u043e\u0432 \u043c\u0435\u0436\u0434\u0443 \u0441\u043e\u0431\u043e\u0439).\n"
            },
            "maxItems": 9000,
            "minItems": 0,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0439."
        },
        "locations": {
            "items": {
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                    },
                    "load_windows": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "gates_count": {
                                    "default": 0,
                                    "format": "int32",
                                    "maximum": 9000,
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430 \u0432 \u0434\u0430\u043d\u043d\u043e\u043c \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u043c \u043e\u043a\u043d\u0435.  \u0415\u0441\u043b\u0438 0, \u0442\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f.  \u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0438\u043b\u044c\u043d\u043e \u0432\u043b\u0438\u044f\u0435\u0442 \u043d\u0430 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u044f.\n"
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
                            "type": "object",
                            "x-description-ru": "\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0440\u0430\u0431\u043e\u0442\u044b \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
                        },
                        "maxItems": 100,
                        "minItems": 0,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d \u0440\u0430\u0431\u043e\u0442\u044b \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
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
                    "transport_restrictions": {
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043c\u043e\u0436\u0435\u0442 \u043f\u0440\u0438\u0435\u0437\u0436\u0430\u0442\u044c \u043d\u0430 \u0434\u0430\u043d\u043d\u0443\u044e \u043b\u043e\u043a\u0430\u0446\u0438\u044e."
                    }
                },
                "required": [
                    "key",
                    "location"
                ],
                "type": "object",
                "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u0441 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c\u0438 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438."
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043b\u043e\u043a\u0430\u0446\u0438\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0432 \u0437\u0430\u043a\u0430\u0437\u0430\u0445 \u0438 \u0441\u043c\u0435\u043d\u0430\u0445."
        },
        "orders": {
            "items": {
                "additionalProperties": false,
                "nullable": true,
                "properties": {
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
                        "minItems": 0,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u0437\u043e\u0432 (\u043c\u043e\u0436\u0435\u0442 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u044c \u043e\u0434\u0438\u043d \u0433\u0440\u0443\u0437 \u0434\u043b\u044f `DROP`, \u0441\u043f\u0438\u0441\u043e\u043a \u0434\u043b\u044f `PICKUP`, \u043f\u0443\u0441\u0442\u043e\u0439 \u0434\u043b\u044f `WORK`)."
                    },
                    "demands": {
                        "items": {
                            "additionalProperties": false,
                            "nullable": true,
                            "properties": {
                                "demand_type": {
                                    "enum": [
                                        "PICKUP",
                                        "DROP",
                                        "WORK"
                                    ],
                                    "nullable": false,
                                    "type": "string",
                                    "x-description-ru": "\u0422\u0438\u043f \u0437\u0430\u044f\u0432\u043a\u0438 - \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 (`PICKUP`), \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0430 (`DROP`), \u0440\u0430\u0431\u043e\u0442\u0430 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 (`WORK`)."
                                },
                                "key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u044f\u0432\u043a\u0438, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                                },
                                "possible_events": {
                                    "items": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "duration": {
                                                "default": 0,
                                                "format": "int32",
                                                "maximum": 43800,
                                                "minimum": 0,
                                                "type": "integer",
                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438 \u0432 \u043c\u0438\u043d\u0443\u0442\u0430\u0445."
                                            },
                                            "location_key": {
                                                "maxLength": 1024,
                                                "minLength": 1,
                                                "type": "string",
                                                "x-description-ru": "\u041a\u043b\u044e\u0447 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0434\u0430\u043d\u043d\u043e\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u0435."
                                            },
                                            "reward": {
                                                "default": 1000,
                                                "format": "double",
                                                "maximum": 1000000,
                                                "minimum": 0,
                                                "type": "number",
                                                "x-description-ru": "\u0412\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0436\u0434\u0435\u043d\u0438\u0435 \u0437\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430."
                                            },
                                            "soft_time_window": {
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
                                            "location_key",
                                            "time_window"
                                        ],
                                        "type": "object",
                                        "x-description-ru": "\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u0435.  \u041e\u0431\u044a\u0435\u0434\u0438\u043d\u044f\u0435\u0442 \u0433\u0435\u043e\u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u043b\u043e\u043a\u0430\u0446\u0438\u044e \u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438.\n"
                                    },
                                    "maxItems": 10,
                                    "minItems": 1,
                                    "type": "array",
                                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u043e\u043a\u043e\u043d \u0438 \u043a\u043b\u044e\u0447\u0435\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0439, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u044f\u0432\u043a\u0438."
                                },
                                "precedence_in_order": {
                                    "default": 0,
                                    "format": "int32",
                                    "maximum": 9000,
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u041f\u0435\u0440\u0432\u0435\u043d\u0441\u0442\u0432\u043e \u0432\u043d\u0443\u0442\u0440\u0438 \u0437\u0430\u043a\u0430\u0437\u0430, 0 - \u043f\u0435\u0440\u0432\u0435\u043d\u0441\u0442\u0432\u043e \u043d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f."
                                },
                                "precedence_in_trip": {
                                    "default": 0,
                                    "format": "int32",
                                    "maximum": 9000,
                                    "minimum": 0,
                                    "type": "integer",
                                    "x-description-ru": "\u041f\u0435\u0440\u0432\u0435\u043d\u0441\u0442\u0432\u043e \u0432\u043d\u0443\u0442\u0440\u0438 \u0440\u0435\u0439\u0441\u0430, 0 - \u043f\u0435\u0440\u0432\u0435\u043d\u0441\u0442\u0432\u043e \u043d\u0435 \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u0442\u0441\u044f."
                                },
                                "target_cargos": {
                                    "items": {
                                        "maxLength": 1024,
                                        "minLength": 1,
                                        "type": "string",
                                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0433\u0440\u0443\u0437\u0430."
                                    },
                                    "maxItems": 1000,
                                    "minItems": 0,
                                    "type": "array",
                                    "uniqueItems": true,
                                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u044e\u0447\u0435\u0439 \u0433\u0440\u0443\u0437\u043e\u0432 \u0434\u043b\u044f `PICKUP`, \u043e\u0434\u0438\u043d \u043a\u043b\u044e\u0447 \u0433\u0440\u0443\u0437\u0430 \u0434\u043b\u044f `DROP`, \u043f\u0443\u0441\u0442\u043e\u0439 \u043a\u043b\u044e\u0447 \u0434\u043b\u044f `WORK`."
                                }
                            },
                            "required": [
                                "key",
                                "demand_type",
                                "possible_events"
                            ],
                            "type": "object",
                            "x-description-ru": "\u0417\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u043e\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u0441 \u0433\u0440\u0443\u0437\u043e\u043c (\u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 / \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0430) \u0438\u043b\u0438 \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
                        },
                        "maxItems": 1000,
                        "minItems": 1,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u044f\u0432\u043e\u043a."
                    },
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u043a\u0430\u0437\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                    },
                    "order_features": {
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u041e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0435\u0439 \u0437\u0430\u043a\u0430\u0437\u0430."
                    },
                    "order_restrictions": {
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043a \u0437\u0430\u043a\u0430\u0437\u0443."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0437\u0430\u043a\u0430\u0437\u0443, \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u043c\u043e\u043c\u0443 \u0432 \u044d\u0442\u043e\u043c \u0436\u0435 \u0440\u0435\u0439\u0441\u0435."
                    },
                    "performer_blacklist": {
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
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u043d\u044b\u0445 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e \u0440\u0430\u0431\u043e\u0442\u044b. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0434\u0430\u043d\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u0435 \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0443 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f\u043c\u0438. \u0414\u0430\u043d\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043d\u0435 \u0434\u043e\u043b\u0436\u0435\u043d \u043f\u0435\u0440\u0435\u0441\u0435\u043a\u0430\u0442\u044c\u0441\u044f \u0441 `performer_restrictions`.\n"
                    },
                    "performer_restrictions": {
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
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e \u0440\u0430\u0431\u043e\u0442\u044b. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0434\u0430\u043d\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u0435 \u043f\u043e \u0441\u043f\u0438\u0441\u043a\u0443 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f.\n"
                    }
                },
                "required": [
                    "key",
                    "demands"
                ],
                "type": "object",
                "x-description-ru": "\u0417\u0430\u043a\u0430\u0437 \u043d\u0430 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0433\u0440\u0443\u0437\u0430, \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u0441\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u044f\u0432\u043e\u043a."
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
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                    },
                    "max_work_shifts": {
                        "default": 31,
                        "format": "int32",
                        "maximum": 31,
                        "minimum": 1,
                        "type": "integer",
                        "x-description-ru": "\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430 \u0441\u043c\u0435\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0432 \u043e\u0434\u043d\u043e\u043c \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0438."
                    },
                    "own_transport_type": {
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
                    "performer_features": {
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
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0441 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438 \u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u043c."
                    },
                    "transport_restrictions": {
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0445 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0443. \u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430 \u0441 \u0437\u0430\u043a\u0430\u0437\u043e\u043c.\n"
                    }
                },
                "required": [
                    "key"
                ],
                "type": "object",
                "x-description-ru": "\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c, \u0441\u043f\u043e\u0441\u043e\u0431\u0435\u043d \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0430\u0442\u044c \u0433\u0440\u0443\u0437\u044b \u043d\u0430 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0435."
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0445 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439."
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
                    "finish_location_key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u0435\u0441\u043b\u0438 \u043d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0430 \u0442\u043e \u0440\u0435\u0439\u0441 \u0437\u0430\u0432\u0435\u0440\u0448\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u043c \u0437\u0430\u043a\u0430\u0437\u0435."
                    },
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0441\u043c\u0435\u043d\u044b, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                    },
                    "resource_key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0440\u0435\u0441\u0443\u0440\u0441\u0430, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0441\u0441\u044b\u043b\u0430\u0435\u0442\u0441\u044f \u0441\u043c\u0435\u043d\u0430."
                    },
                    "shift_type": {
                        "enum": [
                            "PERFORMER",
                            "TRANSPORT"
                        ],
                        "nullable": false,
                        "type": "string",
                        "x-description-ru": "\u0422\u0438\u043f \u0441\u043c\u0435\u043d\u044b, \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043c (PERFORMER) \u0438\u043b\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043e\u043c (TRANSPORT)."
                    },
                    "start_location_key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0439 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u0435\u0441\u043b\u0438 \u043d\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0430 \u0442\u043e \u0440\u0435\u0439\u0441 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u043d\u0430 \u043f\u0435\u0440\u0432\u043e\u043c \u0437\u0430\u043a\u0430\u0437\u0435."
                    },
                    "tariff": {
                        "additionalProperties": false,
                        "properties": {
                            "constraints": {
                                "items": {
                                    "additionalProperties": false,
                                    "properties": {
                                        "cost_per_unit": {
                                            "default": 0,
                                            "format": "double",
                                            "maximum": 10000,
                                            "minimum": 0,
                                            "type": "number",
                                            "x-description-ru": "\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u043e\u043f\u043b\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430. \u0414\u043b\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f - \u0434\u0435\u043d\u0435\u0436\u043d\u0430\u044f \u0435\u0434\u0438\u043d\u0438\u0446\u0430 \u0432 \u043c\u0438\u043d\u0443\u0442\u0443 \u0440\u0430\u0431\u043e\u0442\u044b. \u0414\u043b\u044f \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430 - \u0434\u0435\u043d\u0435\u0436\u043d\u0430\u044f \u0435\u0434\u0438\u043d\u0438\u0446\u0430 \u0437\u0430 \u043c\u0435\u0442\u0440 \u043f\u0443\u0442\u0438.\n"
                                        },
                                        "stage_length": {
                                            "default": 100000000,
                                            "format": "int32",
                                            "maximum": 100000000,
                                            "minimum": 1,
                                            "type": "integer",
                                            "x-description-ru": "\u0414\u043b\u0438\u043d\u0430 \u043e\u043f\u043b\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430, \u043c\u0438\u043d\u0443\u0442\u0430 \u0434\u043b\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f, \u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                        }
                                    },
                                    "required": [
                                        "stage_length",
                                        "cost_per_unit"
                                    ],
                                    "type": "object",
                                    "x-description-ru": "\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0442\u0430\u0440\u0438\u0444\u0430 - \u043e\u043f\u043b\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u044b\u0439 \u043f\u0435\u0440\u0438\u043e\u0434."
                                },
                                "maxItems": 100,
                                "minItems": 1,
                                "type": "array",
                                "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439 \u0442\u0430\u0440\u0438\u0444\u0430."
                            },
                            "cost_per_shift": {
                                "default": 0,
                                "format": "double",
                                "maximum": 100000,
                                "minimum": 0,
                                "type": "number",
                                "x-description-ru": "\u0426\u0435\u043d\u0430 \u0437\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043c\u0435\u043d\u044b, \u0434\u0435\u043d\u0435\u0436\u043d\u0430\u044f \u0435\u0434\u0438\u043d\u0438\u0446\u0430."
                            }
                        },
                        "required": [
                            "cost_per_shift",
                            "constraints"
                        ],
                        "type": "object",
                        "x-description-ru": "\u0422\u0430\u0440\u0438\u0444, \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f \u0441\u043c\u0435\u043d\u044b."
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
                    "key",
                    "shift_type",
                    "resource_key",
                    "availability_time",
                    "working_time"
                ],
                "type": "object",
                "x-description-ru": "\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u0441\u043c\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0438\u043b\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0441\u0443\u0440\u0441\u0430 \u0434\u043b\u044f \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432\u043d\u0443\u0442\u0440\u0438 \u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u0438.\n  * `availability_time` - \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u0441\u043c\u0435\u043d\u044b, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u0438\u043b\u0438 \u0442\u0440\u0430\u0441\u043f\u043e\u0440\u0442 \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445 \u0438 \u043e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c\u0438.\n  * `working_time` - \u0440\u0430\u0431\u043e\u0447\u0435\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043e\u043a\u043d\u043e, \u0432 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u0438\u043b\u0438 \u0442\u0440\u0430\u0441\u043f\u043e\u0440\u0442 \u043c\u043e\u0436\u0435\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u0445, \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0441\u043c\u0435\u043d\u044b.\n"
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0431\u043e\u0447\u0438\u0445 \u0441\u043c\u0435\u043d \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u0439 \u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
        },
        "transports": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "boxes": {
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
                        "maxItems": 100,
                        "minItems": 1,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0441\u0435\u043a\u043e\u0432 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043c\u043e\u0433\u0443\u0442 \u0432\u043c\u0435\u0449\u0430\u0442\u044c \u0433\u0440\u0443\u0437."
                    },
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u041a\u043b\u044e\u0447 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430, \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440."
                    },
                    "performer_restrictions": {
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
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0439 \u043a \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044e, \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u044e\u0449\u0438\u0439 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f\u043c\u0438."
                    },
                    "transport_features": {
                        "items": {
                            "maxLength": 256,
                            "minLength": 1,
                            "type": "string",
                            "x-description-ru": "\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                        },
                        "maxItems": 1000,
                        "minItems": 0,
                        "type": "array",
                        "uniqueItems": true,
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430 \u0441 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438, \u043b\u043e\u043a\u0430\u0446\u0438\u044f\u043c\u0438 \u0438 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f\u043c\u0438."
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
                    "key"
                ],
                "type": "object",
                "x-description-ru": "\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442"
            },
            "maxItems": 9000,
            "minItems": 1,
            "type": "array",
            "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0433\u043e \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
        },
        "trips": {
            "items": {
                "additionalProperties": false,
                "properties": {
                    "actions": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "cargo_placements": {
                                    "items": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "box_key": {
                                                "maxLength": 1024,
                                                "minLength": 1,
                                                "type": "string",
                                                "x-description-ru": "\u041a\u043b\u044e\u0447 \u043e\u0442\u0441\u0435\u043a\u0430."
                                            },
                                            "cargo_key": {
                                                "maxLength": 1024,
                                                "minLength": 1,
                                                "type": "string",
                                                "x-description-ru": "\u041a\u043b\u044e\u0447 \u0433\u0440\u0443\u0437\u0430."
                                            }
                                        },
                                        "required": [
                                            "box_key",
                                            "cargo_key"
                                        ],
                                        "type": "object",
                                        "x-description-ru": "\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0434\u043d\u043e\u0433\u043e \u0433\u0440\u0443\u0437\u0430 \u0432 \u043e\u0442\u0441\u0435\u043a\u0435."
                                    },
                                    "maxItems": 1000,
                                    "minItems": 0,
                                    "type": "array",
                                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0439 \u0433\u0440\u0443\u0437\u043e\u0432."
                                },
                                "demand_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u044f\u0432\u043a\u0438, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435."
                                },
                                "location_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u043b\u043e\u043a\u0430\u0446\u0438\u0438, \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435."
                                },
                                "order_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0437\u0430\u043a\u0430\u0437\u0430, \u0441 \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435."
                                },
                                "todolist": {
                                    "items": {
                                        "additionalProperties": false,
                                        "properties": {
                                            "job_time": {
                                                "format": "date-time",
                                                "type": "string",
                                                "x-description-ru": "\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u0432 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u0438 \u0441 [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)."
                                            },
                                            "job_type": {
                                                "enum": [
                                                    "LOCATION_ARRIVAL",
                                                    "READY_TO_WORK",
                                                    "START_WORK",
                                                    "FINISH_WORK",
                                                    "LOCATION_DEPARTURE"
                                                ],
                                                "nullable": false,
                                                "type": "string",
                                                "x-description-ru": "\u0412\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0435 \u0442\u0438\u043f\u044b \u0440\u0430\u0431\u043e\u0442:\n  * `LOCATION_ARRIVAL` - \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u0435 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u044e (\u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043a\u043e\u0432\u043a\u0438, \u043d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u044b)\n  * `READY_TO_WORK` - \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c \u0433\u043e\u0442\u043e\u0432 \u043a \u0440\u0430\u0431\u043e\u0442\u0435 (\u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u044b, \u043d\u0430\u0447\u0430\u043b\u043e \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0438 \u043d\u0430\u0447\u0430\u043b\u0430 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0438)\n  * `START_WORK` - \u043d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 (\u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f \u043b\u043e\u043a\u0430\u0446\u0438\u0438 \u0438 \u043d\u0430\u0447\u0430\u043b\u0430 \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 \u0437\u0430\u044f\u0432\u043a\u0438, \u043d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b)\n  * `FINISH_WORK` - \u043a\u043e\u043d\u0435\u0446 \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438 (\u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u044b, \u043d\u0430\u0447\u0430\u043b\u043e \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u044f \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u043e\u0442\u044a\u0435\u0437\u0434\u0430 \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0443\u044e \u043b\u043e\u043a\u0430\u0446\u0438\u044e)\n  * `LOCATION_DEPARTURE` - \u043e\u0442\u044a\u0435\u0437\u0434 \u0441 \u043b\u043e\u043a\u0430\u0446\u0438\u0438\n"
                                            }
                                        },
                                        "required": [
                                            "job_type",
                                            "job_time"
                                        ],
                                        "type": "object",
                                        "x-description-ru": "\u0420\u0430\u0431\u043e\u0442\u0430 \u043d\u0430 \u043b\u043e\u043a\u0430\u0446\u0438\u0438."
                                    },
                                    "maxItems": 1000,
                                    "minItems": 1,
                                    "type": "array",
                                    "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0431\u043e\u0442, \u043a\u0430\u0436\u0434\u0430\u044f \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u0432\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u043c \u043e\u043a\u043d\u0435 job_time."
                                }
                            },
                            "required": [
                                "order_key",
                                "demand_key",
                                "location_key",
                                "todolist"
                            ],
                            "type": "object",
                            "x-description-ru": "\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043d\u0430\u0434 \u0437\u0430\u043a\u0430\u0437\u043e\u043c."
                        },
                        "maxItems": 1000,
                        "minItems": 1,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u043d\u0430\u0434 \u0437\u0430\u043a\u0430\u0437\u0430\u043c\u0438."
                    },
                    "assigned_shifts": {
                        "items": {
                            "additionalProperties": false,
                            "properties": {
                                "shift_key": {
                                    "maxLength": 1024,
                                    "minLength": 1,
                                    "type": "string",
                                    "x-description-ru": "\u041a\u043b\u044e\u0447 \u0441\u043c\u0435\u043d\u044b \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0438\u043b\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430."
                                },
                                "shift_time": {
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
                                "shift_key",
                                "shift_time"
                            ],
                            "type": "object",
                            "x-description-ru": "\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u0430\u044f \u0441\u043c\u0435\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u0438\u043b\u0438 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0430 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f (shift_time)."
                        },
                        "maxItems": 2,
                        "minItems": 2,
                        "type": "array",
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0445 \u0441\u043c\u0435\u043d."
                    },
                    "key": {
                        "maxLength": 1024,
                        "minLength": 1,
                        "type": "string",
                        "x-description-ru": "\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0435\u0439\u0441\u0430."
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
                        "x-description-ru": "\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u044e\u0447\u0435\u0439 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0445, \u043d\u043e \u043d\u0435 \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u043d\u0430 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u043a\u0430\u0437\u043e\u0432."
                    }
                },
                "required": [
                    "key",
                    "assigned_shifts"
                ],
                "type": "object",
                "x-description-ru": "\u0420\u0435\u0439\u0441 - \u044d\u0442\u043e \u0441\u043e\u0432\u043e\u043a\u0443\u043f\u043d\u043e\u0441\u0442\u044c \u0440\u0430\u0431\u043e\u0442 (`actions`) \u0437\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u043c \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043c \u043d\u0430 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u043c \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u0435.\n"
            },
            "maxItems": 9000,
            "minItems": 0,
            "type": "array",
            "x-description-ru": "\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0440\u0435\u0439\u0441\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0435\u0440\u0435\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c."
        }
    },
    "required": [
        "locations",
        "orders",
        "performers",
        "transports",
        "shifts"
    ],
    "type": "object",
    "x-description-ru": "\u0417\u0430\u0434\u0430\u0447\u0430 \u0434\u043b\u044f \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f."
}'''
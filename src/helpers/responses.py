def not_found(detail: str):
    return {
            'description': 'Returned when user not found',
            'content': {
                'application/json': {
                    'example': {
                        'detail': detail
                        }
                    }
                }
            }
ADMIN_REORDER = (
    {
        'app': 'auth',
        'label': 'Users',
        'models': [
            {'model': 'auth.User', 'label': 'Users'}
            {'model': 'myapp.MyModel', 'label': 'My Custom Model'}
        ]
    }, {
        'app': 'myapp',
        'label': 'My other section',
        'models': [
            {'model': 'myapp.MyOtherModel', 'label': 'My Other Model'}
        ]
    }
)

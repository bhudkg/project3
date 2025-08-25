DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # The URI connection string
        'NAME': 'file:/path/to/your/database.db?mode=ro', 
        'OPTIONS': {
            # This tells Django to interpret NAME as a URI
            'uri': True, 
        }
    }
}
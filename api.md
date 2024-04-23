# Authentication

Types:

```python
from prelude.types import AuthenticationCreateResponse
```

Methods:

- <code title="post /authentication">client.authentication.<a href="./src/prelude/resources/authentication/authentication.py">create</a>(\*\*<a href="src/prelude/types/authentication_create_params.py">params</a>) -> <a href="./src/prelude/types/authentication_create_response.py">AuthenticationCreateResponse</a></code>

## Feedback

Types:

```python
from prelude.types.authentication import FeedbackCreateResponse
```

Methods:

- <code title="post /authentication/feedback">client.authentication.feedback.<a href="./src/prelude/resources/authentication/feedback.py">create</a>(\*\*<a href="src/prelude/types/authentication/feedback_create_params.py">params</a>) -> <a href="./src/prelude/types/authentication/feedback_create_response.py">FeedbackCreateResponse</a></code>

# Check

Types:

```python
from prelude.types import CheckCreateResponse
```

Methods:

- <code title="post /check">client.check.<a href="./src/prelude/resources/check.py">create</a>(\*\*<a href="src/prelude/types/check_create_params.py">params</a>) -> <a href="./src/prelude/types/check_create_response.py">CheckCreateResponse</a></code>

# Retry

Types:

```python
from prelude.types import RetryCreateResponse
```

Methods:

- <code title="post /retry">client.retry.<a href="./src/prelude/resources/retry.py">create</a>(\*\*<a href="src/prelude/types/retry_create_params.py">params</a>) -> <a href="./src/prelude/types/retry_create_response.py">RetryCreateResponse</a></code>

# Lookup

Types:

```python
from prelude.types import LookupRetrieveResponse
```

Methods:

- <code title="get /lookup/{phone_number}">client.lookup.<a href="./src/prelude/resources/lookup.py">retrieve</a>(phone_number) -> <a href="./src/prelude/types/lookup_retrieve_response.py">LookupRetrieveResponse</a></code>

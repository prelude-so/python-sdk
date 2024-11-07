# Verification

Types:

```python
from prelude_sdk.types import VerificationCreateResponse, VerificationCheckResponse
```

Methods:

- <code title="post /v2/verification">client.verification.<a href="./src/prelude_sdk/resources/verification.py">create</a>(\*\*<a href="src/prelude_sdk/types/verification_create_params.py">params</a>) -> <a href="./src/prelude_sdk/types/verification_create_response.py">VerificationCreateResponse</a></code>
- <code title="post /v2/verification/check">client.verification.<a href="./src/prelude_sdk/resources/verification.py">check</a>(\*\*<a href="src/prelude_sdk/types/verification_check_params.py">params</a>) -> <a href="./src/prelude_sdk/types/verification_check_response.py">VerificationCheckResponse</a></code>

# Transactional

Types:

```python
from prelude_sdk.types import TransactionalSendResponse
```

Methods:

- <code title="post /v2/transactional">client.transactional.<a href="./src/prelude_sdk/resources/transactional.py">send</a>(\*\*<a href="src/prelude_sdk/types/transactional_send_params.py">params</a>) -> <a href="./src/prelude_sdk/types/transactional_send_response.py">TransactionalSendResponse</a></code>

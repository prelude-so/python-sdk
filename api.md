# Transactional

Types:

```python
from prelude_python_sdk.types import TransactionalSendResponse
```

Methods:

- <code title="post /v2/transactional">client.transactional.<a href="./src/prelude_python_sdk/resources/transactional.py">send</a>(\*\*<a href="src/prelude_python_sdk/types/transactional_send_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/transactional_send_response.py">TransactionalSendResponse</a></code>

# Verification

Types:

```python
from prelude_python_sdk.types import VerificationCreateResponse, VerificationCheckResponse
```

Methods:

- <code title="post /v2/verification">client.verification.<a href="./src/prelude_python_sdk/resources/verification.py">create</a>(\*\*<a href="src/prelude_python_sdk/types/verification_create_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/verification_create_response.py">VerificationCreateResponse</a></code>
- <code title="post /v2/verification/check">client.verification.<a href="./src/prelude_python_sdk/resources/verification.py">check</a>(\*\*<a href="src/prelude_python_sdk/types/verification_check_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/verification_check_response.py">VerificationCheckResponse</a></code>

# Watch

Types:

```python
from prelude_python_sdk.types import WatchFeedBackResponse, WatchPredictResponse
```

Methods:

- <code title="post /v2/watch/feedback">client.watch.<a href="./src/prelude_python_sdk/resources/watch.py">feed_back</a>(\*\*<a href="src/prelude_python_sdk/types/watch_feed_back_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/watch_feed_back_response.py">WatchFeedBackResponse</a></code>
- <code title="post /v2/watch/predict">client.watch.<a href="./src/prelude_python_sdk/resources/watch.py">predict</a>(\*\*<a href="src/prelude_python_sdk/types/watch_predict_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/watch_predict_response.py">WatchPredictResponse</a></code>

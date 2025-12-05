# Lookup

Types:

```python
from prelude_python_sdk.types import LookupLookupResponse
```

Methods:

- <code title="get /v2/lookup/{phone_number}">client.lookup.<a href="./src/prelude_python_sdk/resources/lookup.py">lookup</a>(phone_number, \*\*<a href="src/prelude_python_sdk/types/lookup_lookup_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/lookup_lookup_response.py">LookupLookupResponse</a></code>

# Notify

Types:

```python
from prelude_python_sdk.types import (
    NotifyGetSubscriptionConfigResponse,
    NotifyGetSubscriptionPhoneNumberResponse,
    NotifyListSubscriptionConfigsResponse,
    NotifyListSubscriptionPhoneNumberEventsResponse,
    NotifyListSubscriptionPhoneNumbersResponse,
    NotifySendResponse,
    NotifySendBatchResponse,
)
```

Methods:

- <code title="get /v2/notify/management/subscriptions/{config_id}">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">get_subscription_config</a>(config_id) -> <a href="./src/prelude_python_sdk/types/notify_get_subscription_config_response.py">NotifyGetSubscriptionConfigResponse</a></code>
- <code title="get /v2/notify/management/subscriptions/{config_id}/phone_numbers/{phone_number}">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">get_subscription_phone_number</a>(phone_number, \*, config_id) -> <a href="./src/prelude_python_sdk/types/notify_get_subscription_phone_number_response.py">NotifyGetSubscriptionPhoneNumberResponse</a></code>
- <code title="get /v2/notify/management/subscriptions">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">list_subscription_configs</a>(\*\*<a href="src/prelude_python_sdk/types/notify_list_subscription_configs_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/notify_list_subscription_configs_response.py">NotifyListSubscriptionConfigsResponse</a></code>
- <code title="get /v2/notify/management/subscriptions/{config_id}/phone_numbers/{phone_number}/events">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">list_subscription_phone_number_events</a>(phone_number, \*, config_id, \*\*<a href="src/prelude_python_sdk/types/notify_list_subscription_phone_number_events_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/notify_list_subscription_phone_number_events_response.py">NotifyListSubscriptionPhoneNumberEventsResponse</a></code>
- <code title="get /v2/notify/management/subscriptions/{config_id}/phone_numbers">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">list_subscription_phone_numbers</a>(config_id, \*\*<a href="src/prelude_python_sdk/types/notify_list_subscription_phone_numbers_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/notify_list_subscription_phone_numbers_response.py">NotifyListSubscriptionPhoneNumbersResponse</a></code>
- <code title="post /v2/notify">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">send</a>(\*\*<a href="src/prelude_python_sdk/types/notify_send_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/notify_send_response.py">NotifySendResponse</a></code>
- <code title="post /v2/notify/batch">client.notify.<a href="./src/prelude_python_sdk/resources/notify.py">send_batch</a>(\*\*<a href="src/prelude_python_sdk/types/notify_send_batch_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/notify_send_batch_response.py">NotifySendBatchResponse</a></code>

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

# VerificationManagement

Types:

```python
from prelude_python_sdk.types import (
    VerificationManagementDeletePhoneNumberResponse,
    VerificationManagementListPhoneNumbersResponse,
    VerificationManagementListSenderIDsResponse,
    VerificationManagementSetPhoneNumberResponse,
    VerificationManagementSubmitSenderIDResponse,
)
```

Methods:

- <code title="delete /v2/verification/management/phone-numbers/{action}">client.verification_management.<a href="./src/prelude_python_sdk/resources/verification_management.py">delete_phone_number</a>(action, \*\*<a href="src/prelude_python_sdk/types/verification_management_delete_phone_number_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/verification_management_delete_phone_number_response.py">VerificationManagementDeletePhoneNumberResponse</a></code>
- <code title="get /v2/verification/management/phone-numbers/{action}">client.verification_management.<a href="./src/prelude_python_sdk/resources/verification_management.py">list_phone_numbers</a>(action) -> <a href="./src/prelude_python_sdk/types/verification_management_list_phone_numbers_response.py">VerificationManagementListPhoneNumbersResponse</a></code>
- <code title="get /v2/verification/management/sender-id">client.verification_management.<a href="./src/prelude_python_sdk/resources/verification_management.py">list_sender_ids</a>() -> <a href="./src/prelude_python_sdk/types/verification_management_list_sender_ids_response.py">VerificationManagementListSenderIDsResponse</a></code>
- <code title="post /v2/verification/management/phone-numbers/{action}">client.verification_management.<a href="./src/prelude_python_sdk/resources/verification_management.py">set_phone_number</a>(action, \*\*<a href="src/prelude_python_sdk/types/verification_management_set_phone_number_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/verification_management_set_phone_number_response.py">VerificationManagementSetPhoneNumberResponse</a></code>
- <code title="post /v2/verification/management/sender-id">client.verification_management.<a href="./src/prelude_python_sdk/resources/verification_management.py">submit_sender_id</a>(\*\*<a href="src/prelude_python_sdk/types/verification_management_submit_sender_id_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/verification_management_submit_sender_id_response.py">VerificationManagementSubmitSenderIDResponse</a></code>

# Watch

Types:

```python
from prelude_python_sdk.types import (
    WatchPredictResponse,
    WatchSendEventsResponse,
    WatchSendFeedbacksResponse,
)
```

Methods:

- <code title="post /v2/watch/predict">client.watch.<a href="./src/prelude_python_sdk/resources/watch.py">predict</a>(\*\*<a href="src/prelude_python_sdk/types/watch_predict_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/watch_predict_response.py">WatchPredictResponse</a></code>
- <code title="post /v2/watch/event">client.watch.<a href="./src/prelude_python_sdk/resources/watch.py">send_events</a>(\*\*<a href="src/prelude_python_sdk/types/watch_send_events_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/watch_send_events_response.py">WatchSendEventsResponse</a></code>
- <code title="post /v2/watch/feedback">client.watch.<a href="./src/prelude_python_sdk/resources/watch.py">send_feedbacks</a>(\*\*<a href="src/prelude_python_sdk/types/watch_send_feedbacks_params.py">params</a>) -> <a href="./src/prelude_python_sdk/types/watch_send_feedbacks_response.py">WatchSendFeedbacksResponse</a></code>

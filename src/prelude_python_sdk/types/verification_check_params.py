# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCheckParams", "Target", "Psd2"]


class VerificationCheckParams(TypedDict, total=False):
    code: Required[str]
    """The OTP code to validate."""

    target: Required[Target]
    """The verification target.

    Either a phone number or an email address. To use the email verification feature
    contact us to discuss your use case.
    """

    psd2: Psd2
    """Required when checking a code issued under the `prelude:psd2` template.

    The submitted variables must match those provided at issuance; any mismatch
    invalidates the code (PSD2 SCA RTS Article 5 dynamic linking). Ignored on
    non-PSD2 verifications.
    """


class Target(TypedDict, total=False):
    """The verification target.

    Either a phone number or an email address. To use the email verification feature contact us to discuss your use case.
    """

    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class Psd2(TypedDict, total=False):
    """Required when checking a code issued under the `prelude:psd2` template.

    The submitted variables must match those provided at issuance; any mismatch invalidates the code (PSD2 SCA RTS Article 5 dynamic linking). Ignored on non-PSD2 verifications.
    """

    amount: Required[str]
    """Decimal amount of the transaction."""

    currency: Required[str]
    """ISO 4217 currency code."""

    recipient: Required[str]
    """Payee name displayed to the payer."""

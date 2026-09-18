# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WatchEvaluateResponse", "Recipe", "RecipeRule"]


class RecipeRule(BaseModel):
    outcome: Literal["TRIGGERED", "NOT_TRIGGERED", "NOT_EVALUATED"]
    """What the rule concluded.

    - `TRIGGERED` - The condition held; `weight` was added to the score.
    - `NOT_TRIGGERED` - The condition did not hold.
    - `NOT_EVALUATED` - The rule could not run, because something it reads never
      arrived. This is not a quieter `NOT_TRIGGERED`: it contributed nothing either
      way, and it is why `partial_evidence` is set on the recipe.
    """

    rule_id: str
    """The rule that produced this result.

    Present whatever the rule's visibility, so a rule you cannot see the condition
    of is still one you can reweight, switch off, or ask us about.
    """

    weight: int
    """What this rule contributes to the recipe's score when it triggers."""

    blocked_by: Optional[str] = None
    """Why the rule could not run, set only when `outcome` is `NOT_EVALUATED`.

    A rule you authored names the signal or attribute it waited on, since you wrote
    the expression that reads it. A Prelude-managed rule reports `missing_data` and
    nothing more: the signal it waited on is part of a condition that is not
    disclosed.
    """

    name: Optional[str] = None
    """
    The rule's name, present for a rule you authored and omitted for a
    Prelude-managed one. A managed rule's name describes what it looks for, which is
    as much of the condition as the expression is.
    """

    unavailable: Optional[bool] = None
    """
    The rule could not run for a reason on our side rather than anything about your
    request. `outcome` is `NOT_EVALUATED` and the failure is ours to fix.
    """


class Recipe(BaseModel):
    partial_evidence: bool
    """
    At least one rule could not be evaluated, so the score rests on less than the
    whole recipe. The score is still returned — a partial verdict is more useful
    than none — but it is labeled rather than passed off as whole.
    """

    recipe_id: str
    """The recipe that produced this result."""

    rules: List[RecipeRule]
    """One result per rule in the recipe, in membership order.

    Every rule runs — a score is only meaningful when complete, so there is no
    short-circuit on the first trigger.
    """

    score: int
    """
    The sum of the weights of the rules that triggered, clamped to the range -100
    to 100. Two scores at a bound are not comparable.
    """

    threshold: int
    """The score at or above which this recipe flags."""

    verdict: Literal["PASS", "FLAG"]
    """This recipe's own verdict.

    Normally the score against the threshold, unless a preempting rule fired — see
    `determined_by`.
    """

    determined_by: Optional[str] = None
    """
    The preempting rule that set `verdict`, present only when a rule rather than the
    score decided it. Without it a recipe can report a score under its threshold and
    still flag, with nothing in the payload accounting for the difference.
    """


class WatchEvaluateResponse(BaseModel):
    id: str
    """The evaluation identifier."""

    action: Literal["ALLOW", "BLOCK", "CHALLENGE"]
    """
    What the evaluation suggests you do, being the most severe action across the
    recipes that ran. Advisory: enforcement is yours.

    - `ALLOW` - Let the request through.
    - `BLOCK` - Refuse the request.
    - `CHALLENGE` - Let the request through behind an additional check.
    """

    recipes: List[Recipe]
    """One result per recipe that ran.

    A recipe the flow names but that is not in service is absent rather than
    reported as having passed.
    """

    verdict: Literal["PASS", "FLAG"]
    """
    The evaluation-level verdict, being the most severe verdict across the recipes
    that ran.

    - `PASS` - No recipe flagged.
    - `FLAG` - At least one recipe flagged.
    """

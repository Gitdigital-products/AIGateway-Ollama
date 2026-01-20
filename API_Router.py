from fastapi import APIRouter, Header, Request, status
from fastapi.responses import JSONResponse

from .settings import settings
from .security import verify_github_signature

router = APIRouter(prefix="/webhooks/github", tags=["github-webhooks"])


@router.post("/governance-policy-validator")
async def governance_policy_validator_webhook(
    request: Request,
    x_hub_signature_256: str | None = Header(default=None, alias="X-Hub-Signature-256"),
    x_github_event: str | None = Header(default=None, alias="X-GitHub-Event"),
    x_github_delivery: str | None = Header(default=None, alias="X-GitHub-Delivery"),
):
    raw_body = await request.body()

    # 1. Verify signature
    verify_github_signature(
        secret=settings.github_webhook_secret,
        body=raw_body,
        signature_header=x_hub_signature_256,
    )

    # 2. Parse JSON payload
    payload = await request.json()

    # 3. Route by event type
    if x_github_event == "push":
        await handle_push_event(payload)
    elif x_github_event == "pull_request":
        await handle_pull_request_event(payload)
    elif x_github_event == "workflow_run":
        await handle_workflow_run_event(payload)
    else:
        # Unknown/unhandled event types still return 2xx so GitHub doesn’t retry
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={"status": "ignored", "reason": f"event {x_github_event} not handled"},
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "delivery_id": x_github_delivery,
            "event": x_github_event,
        },
    )


async def handle_push_event(payload: dict):
    # TODO: extract changed governance policy files, run validator, emit results
    repo = payload.get("repository", {}).get("full_name")
    ref = payload.get("ref")
    # your governance policy validation logic here
    return


async def handle_pull_request_event(payload: dict):
    # TODO: validate policies touched in PR, comment on PR, update registry
    action = payload.get("action")
    pr = payload.get("pull_request", {})
    number = pr.get("number")
    # your governance policy validation logic here
    return


async def handle_workflow_run_event(payload: dict):
    # TODO: integrate with CI workflows, enforce compliance gates
    workflow = payload.get("workflow", {}).get("name")
    conclusion = payload.get("workflow_run", {}).get("conclusion")
    # your governance policy validation logic here
    return

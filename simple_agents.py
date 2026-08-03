"""A tiny example of multiple AI agents built with the OpenAI Agents SDK."""

from __future__ import annotations

import argparse
import os
from datetime import UTC, datetime


def add_numbers(first: float, second: float) -> float:
    """Add two numbers. Kept separate so it is easy to test."""

    return first + second


def current_utc_time() -> str:
    """Return the current UTC time in a readable format."""

    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def build_agent():
    """Create a small coordinator and its two specialist agents."""

    # Importing here lets the small utility functions be tested without an API SDK.
    from agents import Agent, function_tool

    @function_tool
    def add(first: float, second: float) -> float:
        """Add two numbers and return the result."""

        return add_numbers(first, second)

    @function_tool
    def get_utc_time() -> str:
        """Get the current date and time in UTC."""

        return current_utc_time()

    math_agent = Agent(
        name="Math helper",
        instructions="Help with very simple addition. Use the add tool.",
        tools=[add],
    )
    friendly_agent = Agent(
        name="Friendly helper",
        instructions=(
            "Answer simple greetings and time questions. For time questions, "
            "use the get_utc_time tool. Keep every answer short and friendly."
        ),
        tools=[get_utc_time],
    )
    return Agent(
        name="Simple coordinator",
        instructions=(
            "You coordinate two helpers. Hand addition questions to Math helper. "
            "Hand greetings and time questions to Friendly helper. Keep it simple."
        ),
        handoffs=[math_agent, friendly_agent],
    )


def main() -> None:
    """Run one prompt from the command line."""

    parser = argparse.ArgumentParser(description="Ask a very simple AI agent")
    parser.add_argument("prompt", nargs="+", help="question for the agent")
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        parser.error("set OPENAI_API_KEY before running this program")

    from agents import Runner

    result = Runner.run_sync(build_agent(), " ".join(args.prompt))
    print(result.final_output)


if __name__ == "__main__":
    main()

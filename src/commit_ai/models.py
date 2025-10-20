from pydantic import BaseModel, Field
from typing import Optional


class CommitMessage(BaseModel):
    # """Pydantic model for the LLM response"""

    type: str = Field(
        ...,
        description="Type of change (feat, fix, docs, style, refactor, test, chore)",
    )
    subject: str = Field(..., description="Short description of the change")
    body: Optional[str] = Field(
        None, description="Detailed explanation of the change (optional)"
    )

    def format(self) -> str:
        """Format to become a proper string for the TUI"""
        result = f"{self.type}: {self.subject}"
        if self.body:
            result += f"\n\n{self.body}"
        return result

from typing import List, Optional

from pydantic import BaseModel, Field


class RunRequest(BaseModel):
    url: str = Field("https://www.wjx.cn/vm/QHzdwQy.aspx", description="问卷 URL")
    times: int = Field(1, ge=1, le=50, description="填写次数")
    show_browser: bool = Field(False, description="是否显示浏览器界面")


class JobState(BaseModel):
    status: str
    logs: List[str]
    error: Optional[str] = None

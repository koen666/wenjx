import random
from typing import Dict
from urllib.parse import urlparse

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

from models.schemas import JobState

DEFAULT_URL = "https://www.wjx.cn/vm/QHzdwQy.aspx"


def _normalize_url(url: str) -> str:
    if not url:
        return DEFAULT_URL
    parsed = urlparse(url)
    if not parsed.scheme:
        return f"https://{url}"
    return url


async def _fill_single(page, q_ids, option_count: int):
    for qid in q_ids:
        anchors = await page.query_selector_all(f"div#div{qid} a.jqradio")
        if not anchors:
            raise RuntimeError(f"未找到单选题 {qid} 的选项")
        choice = random.choice(anchors[:option_count])
        await choice.scroll_into_view_if_needed()
        await choice.click()
        await page.wait_for_timeout(200)


async def _fill_multi(page, q_ids, option_count: int):
    for qid in q_ids:
        anchors = await page.query_selector_all(f"div#div{qid} a.jqcheck")
        if not anchors:
            raise RuntimeError(f"未找到多选题 {qid} 的选项")
        max_idx = min(option_count, len(anchors))
        options = list(range(max_idx))
        weights = [0.15, 0.15, 0.2, 0.3, 0.2][: len(options)]
        ans_num = random.choices(range(1, len(options) + 1), weights=weights, k=1)[0]
        picked = random.sample(options, k=ans_num)
        for idx in picked:
            anchor = anchors[idx]
            await anchor.scroll_into_view_if_needed()
            await anchor.click()
            await page.wait_for_timeout(120)
        await page.wait_for_timeout(200)


async def _fill_matrix(page, q_id: int):
    rows = await page.query_selector_all(f"#div{q_id} table tr[tp='d']")
    if not rows:
        raise RuntimeError(f"未找到矩阵题 {q_id} 的行")
    for row in rows:
        anchors = await row.query_selector_all("a.rate-off")
        if not anchors:
            raise RuntimeError(f"矩阵题 {q_id} 行缺少选项")
        choice = random.choice(anchors)
        await choice.scroll_into_view_if_needed()
        await choice.click()
        await page.wait_for_timeout(120)


async def _fill_form(page):
    single_5 = [1, 4]
    single_2 = [2, 3]
    multi_5 = [5, 6, 7, 8, 9]

    await _fill_single(page, single_5, 5)
    await _fill_single(page, single_2, 2)
    await _fill_multi(page, multi_5, 5)
    await _fill_matrix(page, 10)


async def _run_once(browser, target_url: str):
    page = await browser.new_page(
        viewport={"width": 430, "height": 720},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
    )
    try:
        await page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_selector("body", timeout=15000)
        await _fill_form(page)
        await page.click("div#ctlNext")
        await page.wait_for_timeout(800)
    finally:
        await page.close()


async def run_job(job_id: str, url: str, times: int, store: Dict[str, JobState], show_browser: bool = False):
    store[job_id] = JobState(status="running", logs=[], error=None)
    target = _normalize_url(url)
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=not show_browser, args=["--disable-dev-shm-usage"])
            for i in range(times):
                await _run_once(browser, target)
                store[job_id].logs.append(f"第 {i + 1} 份完成")
            await browser.close()
        store[job_id].status = "success"
    except PlaywrightTimeoutError as e:
        store[job_id].status = "error"
        store[job_id].error = f"超时: {e}"
    except Exception as e:  # noqa: BLE001
        store[job_id].status = "error"
        store[job_id].error = str(e)

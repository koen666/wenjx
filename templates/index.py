HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>问卷星填写助手</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', 'Microsoft YaHei', sans-serif; 
  background: linear-gradient(180deg, #f5f5f7 0%, #e8e8ed 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: #1d1d1f;
}
.container {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-radius: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
  max-width: 580px;
  width: 100%;
  overflow: hidden;
  border: 0.5px solid rgba(255, 255, 255, 0.3);
}
.header {
  padding: 48px 40px 32px;
  text-align: center;
}
.header h1 {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #1d1d1f;
  margin-bottom: 8px;
}
.header p {
  font-size: 15px;
  color: #6e6e73;
  font-weight: 400;
  line-height: 1.5;
}
.content {
  padding: 0 40px 40px;
}
.form-group {
  margin-bottom: 28px;
}
.form-group label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-weight: 590;
  color: #1d1d1f;
  margin-bottom: 10px;
  font-size: 15px;
  letter-spacing: -0.01em;
}
.form-group label .icon {
  font-size: 16px;
  color: #86868b;
}
.form-group input[type="text"],
.form-group input[type="number"] {
  width: 100%;
  padding: 13px 16px;
  border: none;
  background: rgba(0, 0, 0, 0.04);
  border-radius: 12px;
  font-size: 15px;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  color: #1d1d1f;
}
.form-group input::placeholder {
  color: #86868b;
}
.form-group input:focus {
  outline: none;
  background: rgba(0, 0, 0, 0.06);
  box-shadow: 0 0 0 4px rgba(0, 122, 255, 0.15);
}
.checkbox-group {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
  padding: 14px 16px;
  background: rgba(0, 0, 0, 0.02);
  border-radius: 12px;
}
.checkbox-group input[type="checkbox"] {
  width: 22px;
  height: 22px;
  cursor: pointer;
  accent-color: #007AFF;
  border-radius: 6px;
}
.checkbox-group label {
  font-size: 14px;
  color: #1d1d1f;
  cursor: pointer;
  user-select: none;
  font-weight: 400;
  line-height: 1.4;
}
.btn {
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 14px;
  font-size: 17px;
  font-weight: 590;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  letter-spacing: -0.01em;
}
.btn-primary {
  background: #007AFF;
  color: white;
  box-shadow: 0 2px 8px rgba(0, 122, 255, 0.25);
}
.btn-primary:hover:not(:disabled) {
  background: #0051D5;
  box-shadow: 0 4px 16px rgba(0, 122, 255, 0.35);
  transform: translateY(-1px);
}
.btn-primary:active:not(:disabled) {
  transform: scale(0.98);
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.status-box {
  margin-top: 28px;
  padding: 16px 18px;
  border-radius: 14px;
  background: rgba(0, 0, 0, 0.03);
  border: 1px solid rgba(0, 0, 0, 0.06);
}
.status-box .status-label {
  font-size: 11px;
  color: #86868b;
  font-weight: 590;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
}
.status-box .status-text {
  font-size: 15px;
  color: #1d1d1f;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 8px;
}
.progress-bar {
  margin-top: 12px;
  height: 4px;
  background: rgba(0, 0, 0, 0.08);
  border-radius: 2px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: #007AFF;
  border-radius: 2px;
  transition: width 0.3s ease;
  width: 0%;
}
.log-box {
  margin-top: 16px;
  background: rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 12px;
  padding: 14px 16px;
  font-family: 'SF Mono', 'Monaco', 'Menlo', monospace;
  font-size: 12px;
  max-height: 180px;
  overflow-y: auto;
  line-height: 1.7;
  white-space: pre-wrap;
  color: #1d1d1f;
}
.log-box::-webkit-scrollbar {
  width: 6px;
}
.log-box::-webkit-scrollbar-track {
  background: transparent;
}
.log-box::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 3px;
}
.log-box::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.25);
}
.footer {
  padding: 24px 40px 32px;
  text-align: center;
}
.footer-hint {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #86868b;
  background: rgba(0, 0, 0, 0.02);
  padding: 8px 14px;
  border-radius: 8px;
  font-weight: 400;
}
.footer-hint code {
  background: rgba(0, 0, 0, 0.06);
  padding: 3px 8px;
  border-radius: 6px;
  font-family: 'SF Mono', 'Monaco', monospace;
  font-size: 11px;
  color: #1d1d1f;
}
.status-running .status-text { color: #007AFF; }
.status-success .status-text { color: #34C759; }
.status-error .status-text { color: #FF3B30; }
.status-error .status-box {
  background: rgba(255, 59, 48, 0.06);
  border-color: rgba(255, 59, 48, 0.15);
}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>问卷星填写助手</h1>
    <p>智能化的问卷批量填写解决方案</p>
  </div>
  <div class="content">
    <div class="form-group">
      <label><span class="icon">🔗</span>问卷链接</label>
      <input type="text" id="url" placeholder="https://www.wjx.cn/vm/..." value="https://www.wjx.cn/vm/QHzdwQy.aspx">
    </div>
    <div class="form-group">
      <label><span class="icon">🔢</span>填写份数</label>
      <input type="number" id="times" min="1" max="50" value="3" placeholder="输入 1-50">
    </div>
    <div class="checkbox-group">
      <input type="checkbox" id="showBrowser">
      <label for="showBrowser">显示浏览器界面（便于调试和查看填写过程）</label>
    </div>
    <button class="btn btn-primary" id="startBtn">开始填写</button>
    <div class="status-box" id="statusBox" style="display:none;">
      <div class="status-label">状态</div>
      <div class="status-text" id="statusText">准备中</div>
      <div class="progress-bar" id="progressBar" style="display:none;">
        <div class="progress-fill" id="progressFill"></div>
      </div>
    </div>
    <div class="log-box" id="logBox" style="display:none;"></div>
  </div>
</div>
<script>
(function() {
  const startBtn = document.getElementById('startBtn');
  const urlInput = document.getElementById('url');
  const timesInput = document.getElementById('times');
  const showBrowserCheck = document.getElementById('showBrowser');
  const statusBox = document.getElementById('statusBox');
  const statusText = document.getElementById('statusText');
  const logBox = document.getElementById('logBox');
  const progressBar = document.getElementById('progressBar');
  const progressFill = document.getElementById('progressFill');
  let currentJob = null;
  let pollTimer = null;
  let totalTimes = 0;

  startBtn.addEventListener('click', async function() {
    const url = urlInput.value.trim();
    const times = parseInt(timesInput.value, 10);
    const showBrowser = showBrowserCheck.checked;
    
    if (!url) {
      alert('请输入问卷链接');
      return;
    }
    
    totalTimes = times;
    startBtn.disabled = true;
    startBtn.textContent = '创建任务中...';
    statusBox.style.display = 'block';
    statusBox.className = 'status-box';
    statusText.textContent = '⏳ 正在创建任务...';
    logBox.style.display = 'block';
    logBox.textContent = '';
    progressBar.style.display = 'block';
    progressFill.style.width = '0%';
    
    try {
      const res = await fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, times, show_browser: showBrowser })
      });
      if (!res.ok) {
        const txt = await res.text();
        throw new Error(txt);
      }
      const data = await res.json();
      currentJob = data.job_id;
      statusText.textContent = '🔄 任务执行中';
      logBox.textContent = '任务 ID: ' + currentJob + '\\n';
      pollStatus();
    } catch (err) {
      statusBox.className = 'status-box status-error';
      statusText.textContent = '❌ 创建任务失败';
      logBox.textContent = err.message;
      startBtn.disabled = false;
      startBtn.textContent = '开始填写';
      progressBar.style.display = 'none';
    }
  });

  function pollStatus() {
    if (!currentJob) return;
    if (pollTimer) clearInterval(pollTimer);
    pollTimer = setInterval(async function() {
      try {
        const res = await fetch('/status/' + currentJob);
        if (!res.ok) return;
        const data = await res.json();
        
        const logs = data.logs || [];
        const completed = logs.length;
        const progress = totalTimes > 0 ? (completed / totalTimes * 100) : 0;
        progressFill.style.width = progress + '%';
        
        if (data.status === 'running') {
          statusBox.className = 'status-box status-running';
          statusText.textContent = '🔄 正在执行 (' + completed + '/' + totalTimes + ')';
        } else if (data.status === 'success') {
          statusBox.className = 'status-box status-success';
          statusText.textContent = '✓ 全部完成';
          progressFill.style.width = '100%';
        } else if (data.status === 'error') {
          statusBox.className = 'status-box status-error';
          statusText.textContent = '✕ 执行出错';
        }
        
        logBox.textContent = logs.join('\\n');
        if (data.error) {
          logBox.textContent += '\\n\\n错误详情：\\n' + data.error;
        }
        
        if (data.status === 'success' || data.status === 'error') {
          clearInterval(pollTimer);
          startBtn.disabled = false;
          startBtn.textContent = '开始填写';
        }
      } catch (e) {
        console.error(e);
      }
    }, 600);
  }
})();
</script>
</body>
</html>"""

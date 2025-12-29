HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>问卷星智能填写助手</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft YaHei', sans-serif; 
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.container {
  background: white;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  max-width: 600px;
  width: 100%;
  overflow: hidden;
}
.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 32px;
  text-align: center;
}
.header h1 {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 8px;
}
.header p {
  font-size: 14px;
  opacity: 0.9;
}
.content {
  padding: 32px;
}
.form-group {
  margin-bottom: 24px;
}
.form-group label {
  display: block;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 8px;
  font-size: 14px;
}
.form-group input[type="text"],
.form-group input[type="number"] {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: 14px;
  transition: all 0.3s;
  font-family: inherit;
}
.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}
.checkbox-group {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 24px;
}
.checkbox-group input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
  accent-color: #667eea;
}
.checkbox-group label {
  font-size: 14px;
  color: #4a5568;
  cursor: pointer;
  user-select: none;
}
.btn {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-family: inherit;
}
.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}
.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}
.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.status-box {
  margin-top: 24px;
  padding: 16px;
  border-radius: 10px;
  background: #f7fafc;
  border-left: 4px solid #667eea;
}
.status-box .status-label {
  font-size: 12px;
  color: #718096;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.status-box .status-text {
  font-size: 14px;
  color: #2d3748;
  font-weight: 500;
}
.log-box {
  margin-top: 16px;
  background: #1a202c;
  color: #e2e8f0;
  border-radius: 10px;
  padding: 16px;
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 13px;
  max-height: 240px;
  overflow-y: auto;
  line-height: 1.6;
  white-space: pre-wrap;
}
.log-box::-webkit-scrollbar {
  width: 8px;
}
.log-box::-webkit-scrollbar-track {
  background: #2d3748;
  border-radius: 10px;
}
.log-box::-webkit-scrollbar-thumb {
  background: #4a5568;
  border-radius: 10px;
}
.footer {
  padding: 20px 32px;
  background: #f7fafc;
  border-top: 1px solid #e2e8f0;
  font-size: 13px;
  color: #718096;
  text-align: center;
}
.footer code {
  background: #e2e8f0;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Consolas', monospace;
  color: #2d3748;
}
.status-running { border-left-color: #3182ce; }
.status-success { border-left-color: #38a169; }
.status-error { border-left-color: #e53e3e; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>📝 问卷星智能填写助手</h1>
    <p>快速、智能、自动化的问卷批量填写工具</p>
  </div>
  <div class="content">
    <div class="form-group">
      <label for="url">📋 问卷链接</label>
      <input type="text" id="url" placeholder="请输入问卷星问卷链接" value="https://www.wjx.cn/vm/QHzdwQy.aspx">
    </div>
    <div class="form-group">
      <label for="times">🔢 填写份数</label>
      <input type="number" id="times" min="1" max="50" value="3" placeholder="1-50">
    </div>
    <div class="checkbox-group">
      <input type="checkbox" id="showBrowser">
      <label for="showBrowser">🖥️ 显示浏览器界面（勾选后可实时查看填写过程）</label>
    </div>
    <button class="btn btn-primary" id="startBtn">🚀 开始填写</button>
    <div class="status-box" id="statusBox" style="display:none;">
      <div class="status-label">任务状态</div>
      <div class="status-text" id="statusText">等待中...</div>
    </div>
    <div class="log-box" id="logBox" style="display:none;"></div>
  </div>
  <div class="footer">
    💡 首次使用需安装浏览器：<code>python -m playwright install chromium</code>
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
  let currentJob = null;
  let pollTimer = null;

  startBtn.addEventListener('click', async function() {
    const url = urlInput.value.trim();
    const times = parseInt(timesInput.value, 10);
    const showBrowser = showBrowserCheck.checked;
    
    if (!url) {
      alert('请输入问卷链接');
      return;
    }
    
    startBtn.disabled = true;
    startBtn.textContent = '⏳ 创建任务中...';
    statusBox.style.display = 'block';
    statusBox.className = 'status-box';
    statusText.textContent = '正在创建任务...';
    logBox.style.display = 'block';
    logBox.textContent = '';
    
    try {
      const res = await fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, times, show_browser: showBrowser })
      });
      if (!res.ok) {
        const txt = await res.text();
        throw new Error('创建任务失败: ' + txt);
      }
      const data = await res.json();
      currentJob = data.job_id;
      statusText.textContent = '任务已创建，正在执行...';
      logBox.textContent = '任务 ID: ' + currentJob + '\\n';
      pollStatus();
    } catch (err) {
      statusBox.className = 'status-box status-error';
      statusText.textContent = '❌ 错误: ' + err.message;
      startBtn.disabled = false;
      startBtn.textContent = '🚀 开始填写';
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
        
        if (data.status === 'running') {
          statusBox.className = 'status-box status-running';
          statusText.textContent = '⚡ 正在运行中...';
        } else if (data.status === 'success') {
          statusBox.className = 'status-box status-success';
          statusText.textContent = '✅ 全部完成！';
        } else if (data.status === 'error') {
          statusBox.className = 'status-box status-error';
          statusText.textContent = '❌ 执行出错: ' + (data.error || '未知错误');
        }
        
        logBox.textContent = (data.logs || []).join('\\n');
        
        if (data.status === 'success' || data.status === 'error') {
          clearInterval(pollTimer);
          startBtn.disabled = false;
          startBtn.textContent = '🚀 开始填写';
        }
      } catch (e) {
        console.error(e);
      }
    }, 800);
  }
})();
</script>
</body>
</html>"""

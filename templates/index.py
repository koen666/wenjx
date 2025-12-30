HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>问卷星自动填写助手 - Glassmorphism Edition</title>
<style>
/* ========== CSS Variables ========== */
:root {
  --apple-blue: #007AFF;
  --apple-blue-dark: #0051D5;
  --apple-green: #34C759;
  --apple-red: #FF3B30;
  --text-primary: #1d1d1f;
  --text-secondary: #6e6e73;
  --text-tertiary: #86868b;
  --glass-white: rgba(255, 255, 255, 0.88);
  --glass-border: rgba(255, 255, 255, 0.4);
  --shadow-soft: 0 8px 32px rgba(31, 38, 135, 0.08);
  --shadow-medium: 0 16px 64px rgba(31, 38, 135, 0.12);
  --shadow-glow: 0 8px 32px rgba(0, 122, 255, 0.25);
}

/* ========== Reset & Base ========== */
* { 
  margin: 0; 
  padding: 0; 
  box-sizing: border-box; 
}

body { 
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', 'Helvetica Neue', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei UI', sans-serif; 
  background: 
    radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.15), transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(72, 149, 239, 0.15), transparent 50%),
    radial-gradient(circle at 40% 20%, rgba(169, 169, 188, 0.12), transparent 40%),
    linear-gradient(135deg, #F5F5F7 0%, #E8EAF6 50%, #F0F4F8 100%);
  background-attachment: fixed;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: var(--text-primary);
  position: relative;
  overflow-x: hidden;
}

/* Subtle animated grid overlay */
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    linear-gradient(rgba(0, 122, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 122, 255, 0.03) 1px, transparent 1px);
  background-size: 100px 100px;
  pointer-events: none;
  z-index: 0;
  opacity: 0.5;
  animation: gridPulse 15s ease-in-out infinite;
}

@keyframes gridPulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

/* ========== Main Container (Glassmorphism Card) ========== */
.container {
  position: relative;
  z-index: 1;
  background: var(--glass-white);
  backdrop-filter: saturate(180%) blur(25px);
  -webkit-backdrop-filter: saturate(180%) blur(25px);
  border-radius: 32px;
  box-shadow: 
    var(--shadow-medium),
    0 0 0 1px var(--glass-border) inset,
    0 2px 4px rgba(255, 255, 255, 0.8) inset;
  max-width: 640px;
  width: 100%;
  overflow: hidden;
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeInUp {
  from { 
    opacity: 0; 
    transform: translateY(40px) scale(0.96); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0) scale(1); 
  }
}

/* ========== Header ========== */
.header {
  padding: 56px 48px 40px;
  text-align: center;
  position: relative;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.5) 0%, transparent 100%);
}

.header h1 {
  font-size: 38px;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  margin-bottom: 12px;
  line-height: 1.1;
}

.header p {
  font-size: 16px;
  color: var(--text-secondary);
  font-weight: 400;
  line-height: 1.6;
  letter-spacing: -0.01em;
}

/* ========== Content Area ========== */
.content {
  padding: 0 48px 56px;
}

/* ========== Form Group ========== */
.form-group {
  margin-bottom: 32px;
}

.form-group label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 12px;
  font-size: 15px;
  letter-spacing: -0.02em;
}

.form-group label .icon {
  font-size: 17px;
  opacity: 0.7;
}

/* ========== Input Fields (Glassmorphism) ========== */
.form-group input[type="text"],
.form-group input[type="number"] {
  width: 100%;
  padding: 16px 18px;
  border: 1px solid rgba(0, 0, 0, 0.06);
  background: rgba(255, 255, 255, 0.65);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 16px;
  font-size: 15px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  color: var(--text-primary);
  box-shadow: 
    0 2px 8px rgba(31, 38, 135, 0.04),
    0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.form-group input::placeholder {
  color: var(--text-tertiary);
}

.form-group input:hover {
  border-color: rgba(0, 122, 255, 0.2);
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 
    0 4px 16px rgba(31, 38, 135, 0.06),
    0 0 0 1px rgba(255, 255, 255, 0.7) inset;
  transform: translateY(-1px);
}

.form-group input:focus {
  outline: none;
  border-color: var(--apple-blue);
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 
    0 8px 24px rgba(0, 122, 255, 0.18),
    0 0 0 4px rgba(0, 122, 255, 0.08),
    0 0 0 1px rgba(255, 255, 255, 0.9) inset;
  transform: translateY(-2px);
}

/* ========== Checkbox Group ========== */
.checkbox-group {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 32px;
  padding: 18px 20px;
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 16px;
  border: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(31, 38, 135, 0.04);
}

.checkbox-group:hover {
  background: rgba(255, 255, 255, 0.7);
  border-color: rgba(0, 122, 255, 0.2);
  box-shadow: 0 4px 16px rgba(31, 38, 135, 0.08);
  transform: translateY(-1px);
}

.checkbox-group input[type="checkbox"] {
  width: 24px;
  height: 24px;
  cursor: pointer;
  accent-color: var(--apple-blue);
  border-radius: 8px;
  flex-shrink: 0;
}

.checkbox-group label {
  font-size: 14px;
  color: var(--text-primary);
  cursor: pointer;
  user-select: none;
  font-weight: 500;
  line-height: 1.5;
  letter-spacing: -0.01em;
}

/* ========== Primary Button (Apple Style) ========== */
.btn {
  width: 100%;
  padding: 18px 24px;
  border: none;
  border-radius: 18px;
  font-size: 17px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-family: inherit;
  letter-spacing: -0.02em;
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: linear-gradient(180deg, #007AFF 0%, #0051D5 100%);
  color: white;
  box-shadow: 
    var(--shadow-glow),
    0 4px 12px rgba(0, 0, 0, 0.08),
    0 0 0 1px rgba(255, 255, 255, 0.2) inset;
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.5s;
}

.btn-primary:hover:not(:disabled)::before {
  left: 100%;
}

.btn-primary:hover:not(:disabled) {
  background: linear-gradient(180deg, #0051D5 0%, #003DA5 100%);
  box-shadow: 
    0 12px 40px rgba(0, 122, 255, 0.35),
    0 6px 16px rgba(0, 0, 0, 0.12),
    0 0 0 1px rgba(255, 255, 255, 0.3) inset;
  transform: translateY(-2px);
}

.btn-primary:active:not(:disabled) {
  transform: translateY(0) scale(0.98);
  box-shadow: 
    0 6px 20px rgba(0, 122, 255, 0.25),
    0 2px 8px rgba(0, 0, 0, 0.1);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  filter: saturate(0.7);
}

/* ========== Status Box ========== */
.status-box {
  margin-top: 32px;
  padding: 20px 24px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  box-shadow: 
    0 4px 16px rgba(31, 38, 135, 0.06),
    0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.status-box .status-label {
  font-size: 11px;
  color: var(--text-tertiary);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 12px;
}

.status-box .status-text {
  font-size: 16px;
  color: var(--text-primary);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  letter-spacing: -0.01em;
}

/* ========== Progress Bar ========== */
.progress-bar {
  margin-top: 16px;
  height: 8px;
  background: rgba(0, 0, 0, 0.08);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) inset;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #007AFF 0%, #0051D5 100%);
  border-radius: 10px;
  transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  width: 0%;
  box-shadow: 
    0 0 12px rgba(0, 122, 255, 0.4),
    0 0 0 1px rgba(255, 255, 255, 0.3) inset;
  position: relative;
  overflow: hidden;
}

.progress-fill::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  to { left: 100%; }
}

/* ========== Log Box (Terminal Style) ========== */
.log-box {
  margin-top: 20px;
  background: rgba(28, 28, 30, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 18px 20px;
  font-family: 'SF Mono', 'Monaco', 'Menlo', 'Consolas', 'Courier New', monospace;
  font-size: 12px;
  max-height: 240px;
  overflow-y: auto;
  line-height: 1.8;
  white-space: pre-wrap;
  color: #30D158;
  box-shadow: 
    0 8px 24px rgba(0, 0, 0, 0.3) inset,
    0 4px 16px rgba(0, 0, 0, 0.2);
  animation: fadeIn 0.4s ease-out;
}

/* Custom Scrollbar for Log Box */
.log-box::-webkit-scrollbar {
  width: 10px;
}

.log-box::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 5px;
  margin: 4px;
}

.log-box::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  border: 2px solid rgba(28, 28, 30, 0.95);
  transition: background 0.2s;
}

.log-box::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.35);
}

/* ========== Status State Variations ========== */
.status-running {
  border-color: rgba(0, 122, 255, 0.2);
  background: rgba(0, 122, 255, 0.06);
}

.status-running .status-text { 
  color: var(--apple-blue); 
}

.status-success {
  border-color: rgba(52, 199, 89, 0.2);
  background: rgba(52, 199, 89, 0.06);
}

.status-success .status-text { 
  color: var(--apple-green); 
}

.status-error {
  border-color: rgba(255, 59, 48, 0.2);
  background: rgba(255, 59, 48, 0.06);
}

.status-error .status-text { 
  color: var(--apple-red); 
}

/* ========== Responsive Design ========== */
@media (max-width: 640px) {
  body { 
    padding: 30px 16px; 
  }
  .container { 
    border-radius: 24px; 
    max-width: 100%;
  }
  .header { 
    padding: 40px 32px 32px; 
  }
  .header h1 { 
    font-size: 30px; 
  }
  .content { 
    padding: 0 32px 40px; 
  }
  .form-group {
    margin-bottom: 24px;
  }
  .checkbox-group {
    padding: 14px 16px;
  }
  .btn {
    padding: 16px 20px;
    font-size: 16px;
  }
}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>问卷星自动填写助手</h1>
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
      <div class="status-label">执行状态</div>
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

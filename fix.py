import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Add Chart.js CDN after </title>
html = html.replace(
    '</title>',
    '</title>\n  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'
)

# 2. Fill in all stub IC sections

cardiac_code = '''      // CARDIAC
      var c1 = baseOpts();
      mkChart('crhr', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'RHR', data: D.mrhv, borderColor: '#6c63ff', backgroundColor: 'rgba(108,99,255,0.1)', tension: 0.25, pointRadius: 2 }] }, options: c1 });
      var c2 = baseOpts();
      mkChart('chrv', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'HRV', data: D.hrvv, borderColor: '#22c55e', backgroundColor: 'rgba(34,197,94,0.1)', tension: 0.25, pointRadius: 2 }] }, options: c2 });
      var c3 = baseOpts();
      mkChart('cblood_bp', { type: 'line', data: { labels: D.bpsl, datasets: [{ label: 'Systolic', data: D.bpsv_sys, borderColor: '#6c63ff', tension: 0.25, pointRadius: 3 }, { label: 'Diastolic', data: D.bpsv_dia, borderColor: '#22c55e', tension: 0.25, pointRadius: 3 }] }, options: c3 });'''

overview_code = '''      // OVERVIEW
      var o1 = baseOpts();
      mkChart('car_hr', { type: 'bar', data: { labels: D.mrhl, datasets: [{ label: 'RHR', data: D.mrhv, backgroundColor: 'rgba(108,99,255,0.7)' }] }, options: o1 });
      var o2 = baseOpts();
      mkChart('ca_hrv', { type: 'bar', data: { labels: D.mrhl, datasets: [{ label: 'HRV', data: D.hrvv, backgroundColor: 'rgba(34,197,94,0.7)' }] }, options: o2 });
      var o3 = baseOpts();
      mkChart('ca_steps', { type: 'bar', data: { labels: D.mrhl, datasets: [{ label: 'Steps', data: D.stepsv, backgroundColor: 'rgba(249,115,22,0.7)' }] }, options: o3 });'''

body_code = '''      // BODY
      var b1 = baseOpts();
      mkChart('cb_weight', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'Weight (lb)', data: D.weightv, borderColor: '#6c63ff', backgroundColor: 'rgba(108,99,255,0.1)', tension: 0.25, pointRadius: 2 }] }, options: b1 });
      var b2 = baseOpts();
      mkChart('cb_bmi', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'BMI', data: D.bmiv, borderColor: '#f97316', backgroundColor: 'rgba(249,115,22,0.1)', tension: 0.25, pointRadius: 2 }] }, options: b2 });'''

activity_code = '''      // ACTIVITY
      var a1 = baseOpts();
      mkChart('cac_steps', { type: 'bar', data: { labels: D.mrhl, datasets: [{ label: 'Daily Steps', data: D.stepsv, backgroundColor: 'rgba(34,197,94,0.7)' }] }, options: a1 });
      var a2 = baseOpts();
      mkChart('cac_vo2', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'VO2 Max', data: D.vo2v, borderColor: '#6c63ff', tension: 0.25, pointRadius: 2 }] }, options: a2 });'''

sleep_code = '''      // SLEEP
      var sl1 = baseOpts();
      mkChart('csl_dur', { type: 'bar', data: { labels: D.mrhl, datasets: [{ label: 'Sleep (hrs)', data: D.sleepv, backgroundColor: 'rgba(108,99,255,0.7)' }] }, options: sl1 });'''

glucose_code = '''      // GLUCOSE
      var g1 = baseOpts();
      mkChart('cgl_hba1c', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'HbA1c', data: D.hba1cv, borderColor: '#ef4444', tension: 0.25, pointRadius: 3 }] }, options: g1 });'''

vitals_code = '''      // VITALS
      var v1 = baseOpts();
      mkChart('cvi_bp', { type: 'line', data: { labels: D.bpsl, datasets: [{ label: 'Systolic', data: D.bpsv_sys, borderColor: '#6c63ff', tension: 0.25, pointRadius: 2 }, { label: 'Diastolic', data: D.bpsv_dia, borderColor: '#22c55e', tension: 0.25, pointRadius: 2 }] }, options: v1 });'''

correlations_code = '''      // CORRELATIONS
      var cr1 = baseOpts();
      mkChart('ccr_hrv_ex', { type: 'scatter', data: { datasets: [{ label: 'HRV vs Exercise', data: D.cr_hrv_ex, backgroundColor: 'rgba(168,85,247,0.8)' }] }, options: cr1 });'''

analysis_code = '''      // ANALYSIS
      var an1 = baseOpts(); an1.scales.y.min = 10; an1.scales.y.max = 60;
      mkChart('can_vo2', { type: 'line', data: { labels: D.mrhl, datasets: [{ label: 'VO2 Max', data: D.vo2v, borderColor: '#6c63ff', tension: 0.25, pointRadius: 2 }] }, options: an1 });
      var an2 = baseOpts();
      mkChart('can_bp', { type: 'line', data: { labels: D.bpsl, datasets: [{ label: 'Systolic', data: D.bpsv_sys, borderColor: '#6c63ff', tension: 0.25, pointRadius: 3 }, { label: 'Diastolic', data: D.bpsv_dia, borderColor: '#22c55e', tension: 0.25, pointRadius: 3 }] }, options: an2 });
      var an3 = baseOpts();
      mkChart('can_wstd', { type: 'line', data: { labels: D.wstdl, datasets: [{ label: 'Walk Steadiness', data: D.wstdv, borderColor: '#f97316', tension: 0.25, pointRadius: 0 }] }, options: an3 });
      var an4 = baseOpts();
      mkChart('can_hrec', { type: 'line', data: { labels: D.hrecl, datasets: [{ label: 'HR Recovery', data: D.hrecv, borderColor: '#22c55e', tension: 0.25, pointRadius: 3 }] }, options: an4 });'''

# Apply replacements
html = html.replace('// Full-history cardiac charts', cardiac_code)
html = html.replace('// Overview summary charts', overview_code)
html = html.replace('// Body composition charts', body_code)
html = html.replace('// Activity & exercise charts', activity_code)
html = html.replace('// Sleep charts', sleep_code)
html = html.replace('// HbA1C time series chart', glucose_code)
html = html.replace('// Vitals charts', vitals_code)
html = html.replace('// Correlation charts', correlations_code)
html = html.replace('// Clinical view charts', analysis_code)

with open('index.html', 'w') as f:
    f.write(html)

print('Done! Chart.js added and all stub sections filled in.')

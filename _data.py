LEGACY_HTML = True  # 既存HTMLを保持（再アセンブル禁止）
TITLE = '電気代節約診断【無料】月々いくら安くなる？最適プランを提案'
DESCRIPTION = '家族構成・使用量を入力するだけで電気代を節約できる最適プランを無料診断。新電力・電力会社比較。'
JS_CODE = 'var Qs = [\n  { text:"世帯の人数は？", opts:["1人暮らし","2人（夫婦・カップル）","3〜4人（家族）","5人以上"], key:"members" },\n  { text:"現在の電力会社は？", opts:["東京電力・東電EP","関西電力","中部電力","新電力（その他）"], key:"provider" },\n  { text:"月の電気代はおよそいくらですか？", opts:["5,000円未満","5,000〜10,000円","10,000〜20,000円","20,000円以上"], key:"bill" },\n  { text:"住宅タイプは？", opts:["マンション・アパート","一戸建て"], key:"housing" },\n  { text:"エアコンの使用頻度は？", opts:["あまり使わない","普通（夏・冬のみ）","よく使う","ほぼ常時使用"], key:"ac" }\n];\nvar cur = 0, ans = {};\n\nfunction startDiagnosis() { show(\'questions\'); renderQ(); }\n\nfunction show(name) {\n  document.querySelectorAll(\'.screen\').forEach(function(s){ s.classList.remove(\'active\'); });\n  document.getElementById(\'screen-\'+name).classList.add(\'active\');\n}\n\nfunction renderQ() {\n  var q = Qs[cur];\n  var pct = Math.round((cur+1)/Qs.length*100);\n  document.getElementById(\'q-label\').textContent = \'質問 \'+(cur+1)+\' / \'+Qs.length;\n  document.getElementById(\'q-pct\').textContent = pct+\'%\';\n  document.getElementById(\'prog\').style.width = pct+\'%\';\n  document.getElementById(\'q-text\').textContent = q.text;\n  var c = document.getElementById(\'opts\'); c.innerHTML = \'\';\n  q.opts.forEach(function(opt, i) {\n    var b = document.createElement(\'button\');\n    b.className = \'option-btn\'; b.textContent = opt;\n    b.onclick = function() { pick(i, opt, q.key); };\n    c.appendChild(b);\n  });\n}\n\nfunction pick(i, val, key) {\n  ans[key] = {i:i, val:val};\n  document.querySelectorAll(\'.option-btn\').forEach(function(b,j){ b.classList.toggle(\'selected\',j===i); });\n  setTimeout(function(){\n    cur++;\n    if (cur < Qs.length) { renderQ(); } else { show(\'loading\'); setTimeout(showResults, 1600); }\n  }, 300);\n}\n\nfunction showResults() {\n  var billIdx = ans.bill ? ans.bill.i : 1;\n  var provIdx = ans.provider ? ans.provider.i : 0;\n  var acIdx = ans.ac ? ans.ac.i : 1;\n  var baseBills = [4000,8000,15000,25000];\n  var base = baseBills[billIdx];\n  var rates = [0.12,0.10,0.10,0.05];\n  var acBonus = [0,300,700,1500];\n  var saving = Math.round((base*rates[provIdx]+acBonus[acIdx])/100)*100;\n  var annual = saving*12;\n  document.getElementById(\'res-saving\').textContent = \'月 ¥\'+saving.toLocaleString();\n  document.getElementById(\'res-annual\').textContent = \'年間 ¥\'+annual.toLocaleString()+\'の節約\';\n  document.getElementById(\'res-annual-max\').textContent = \'¥\'+annual.toLocaleString();\n  var advice = provIdx<3 ? \'大手電力から新電力への切り替えで大幅な削減が期待できます。申し込みから最短2週間で切り替え完了です。\' : \'現在の新電力プランより安いプランへの変更で、さらに節約できる可能性があります。\';\n  document.getElementById(\'res-detail\').innerHTML = \'<div class="flex justify-between mb-2"><span>現在の想定月額</span><strong>¥\'+base.toLocaleString()+\'</strong></div><div class="flex justify-between mb-3"><span>削減後の推定月額</span><strong class="text-green-600">¥\'+(base-saving).toLocaleString()+\'</strong></div><p class="text-xs text-gray-500">\'+advice+\'</p>\';\n  show(\'results\');\n}\n\nfunction restart() { cur=0; ans={}; show(\'intro\'); }'
MAIN_HTML = '<div><button class="btn">開始する</button></div>'
FAQ = [
    ('電気代節約診断は無料で使えますか？', 'はい、完全無料・登録不要でご利用いただけます。'),
    ('何回でも使えますか？', 'はい、回数制限なく何度でもご利用いただけます。'),
    ('入力したデータはサーバーに送信されますか？', 'いいえ。すべての処理はブラウザ内で完結し、入力内容はサーバーへ送信されません。'),
    ('スマートフォンでも使えますか？', 'はい、スマートフォン・タブレット・PCすべてに最適化されています。'),
    ('結果を保存・共有できますか？', 'スクリーンショットでの保存またはSNSシェアボタンからご共有いただけます。'),
]
HOW_TO = [
    'ページを開き、入力フォームの項目を確認する',
    '必要な情報を入力または選択する',
    '実行ボタンをクリックして結果を取得する',
    '表示された結果・アドバイスを確認する',
    '必要に応じてコピー・SNSシェアで活用する',
]
FOOTER_LINKS = [('https://appadaycreator.com/electricity-plan-advisor/', '電力プラン診断'), ('https://appadaycreator.com/water-bill-reducer/', 'Water Bill Reducer'), ('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー')]

---
marp: true
theme: default
paginate: true
header: 'Space Invader × GitHub｜第二堂'
---

<!--
第二堂講稿(共約 3 小時,含兩次 10 分鐘休息)
時間配置:
  0:00–0:20  Part 1 複習 + 作業一檢討
  0:20–1:00  Part 2 帶做階段三:防護罩 + 爆炸特效
  (休息 10 分)
  1:10–1:55  Part 3 衝突處理(本堂重點)
  1:55–2:25  Part 3.5 回到過去的版本(歷史重現)+ 比差異(深入)
  (休息 10 分)
  2:35–2:50  Part 4 .gitignore + 分支清理 + 好習慣總整理
  2:50–3:00  收尾 + 預告作業二
-->

# Space Invader × GitHub
## 第二堂:進階功能 + 解決衝突

今天會遇到新手最怕、卻最該學會的關卡:**merge conflict**

---

## 今天結束時,你會

- 幫遊戲加上防護罩與擊落爆炸特效
- **看懂並親手解決一次 merge 衝突**
- 知道 `.gitignore` 是什麼、為什麼需要
- 養成「合併完就清分支」的收尾習慣

---

<!-- _class: lead -->
# Part 1
## 複習 + 作業一檢討(0:00–0:20)

---

## 上週的主軸,還記得嗎?

> 先拉、開枝、改存推、開 PR 合、再拉、剪枝

```
checkout main → pull → checkout -b feature
→ 改 → add → commit → push
→ 開 PR → Merge → checkout main → pull → branch -d
```

---

## 作業一檢討

- 你的功能分支長怎樣?
- commit 訊息清楚嗎?
- PR 的 Files changed 看得懂嗎?
- 有沒有記得合併後 pull + 刪分支?

> 一起看一兩位同學的 PR,互相學。

---

<!-- _class: lead -->
# Part 2
## 帶做階段三:防護罩 + 爆炸(0:20–1:05)

---

## 先照流程開分支

```bash
git checkout main && git pull
git checkout -b feature/bunkers
```

(衝突的部分我們等一下故意製造,先把功能做出來)

---

## 功能一:防護罩 bunkers

- 用 `spawn_bunkers()` 生成四座、由小方塊組成的牆
- 子彈(玩家或敵人)打到方塊 → 那塊消失、子彈消失
- 繪製時把每個方塊畫成青色

> 細節跟著 `stage3-bunkers.md`。

---

## 功能二:爆炸特效

- 用一個 `explosions` 清單記錄 `[x, y, 半徑]`
- 敵人被擊落時,在它的位置加一個爆炸
- 每幀讓半徑變大,太大就移除 → 擴散後消失的效果

---

## 測試一下

```bash
python space_invader.py
```

- 防護罩擋得住子彈嗎?被打會缺塊嗎?
- 擊落敵人有橘色爆炸嗎?

---

<!-- _class: lead -->
# Part 3
## 衝突處理(1:15–2:10)
### 本堂重點

---

## 衝突是什麼?

當**兩邊改了同一行**,Git 不知道聽誰的,就會 conflict。

今天我們**故意製造**一次,在安全環境學會處理它。
(平常不會這樣搞 main,這是教學特例)

---

## 製造衝突:Step 1 — 在 main 改一行

```bash
git checkout main && git pull
```

把分數顏色改成黃色:

```python
screen.blit(font.render(f"Score: {score}", True, YELLOW), (10, 10))
```

```bash
git add space_invader.py
git commit -m "style: 分數改成黃色"
git push
```

---

## 製造衝突:Step 2 — 分支改同一行成青色

回到你的功能分支,把同一行改成青色:

```python
screen.blit(font.render(f"Score: {score}", True, CYAN), (10, 10))
```

commit、push。
**現在 main 和分支都改了同一行 → 開 PR 會說有衝突。**

---

## 解決衝突:在本機把 main 併進來

```bash
git checkout feature/bunkers
git pull origin main        # 這時跳出衝突
```

打開檔案,你會看到這些記號 👇

---

## 衝突記號怎麼讀

```python
<<<<<<< HEAD
    ...青色...        ← 你這邊(分支)的版本
=======
    ...黃色...        ← main 的版本
>>>>>>> main
```

- `<<<<<<<` ~ `=======`:你的版本
- `=======` ~ `>>>>>>>`:對方(main)的版本

---

## 解決:挑一個,清乾淨

假設留青色,刪到只剩:

```python
    screen.blit(font.render(f"Score: {score}", True, CYAN), (10, 10))
```

⚠️ `<<<<<<<`、`=======`、`>>>>>>>` 三行記號**全部刪掉**,它們不是程式碼!

---

## 解決完,收尾

```bash
python space_invader.py      # 先確認沒壞
git add space_invader.py
git commit -m "merge: 解決分數顏色衝突,保留青色"
git push
```

回 GitHub:衝突警告消失,可以 Merge 了 ✅

---

## 心法

> 衝突不是錯誤,是 Git 在問你:
> **「這行,你要哪個版本?」**

你決定 → 清記號 → commit。就這樣。

---

<!-- _class: lead -->
# Part 3.5
## 回到過去的版本(1:55–2:25)

Git 最迷人的能力:**過去的版本都還在,看得到、回得去**

---

## 先複習:看歷史、找 hash

```bash
git log --oneline
```

```
5c0796e docs: 兩堂制改版
213591e feat: 加入 Space Invader 遊戲與教程   ← 想回到這個版本
```

前面那串 hash 就是版本的「身分證號」。

---

## A. 只想「看看」當時長怎樣

```bash
git checkout 213591e      # 時光機:整個專案變回當時
python space_invader.py   # 跑跑看最初版(沒命、沒關卡)
git checkout main         # 看完,回到現在
```

> Git 會說 "detached HEAD" —— 別怕,意思是「你正站在歷史某一點看風景」,`checkout main` 就回來了。

---

## B. 只還原「某一個檔案」到過去

```bash
git restore --source=213591e space_invader.py
```

只把這個檔變回當時,其他不動。要保留就照常 add + commit。

---

## C. 撤銷某次改動,但保留歷史

```bash
git revert 213591e
```

產生一個「反向 commit」抵銷那次改動。**不刪歷史**,團隊最推薦的反悔方式。

---

## ⚠️ 不要碰 `git reset --hard`

網路上常看到它「回到過去」,但它會**真的把後面歷史丟掉**,還會跟遠端打架。

> 新手一律用 A / B / C 三種安全做法就好。

---

## 比差異:兩個版本差在哪?

```bash
git diff 213591e 5c0796e      # 比較任意兩版本
git diff main feature/xxx     # 比較兩條分支
```

GitHub 上:commit 頁面、PR 的 Files changed、Compare 頁面都能看。

---

## 速查表

| 我想… | 用什麼 |
|--------|--------|
| 看歷史 | `git log --oneline` |
| 看某次改動 | `git show <hash>` |
| 比兩版本 | `git diff A B` |
| 看當時(會回來) | `git checkout <hash>` → `checkout main` |
| 還原單一檔 | `git restore --source=<hash> 檔名` |
| 撤銷某次(留歷史) | `git revert <hash>` |

詳見 `history-and-diff.md`

---

<!-- 休息 10 分鐘 -->
## ☕ 休息 10 分鐘

---

<!-- _class: lead -->
# Part 4
## .gitignore + 收尾好習慣(2:35–2:50)

---

## 跑過遊戲後多了什麼?

```bash
git status
# 會看到 __pycache__/ 這個資料夾
```

那是 Python 自動產生的暫存,**不該上傳**。

---

## .gitignore:叫 Git 忽略某些檔案

專案根目錄放一個 `.gitignore`:

```
__pycache__/
*.pyc
.vscode/
highscore.txt
```

列在裡面的,`git status` 就不會再囉嗦。

---

## 合併完,記得剪枝

```bash
git branch -d feature/bunkers              # 刪本機
git push origin --delete feature/bunkers   # 刪遠端
```

任務完成的分支不留著,repo 才乾淨。

---

## 完整流程(最終版,含收尾)

```
checkout main → pull → checkout -b feature
→ 改 → add → commit → push
→ 開 PR → (有衝突就解) → Merge
→ checkout main → pull
→ branch -d (本機) + 刪遠端分支
```

---

## 兩堂課總結

✅ 從零學會 Git / GitHub 協作
✅ 跑了多次完整 PR 流程
✅ **親手解決過 merge 衝突**
✅ 做出一個有命、有關卡、有防護罩的 Space Invader

---

## 📝 作業二(回家 2 小時)

自己做一個功能,並**刻意製造+解決一次衝突**。
詳見 `homework/homework2.md`。

---

<!-- _class: lead -->
# 兩堂課完成!
## 你已經會 GitHub 協作的核心了 🚀

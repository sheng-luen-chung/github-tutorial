# 看歷史、比差異、回到過去的版本

Git 最強的地方:**每一個過去的版本都還在,隨時看得到、回得去**。
這份講義教你三件事:① 看歷史 ② 比差異 ③ 回到當時的版本(歷史重現)。

---

## ① 看歷史:這個專案改過什麼?

```bash
git log                       # 完整歷史(按 q 離開)
git log --oneline             # 一行一個 commit,最常用
git log --oneline --graph     # 加上分支/合併的線條圖
git log --oneline -5          # 只看最近 5 筆
```

`--oneline` 長這樣,**最前面那串就是 commit 的「身分證號」(hash)**:

```
5b992ee Merge pull request #4 ...
c6e1a93 docs: 新增講師備課文件 teaching-plan
f4d1d9b Merge pull request #3 ...
213591e feat: 加入 Space Invader 遊戲與教程
```

> 之後要指定某個版本,就用這串 hash(打前 7 碼就夠)。

看某一個 commit 到底改了什麼:

```bash
git show 213591e             # 顯示這個 commit 的說明 + 完整改動
```

---

## ② 比差異:兩個版本差在哪?

`git diff` 是「比較器」。綠色 `+` 是新增的行,紅色 `-` 是刪掉的行。

```bash
git diff                     # 我「還沒 commit」的改動(工作區 vs 最後一次 commit)
git diff --staged            # 我已經 git add、但還沒 commit 的改動
git diff 213591e 5b992ee     # 比較任意兩個 commit
git diff 213591e             # 某個舊版本 vs 現在
git diff main feature/xxx    # 比較兩條分支
```

只想知道「哪些檔案動了」,不看細節:

```bash
git diff --stat 213591e 5b992ee
```

### 在 GitHub 上看差異(不用打指令)

- **PR 的 Files changed 分頁**:這條分支相對 main 改了什麼(你開 PR 時看過)
- **某個 commit 頁面**:點任一 commit,看它單獨的改動
- **Compare 頁面**:網址 `.../compare/版本A...版本B`,可比較任兩個版本/分支

---

## ③ 回到過去的版本(歷史重現)

這是重點。依「你想做什麼」分三種,**由安全到需要小心**:

### A. 只想「看看」當時長怎樣(看完再回來)

```bash
git checkout 213591e         # 時光機:整個專案變回那個 commit 的樣子
python space_invader.py      # 跑跑看當時的版本
git checkout main            # 看完,回到現在
```

> 這時 Git 會說你在 "detached HEAD"。別緊張,它只是提醒「你正站在歷史的某一點上看風景」。**只要 `git checkout main` 就回到現在**,什麼都不會壞。

### B. 只想把「某個檔案」還原成過去的樣子

```bash
git restore --source=213591e space_invader.py
```

把 `space_invader.py` 單獨變回 213591e 當時的內容,其他檔案不動。
這是「修改」,確認要保留的話照常 `git add` + `commit`。

### C. 想「撤銷」某個過去的 commit,但保留歷史紀錄

```bash
git revert 213591e           # 產生一個「反向」的新 commit,抵銷那次改動
```

`revert` 不會刪歷史,而是**新增一筆**「把那次改動還原回去」的 commit —— 安全、可追溯,團隊裡最推薦的「反悔」方式。

### ⚠️ 關於 `git reset --hard`

你可能在網路上看到 `git reset --hard` 也能回到過去。它會**真的把後面的歷史丟掉**,對新手很危險、也會跟遠端打架。**這堂課一律用上面 A/B/C 三種安全做法**,`reset --hard` 先不要碰。

---

## GitHub 上的「歷史重現」

- 在任一 commit 頁面,按 **`<> Browse the repository at this point`**,可以瀏覽當時整個專案的檔案。
- **Tag / Release**:想標記「這是 v1.0 版本」,可在某個 commit 上打 tag,日後一鍵回到那個里程碑。
  ```bash
  git tag v1.0 5b992ee
  git push origin v1.0
  ```

---

## 一句話總結

| 我想… | 用什麼 |
|--------|--------|
| 看改過什麼 | `git log --oneline` / `git show` |
| 比兩個版本差異 | `git diff A B`(或 GitHub Files changed) |
| 看當時長怎樣(看完回來) | `git checkout <hash>` → `git checkout main` |
| 還原單一檔案到過去 | `git restore --source=<hash> 檔名` |
| 撤銷某次改動(保留歷史) | `git revert <hash>` |

> 核心心法:**在 Git 裡,過去不會消失。看歷史、比差異、回到當時,都只是「換個角度看同一份歷史」而已。**

---
marp: true
theme: default
paginate: true
header: 'Space Invader × GitHub｜第一堂'
---

<!--
第一堂講稿(共約 3 小時,含兩次 10 分鐘休息)
時間配置:
  0:00–0:35  Part 1 Git 背景
  0:35–0:55  Part 2 工作流程總覽
  (休息 10 分)
  1:05–1:45  Part 3 帶做階段一:三條命(完整跑一次 PR)
  1:45–2:00  Part 3.5 看歷史與差異入門(log / diff / show)
  (休息 10 分)
  2:10–2:50  Part 4 帶做階段二:關卡系統(再跑一次 + Issue)
  2:50–3:00  收尾 + 預告作業一
-->

# Space Invader × GitHub
## 第一堂:Git 基礎 + 你的第一個 Pull Request

用做遊戲,把 GitHub 協作練到熟

---

## 今天結束時,你會

- 說得出 Git / GitHub 的差別,以及 commit / branch / PR 是什麼
- **獨立跑完一次**:拉 main → 開分支 → 改 → commit → push → PR → merge → 再拉
- 親手幫遊戲加上「三條命」和「關卡系統」兩個功能
- 帶著一份回家能自己練的作業

---

<!-- _class: lead -->
# Part 1
## Git 背景(0:00–0:40)

---

## 你一定做過這種事

```
報告_最終版.docx
報告_最終版_真的最終.docx
報告_最終版_這次真的最終.docx
```

- 改壞了 → 救不回來
- 兩個人一起改 → 互相覆蓋
- 想知道「上週改了什麼」→ 不可能

**Git 就是來解決這些的。**

---

## Git ≠ GitHub

| | 是什麼 | 類比 |
|---|---|---|
| **Git** | 你電腦上的工具,記錄版本 | 存檔系統 |
| **GitHub** | 網路平台,放專案+協作 | 雲端存檔 + 社群 |

Git 在你電腦裡跑;GitHub 在網路上。兩者分開,靠指令同步。

---

## 四個核心名詞

- **Repository(repo)**:一個專案資料夾,Git 在裡面記錄歷史
- **Commit**:某個時間點的存檔快照 + 一句說明
- **Branch(分支)**:平行開發線,亂改不影響正式版
- **main**:預設的「正式版」分支

---

## 最重要的觀念:本機 vs 遠端

```
   你的電腦 (local)            GitHub (remote)
   ┌────────────┐            ┌────────────┐
   │  commit    │  push →     │            │
   │            │  ← pull     │            │
   └────────────┘            └────────────┘
```

- **push**:本機 → GitHub
- **pull**:GitHub → 本機
- ⚠️ `commit` 只存在你電腦,沒 `push` 別人看不到!

---

## 為什麼不直接改 main?

直接改 main = 直接改「已上線的網站」,改壞大家遭殃。

正確做法:

> 開分支 → 在分支實驗 → 確定 OK → 用 PR 併回 main

**main 永遠保持乾淨可用。**

---

## Pull Request(PR)

PR = 「我這條分支改好了,請併進 main 好嗎?」的申請單

在 GitHub 上能:
- 看到改了哪些行(綠加、紅刪)
- 審查、留言
- 按 **Merge** 正式合併

公司、開源專案都靠它協作。

---

## 迷路時的萬用指令

```bash
git status      # 我現在改了什麼?下一步該做什麼?
```

> 卡住就打 `git status`,它幾乎都會告訴你怎麼辦。

---

<!-- _class: lead -->
# Part 2
## 工作流程總覽(0:40–1:00)

---

## 今天的主軸:每個功能跑一次這個循環

```
① git checkout main
② git pull                      ← 先拉最新 main
③ git checkout -b feature/xxx   ← 開分支
④ 改程式
⑤ git add + commit             ← 存快照
⑥ git push                     ← 上傳分支
⑦ GitHub 開 PR
⑧ GitHub 按 Merge
⑨ git checkout main
⑩ git pull                     ← 再拉回合併結果
⑪ git branch -d feature/xxx    ← 刪分支
```

---

## 一句話記住

> **先拉、開枝、改存推、開 PR 合、再拉、剪枝**

今天我們會用「三條命」和「關卡」兩個功能,各跑一次這個循環。

---

<!-- 休息 10 分鐘 -->
## ☕ 休息 10 分鐘

回來我們就開始動手寫程式。

---

<!-- _class: lead -->
# Part 3
## 帶做階段一:三條命(1:10–1:55)

完整跑第一次 PR 流程

---

## 先讓遊戲跑起來

```bash
git clone <repo 網址>
cd github-tutorial
python -m pip install pygame
python space_invader.py
```

操作:`←` `→` 移動、`空白鍵` 射擊、`R` 重來

---

## 步驟 ①②③:拉 main、開分支

```bash
git checkout main
git pull
git checkout -b feature/player-lives
git branch          # 確認 * 在新分支上
```

---

## 步驟 ④:改三個地方

1. 新增變數 `lives = 3`
2. 被擊中 → 扣一條命,歸零才結束
3. 右上角顯示 `Lives: 3`

> 細節跟著 `stage1-lives.md` 一步步做。

---

## 步驟 ⑤⑥:commit + push

```bash
python space_invader.py     # 先測!被打三次才 GAME OVER
git add space_invader.py
git commit -m "feat: 玩家三條命並顯示在右上角"
git push -u origin feature/player-lives
```

---

## 步驟 ⑦⑧:開 PR、Merge

1. GitHub 上點「Compare & pull request」
2. 填標題、內文 → Create
3. 看 **Files changed**(這就是 review 畫面)
4. 按 **Merge** → Confirm 🎉

---

## 步驟 ⑨⑩⑪:同步 + 清理

```bash
git checkout main
git pull                          # 把剛 merge 的抓回來
git branch -d feature/player-lives
```

**你剛剛獨立跑完了一次完整流程!**

---

<!-- _class: lead -->
# Part 3.5
## 看歷史與差異入門(1:45–2:00)

你剛做了好幾個 commit —— 現在來「讀」它們

---

## 看歷史:改過什麼?

```bash
git log --oneline        # 一行一個 commit
git log --oneline --graph
```

```
a1b2c3d feat: 玩家三條命並顯示在右上角
213591e feat: 加入 Space Invader 遊戲與教程
```

> 最前面那串是 commit 的「身分證號」(hash),指定版本就用它。

---

## 看某個 commit 改了什麼

```bash
git show a1b2c3d        # 那次 commit 的說明 + 完整改動
```

綠色 `+` = 新增的行,紅色 `-` = 刪掉的行。

---

## 比較兩個版本的差異

```bash
git diff                      # 我還沒 commit 的改動
git diff 213591e a1b2c3d      # 任意兩個版本之間
```

在 GitHub 上不用打指令:**PR 的 Files changed 分頁**就是在看差異。

> 完整版(含「回到過去的版本」)見 `history-and-diff.md`,第二堂會深入。

---

<!-- 休息 10 分鐘 -->
## ☕ 休息 10 分鐘

---

<!-- _class: lead -->
# Part 4
## 帶做階段二:關卡系統(2:10–2:50)

再跑一次 + 學用 Issue

---

## 這次多一個習慣:先開 Issue

GitHub → Issues → New issue

- 標題:`加入關卡系統`
- 內文:清空敵人後進下一關,敵人加速,顯示關卡
- 記下編號(例如 #1)

> Issue = 待辦事項 + 討論串,團隊用它分配工作。

---

## 開分支、改程式

```bash
git checkout main && git pull
git checkout -b feature/levels
```

改動:
- 把生成敵人抽成 `spawn_enemies()` 函式
- 清空敵人 → 關卡 +1、敵人加速、重生一波
- 畫面上方顯示 `Level N`

---

## 這次練「拆成小 commit」

```bash
git commit -m "refactor: 把生成敵人抽成 spawn_enemies()"
# ...再改...
git commit -m "feat: 加入關卡系統,敵人加速重生 (Closes #1)"
```

✨ 訊息寫 `Closes #1` → PR merge 後 Issue 自動關閉!

---

## 推上去、開 PR、合併、同步

```bash
git push -u origin feature/levels
# GitHub 開 PR → Merge
git checkout main && git pull
git branch -d feature/levels
```

去 Issues 分頁看:#1 已自動關閉 ✅

---

## 今天回顧

✅ 懂了 Git / GitHub / commit / branch / PR
✅ 親手跑了**兩次**完整 PR 流程
✅ 遊戲多了三條命 + 關卡系統
✅ 學會用 Issue 追蹤、寫好的 commit

---

## 📝 作業一(回家 2 小時)

自己挑一個小功能,**獨立**跑完整個流程做出來。
詳見 `homework/homework1.md`。

下週第二堂:防護罩、爆炸特效,還有最刺激的 **解決衝突**!

---

<!-- _class: lead -->
# 今天辛苦了!
## 有問題隨時問

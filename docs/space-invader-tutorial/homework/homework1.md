# 作業一:獨立跑完一次 PR 流程(約 2 小時)

> 第一堂課後練習。目標**不是**寫多厲害的功能,而是**自己一個人**把整個 GitHub 流程跑順。

## 任務

從下面三個小功能**任選一個**(或自己想一個難度差不多的),用完整流程做出來:

| 選項 | 要做的事 | 難度 |
|------|----------|------|
| A. 暫停鍵 | 按 `P` 暫停 / 繼續遊戲(暫停時敵人和子彈不動) | ⭐ |
| B. 加速移動 | 按住 `Shift` 時太空船移動變快 | ⭐ |
| C. 子彈數上限調整 | 把同時最多 5 顆子彈改成 3 顆,並讓敵人開火頻率提高 | ⭐ |

> 提示:暫停可以用一個 `paused = True/False` 變數,在更新邏輯外面包一層 `if not paused:`。

## 一定要照這個流程(這才是作業重點)

```bash
git checkout main
git pull                              # ① 先拉最新 main
git checkout -b feature/你的功能名      # ② 開分支
# ③ 改 space_invader.py
python space_invader.py               # ④ 測試
git add space_invader.py
git commit -m "feat: ..."             # ⑤ commit(訊息要清楚)
git push -u origin feature/你的功能名   # ⑥ push
# ⑦ 到 GitHub 開 PR、寫內文
# ⑧ 自己按 Merge
git checkout main
git pull                              # ⑨ 再拉回合併結果
git branch -d feature/你的功能名        # ⑩ 刪分支
```

## 做完後:讀讀自己的歷史(約 15 分鐘)

功能做完、PR merge 後,用這幾個指令「回頭看」自己改了什麼:

```bash
git log --oneline           # 看歷史,找出你那筆 commit 的 hash
git show <你的commit hash>   # 看那次 commit 到底改了哪些行
git diff <舊hash> <新hash>   # 比較「加功能前」和「加功能後」
```

> 這是在練 `history-and-diff.md` 的前半段(看歷史、比差異),第二堂會教「回到過去的版本」。

## 繳交方式

把你的 **PR 連結**貼給老師。我會看:

- [ ] 有一條 `feature/...` 分支(沒有直接改 main)
- [ ] commit 訊息清楚(不是 `update`、`123`)
- [ ] PR 有標題與簡單內文
- [ ] PR 已 merge,且本機 main 已 pull 同步
- [ ] 合併完的分支已刪除

## 卡住時

1. 先打 `git status`,看它怎麼說
2. 看錯誤訊息的**最後一行**
3. 對照 `solutions/` 裡的解答檔
4. 還是不行 → 截圖 `git status` 的結果問老師

## 加分(可選)

寫一段 3~5 行的心得:**這次流程裡哪一步你一開始不懂、後來怎麼想通的?**
（這比功能本身更重要 —— 我想知道你的卡點。）

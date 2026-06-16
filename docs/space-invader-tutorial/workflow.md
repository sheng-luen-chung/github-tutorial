# 標準工作流程(每次做功能都照這個跑)

這是整套教程的**主軸**。每加一個遊戲功能,就完整跑一次。跑到第三次,你就不用看這張表了。

## 一張圖看懂

```
（本機 main）                              （GitHub 遠端）
     │
 ① git checkout main
 ② git pull            ←──────────── 先把遠端最新的 main 抓下來
     │
 ③ git checkout -b feature/xxx   開一條分支來做這個功能
     │
 ④ 改程式碼
 ⑤ git add + git commit          拍存檔快照(可重複多次)
     │
 ⑥ git push -u origin feature/xxx ──────────→ 把分支上傳
     │
 ⑦ 在 GitHub 開 Pull Request
 ⑧ 在 GitHub 按 Merge            ──────────→ 分支併進遠端 main
     │
 ⑨ git checkout main
 ⑩ git pull            ←──────────── 把剛 merge 的結果抓回本機
     │
 ⑪ git branch -d feature/xxx     刪掉做完的分支(本機)
    （遠端分支在 PR 頁面按 Delete branch）
```

## 為什麼是這個順序?(高中生常見疑問)

| 步驟 | 為什麼非做不可 |
|------|----------------|
| ①② 先 pull main | 確保你是從「最新版」開始改。跳過它,之後容易跟別人的修改撞在一起。 |
| ③ 開分支 | 你的實驗都待在分支裡,**正式版 main 永遠是好的**。做壞了大不了刪分支。 |
| ⑤ commit | 每個 commit 是一個「可以回去的存檔點」。小步存檔,出錯才回得去。 |
| ⑥ push | commit 只存在你電腦裡,push 之後才上得了 GitHub、別人才看得到。 |
| ⑦⑧ PR + merge | PR 是「請求合併」的申請單,留下審查紀錄。合併動作在 GitHub 上完成。 |
| ⑩ 再 pull main | 合併發生在遠端,本機 main 還是舊的,要 pull 才會同步。 |
| ⑪ 刪分支 | 功能做完了,分支留著只會越積越亂。 |

## 對照指令速查

```bash
git checkout main                    # ①
git pull                             # ②
git checkout -b feature/my-feature   # ③
# ④ 用編輯器改 code
git add .                            # ⑤
git commit -m "feat: 做了什麼"        # ⑤
git push -u origin feature/my-feature# ⑥
# ⑦⑧ 到 GitHub 網頁開 PR、按 Merge
git checkout main                    # ⑨
git pull                             # ⑩
git branch -d feature/my-feature     # ⑪
```

> 💡 一句話記住整個流程:**「先拉、開枝、改存推、開 PR 合、再拉、剪枝」**。

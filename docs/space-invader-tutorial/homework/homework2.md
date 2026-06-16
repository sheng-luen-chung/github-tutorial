# 作業二:做一個功能 + 親手製造並解決一次衝突(約 2 小時)

> 第二堂課後練習。這次有兩個目標:(1) 再做一個功能,(2) **自己製造並解決一次 merge 衝突**。
> 衝突處理是新手最怕的,多練一次就不怕了。

## Part 1:做一個功能(約 40 分鐘)

任選一個(或自訂同等難度):

| 選項 | 要做的事 | 難度 |
|------|----------|------|
| A. 最高分紀錄 | 遊戲結束時把最高分存到 `highscore.txt`,開場顯示歷史最高 | ⭐⭐ |
| B. 雙排子彈 | 按 `空白鍵` 一次發射兩顆並排的子彈 | ⭐ |
| C. 敵人變色 | 不同排的敵人用不同顏色,被擊落分數不同 | ⭐⭐ |

> 選 A 的話:記得把 `highscore.txt` 加進 `.gitignore`,**不要**把存檔上傳。

照標準流程做(開分支 → 改 → commit → push → PR → merge → pull → 刪分支)。

## Part 2:製造並解決一次衝突(約 40 分鐘)

這部分**刻意**製造衝突來練習:

### Step 1 — 在 main 改某一行

```bash
git checkout main && git pull
```

挑一行容易改的(例如把視窗標題或某個顏色改掉),commit 並 push 到 main。

```python
pygame.display.set_caption("My Space Invader")   # 範例:改標題
```

### Step 2 — 開分支,改「同一行」成不同內容

```bash
git checkout -b feature/conflict-practice
```

把**同一行**改成別的內容,commit、push。

### Step 3 — 製造衝突並解決

```bash
git pull origin main         # 跳出衝突
```

打開檔案,你會看到:

```
<<<<<<< HEAD
你分支的版本
=======
main 的版本
>>>>>>> main
```

挑一個要留的、刪掉另一個、**把三行記號清乾淨**,然後:

```bash
python space_invader.py      # 確認沒壞
git add .
git commit -m "merge: 解決標題衝突"
git push
```

開 PR → Merge → 回本機 pull → 刪分支。

## Part 3:歷史重現 —— 回到過去的版本(約 30 分鐘)

對照 `history-and-diff.md`,實際操作一次「時光機」。

### Step 1 — 找出一個舊版本

```bash
git log --oneline          # 找一個「還沒加功能」的舊 commit,記下它的 hash
```

### Step 2 — 回到當時看看(看完要回來)

```bash
git checkout <舊hash>      # 整個專案變回當時
python space_invader.py    # 跑跑看舊版,跟現在比有什麼不同?
git checkout main          # 看完回到現在(很重要!)
```

### Step 3 — 比較兩個版本的差異

```bash
git diff <舊hash> main          # 看舊版到現在改了什麼
git diff --stat <舊hash> main   # 只看「哪些檔案動了」
```

> ⚠️ 全程不要用 `git reset --hard`。只用 `checkout`(看)、`diff`(比),安全又學得到東西。

## 繳交方式

貼給老師:

1. Part 1 功能的 **PR 連結**
2. Part 2 解決衝突那次的 **PR 連結**(或 commit 連結)
3. 回答三題:
   - 衝突記號裡 `=======` 上下兩段分別代表什麼?
   - 你解決衝突時留了哪個版本?為什麼?
   - Part 3 你回到的舊版本,跟現在最大的差別是什麼?(用 `git diff` 觀察)

## 檢查清單

- [ ] Part 1 功能正常,且走完整 PR 流程
- [ ] (若選 A)`highscore.txt` 有寫進 `.gitignore`
- [ ] Part 2 親手解決過一次衝突,記號清乾淨、遊戲還能跑
- [ ] Part 3 成功 `checkout` 到舊版本又回到 main,並用 `git diff` 比過差異
- [ ] 兩個 PR 都已 merge,本機 main 已同步、分支已清

## 加分(可選)

用 `git log --oneline` 截一張你目前的 commit 歷史圖,寫一句:**看著這串歷史,你覺得「分支 + PR」幫你避免了什麼麻煩?**
